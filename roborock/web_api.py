from __future__ import annotations

import base64
import hashlib
import hmac
import logging
import math
import secrets
import time

import aiohttp
from aiohttp import ContentTypeError

from roborock.containers import HomeData, HomeDataRoom, ProductResponse, RRiot, UserData
from roborock.exceptions import (
    RoborockAccountDoesNotExist,
    RoborockException,
    RoborockInvalidCode,
    RoborockInvalidCredentials,
    RoborockInvalidEmail,
    RoborockInvalidUserAgreement,
    RoborockMissingParameters,
    RoborockNoUserAgreement,
    RoborockTooFrequentCodeRequests,
    RoborockUrlException,
)

_LOGGER = logging.getLogger(__name__)


class RoborockApiClient:
    def __init__(self, username: str, base_url=None) -> None:
        """Sample API Client."""
        self._username = username
        self._default_url = "https://euiot.roborock.com"
        self.base_url = base_url
        self._device_identifier = secrets.token_urlsafe(16)

    async def _get_base_url(self) -> str:
        if not self.base_url:
            url_request = PreparedRequest(self._default_url)
            response = await url_request.request(
                "post",
                "/api/v1/getUrlByEmail",
                params={"email": self._username, "needtwostepauth": "false"},
            )
            if response is None:
                raise RoborockUrlException("get url by email returned None")
            response_code = response.get("code")
            if response_code != 200:
                if response_code == 2003:
                    raise RoborockInvalidEmail("Your email was incorrectly formatted.")
                elif response_code == 1001:
                    raise RoborockMissingParameters(
                        "You are missing parameters for this request, are you sure you " "entered your username?"
                    )
                raise RoborockUrlException(response.get("error"))
            response_data = response.get("data")
            if response_data is None:
                raise RoborockUrlException("response does not have 'data'")
            self.base_url = response_data.get("url")
        return self.base_url

    def _get_header_client_id(self):
        md5 = hashlib.md5()
        md5.update(self._username.encode())
        md5.update(self._device_identifier.encode())
        return base64.b64encode(md5.digest()).decode()

    def _get_hawk_authentication(self, rriot: RRiot, url: str) -> str:
        timestamp = math.floor(time.time())
        nonce = secrets.token_urlsafe(6)
        prestr = ":".join(
            [
                rriot.u,
                rriot.s,
                nonce,
                str(timestamp),
                hashlib.md5(url.encode()).hexdigest(),
                "",
                "",
            ]
        )
        mac = base64.b64encode(hmac.new(rriot.h.encode(), prestr.encode(), hashlib.sha256).digest()).decode()
        return f'Hawk id="{rriot.u}", s="{rriot.s}", ts="{timestamp}", nonce="{nonce}", mac="{mac}"'

    async def request_code(self) -> None:
        base_url = await self._get_base_url()
        header_clientid = self._get_header_client_id()
        code_request = PreparedRequest(base_url, {"header_clientid": header_clientid})

        code_response = await code_request.request(
            "post",
            "/api/v1/sendEmailCode",
            params={
                "username": self._username,
                "type": "auth",
            },
        )
        if code_response is None:
            raise RoborockException("Failed to get a response from send email code")
        response_code = code_response.get("code")
        if response_code != 200:
            if response_code == 2008:
                raise RoborockAccountDoesNotExist("Account does not exist - check your login and try again.")
            elif response_code == 9002:
                raise RoborockTooFrequentCodeRequests("You have attempted to request too many codes. Try again later")
            else:
                raise RoborockException(f"{code_response.get('msg')} - response code: {code_response.get('code')}")

    async def pass_login(self, password: str) -> UserData:
        base_url = await self._get_base_url()
        header_clientid = self._get_header_client_id()

        login_request = PreparedRequest(base_url, {"header_clientid": header_clientid})
        login_response = await login_request.request(
            "post",
            "/api/v1/login",
            params={
                "username": self._username,
                "password": password,
                "needtwostepauth": "false",
            },
        )
        if login_response is None:
            raise RoborockException("Login response is none")
        if login_response.get("code") != 200:
            raise RoborockException(f"{login_response.get('msg')} - response code: {login_response.get('code')}")
        user_data = login_response.get("data")
        if not isinstance(user_data, dict):
            raise RoborockException("Got unexpected data type for user_data")
        return UserData.from_dict(user_data)

    async def pass_login_v3(self, password: str) -> UserData:
        """Seemingly it follows the format below, but password is encrypted in some manner.
        # login_response = await login_request.request(
        #     "post",
        #     "/api/v3/auth/email/login",
        #     params={
        #         "email": self._username,
        #         "password": password,
        #         "twoStep": 1,
        #         "version": 0
        #     },
        # )
        """
        raise NotImplementedError("Pass_login_v3 has not yet been implemented")

    async def code_login(self, code) -> UserData:
        base_url = await self._get_base_url()
        header_clientid = self._get_header_client_id()

        login_request = PreparedRequest(base_url, {"header_clientid": header_clientid})
        login_response = await login_request.request(
            "post",
            "/api/v1/loginWithCode",
            params={
                "username": self._username,
                "verifycode": code,
                "verifycodetype": "AUTH_EMAIL_CODE",
            },
        )
        if login_response is None:
            raise RoborockException("Login request response is None")
        response_code = login_response.get("code")
        if response_code != 200:
            if response_code == 2018:
                raise RoborockInvalidCode("Invalid code - check your code and try again.")
            if response_code == 3009:
                raise RoborockNoUserAgreement("You must accept the user agreement in the Roborock app to continue.")
            if response_code == 3006:
                raise RoborockInvalidUserAgreement(
                    "User agreement must be accepted again - or you are attempting to use the Mi Home app account."
                )
            raise RoborockException(f"{login_response.get('msg')} - response code: {response_code}")
        user_data = login_response.get("data")
        if not isinstance(user_data, dict):
            raise RoborockException("Got unexpected data type for user_data")
        return UserData.from_dict(user_data)

    async def _get_home_id(self, user_data: UserData):
        base_url = await self._get_base_url()
        header_clientid = self._get_header_client_id()
        home_id_request = PreparedRequest(base_url, {"header_clientid": header_clientid})
        home_id_response = await home_id_request.request(
            "get",
            "/api/v1/getHomeDetail",
            headers={"Authorization": user_data.token},
        )
        if home_id_response is None:
            raise RoborockException("home_id_response is None")
        if home_id_response.get("code") != 200:
            if home_id_response.get("code") == 2010:
                raise RoborockInvalidCredentials(
                    f"Invalid credentials ({home_id_response.get('msg')}) - check your login and try again."
                )
            raise RoborockException(f"{home_id_response.get('msg')} - response code: {home_id_response.get('code')}")

        return home_id_response["data"].get("rrHomeId")

    async def get_home_data(self, user_data: UserData) -> HomeData:
        rriot = user_data.rriot
        if rriot is None:
            raise RoborockException("rriot is none")
        home_id = await self._get_home_id(user_data)
        if rriot.r.a is None:
            raise RoborockException("Missing field 'a' in rriot reference")
        home_request = PreparedRequest(
            rriot.r.a,
            {
                "Authorization": self._get_hawk_authentication(rriot, f"/user/homes/{str(home_id)}"),
            },
        )
        home_response = await home_request.request("get", "/user/homes/" + str(home_id))
        if not home_response.get("success"):
            raise RoborockException(home_response)
        home_data = home_response.get("result")
        if isinstance(home_data, dict):
            return HomeData.from_dict(home_data)
        else:
            raise RoborockException("home_response result was an unexpected type")

    async def get_home_data_v2(self, user_data: UserData) -> HomeData:
        """This is the same as get_home_data, but uses a different endpoint and includes non-robotic vacuums."""
        rriot = user_data.rriot
        if rriot is None:
            raise RoborockException("rriot is none")
        home_id = await self._get_home_id(user_data)
        if rriot.r.a is None:
            raise RoborockException("Missing field 'a' in rriot reference")
        home_request = PreparedRequest(
            rriot.r.a,
            {
                "Authorization": self._get_hawk_authentication(rriot, "/v2/user/homes/" + str(home_id)),
            },
        )
        home_response = await home_request.request("get", "/v2/user/homes/" + str(home_id))
        if not home_response.get("success"):
            raise RoborockException(home_response)
        home_data = home_response.get("result")
        if isinstance(home_data, dict):
            return HomeData.from_dict(home_data)
        else:
            raise RoborockException("home_response result was an unexpected type")

    async def get_rooms(self, user_data: UserData, home_id: int | None = None) -> list[HomeDataRoom]:
        rriot = user_data.rriot
        if rriot is None:
            raise RoborockException("rriot is none")
        if home_id is None:
            home_id = await self._get_home_id(user_data)
        if rriot.r.a is None:
            raise RoborockException("Missing field 'a' in rriot reference")
        room_request = PreparedRequest(
            rriot.r.a,
            {
                "Authorization": self._get_hawk_authentication(rriot, "/v2/user/homes/" + str(home_id)),
            },
        )
        room_response = await room_request.request("get", f"/user/homes/{str(home_id)}/rooms" + str(home_id))
        if not room_response.get("success"):
            raise RoborockException(room_response)
        rooms = room_response.get("result")
        if isinstance(rooms, list):
            output_list = []
            for room in rooms:
                output_list.append(HomeDataRoom.from_dict(room))
            return output_list
        else:
            raise RoborockException("home_response result was an unexpected type")

    async def get_products(self, user_data: UserData) -> ProductResponse:
        """Gets all products and their schemas, good for determining status codes and model numbers."""
        base_url = await self._get_base_url()
        header_clientid = self._get_header_client_id()
        product_request = PreparedRequest(base_url, {"header_clientid": header_clientid})
        product_response = await product_request.request(
            "get",
            "/api/v3/product",
            headers={"Authorization": user_data.token},
        )
        if product_response is None:
            raise RoborockException("home_id_response is None")
        if product_response.get("code") != 200:
            raise RoborockException(f"{product_response.get('msg')} - response code: {product_response.get('code')}")
        result = product_response.get("data")
        if isinstance(result, dict):
            return ProductResponse.from_dict(result)
        raise RoborockException("product result was an unexpected type")


class PreparedRequest:
    def __init__(self, base_url: str, base_headers: dict | None = None) -> None:
        self.base_url = base_url
        self.base_headers = base_headers or {}

    async def request(self, method: str, url: str, params=None, data=None, headers=None) -> dict:
        _url = "/".join(s.strip("/") for s in [self.base_url, url])
        _headers = {**self.base_headers, **(headers or {})}
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                    method,
                    _url,
                    params=params,
                    data=data,
                    headers=_headers,
                ) as resp:
                    return await resp.json()
            except ContentTypeError as err:
                """If we get an error, lets log everything for debugging."""
                try:
                    resp_json = await resp.json(content_type=None)
                    _LOGGER.info("Resp: %s", resp_json)
                except ContentTypeError as err_2:
                    _LOGGER.info(err_2)
                resp_raw = await resp.read()
                _LOGGER.info("Resp raw: %s", resp_raw)
                # Still raise the err so that it's clear it failed.
                raise err
