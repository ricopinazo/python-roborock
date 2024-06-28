Api commands
============
This page is still under construction. All of the following are the commands we have reverse engineered. It is not an exhaustive list of all the possible commands.

Commands do not immediately make it to this page. You can find more commands [here](https://github.com/humbertogontijo/python-roborock/blob/main/roborock/roborock_typing.py#L18)

Commands can have multiple parameters that can change from one model to another.

* :ref:`app_charge`
* :ref:`app_get_dryer_setting`
* :ref:`app_get_init_status`
* :ref:`app_pause`
* :ref:`app_rc_end`
* :ref:`app_rc_move`
* :ref:`app_rc_start`
* :ref:`app_rc_stop`
* :ref:`app_segment_clean`
* :ref:`app_set_dryer_setting`
* :ref:`app_start_collect_dust`
* :ref:`app_start_wash`
* :ref:`app_start`
* :ref:`app_stop_collect_dust`
* :ref:`app_stop_wash`
* :ref:`app_stop`
* :ref:`change_sound_volume`
* :ref:`close_dnd_timer`
* :ref:`del_server_timer`
* :ref:`dnld_install_sound`
* :ref:`get_clean_sequence`
* :ref:`get_consumable`
* :ref:`get_custom_mode`
* :ref:`get_customize_clean_mode`
* :ref:`get_dnd_timer`
* :ref:`get_dust_collection_mode`
* :ref:`get_clean_follow_ground_material_status`
* :ref:`get_identify_furniture_status`
* :ref:`get_identify_ground_material_status`
* :ref:`get_led_status`
* :ref:`get_map_v1`
* :ref:`get_multi_map`
* :ref:`get_multi_maps_list`
* :ref:`get_network_info`
* :ref:`get_prop`
* :ref:`get_room_mapping`
* :ref:`get_scenes_valid_tids`
* :ref:`get_serial_number`
* :ref:`get_smart_wash_params`
* :ref:`get_sound_progress`
* :ref:`get_status`
* :ref:`get_timezone`
* :ref:`get_turn_server`
* :ref:`get_valley_electricity_timer`
* :ref:`get_wash_towel_mode`
* :ref:`load_multi_map`
* :ref:`name_segment`
* :ref:`reset_consumable`
* :ref:`resume_segment_clean`
* :ref:`resume_zoned_clean`
* :ref:`retry_request`
* :ref:`reunion_scenes`
* :ref:`save_map`
* :ref:`send_ice_to_robot`
* :ref:`send_sdp_to_robot`
* :ref:`set_server_timer`
* :ref:`set_clean_motor_mode`
* :ref:`set_customize_clean_mode`
* :ref:`set_dnd_timer`
* :ref:`set_dust_collection_mode`
* :ref:`set_fds_endpoint`
* :ref:`set_identify_furniture_status`
* :ref:`set_identify_ground_material_status`
* :ref:`set_led_status`
* :ref:`set_mop_mode`
* :ref:`set_scenes_segments`
* :ref:`set_scenes_zones`
* :ref:`set_segment_ground_material`
* :ref:`set_smart_wash_params`
* :ref:`set_timezone`
* :ref:`set_valley_electricity_timer`
* :ref:`set_wash_towel_mode`
* :ref:`set_water_box_custom_mode`
* :ref:`start_camera_preview`
* :ref:`start_edit_map`
* :ref:`start_voice_chat`
* :ref:`start_wash_then_charge`
* :ref:`stop_camera_preview`
* :ref:`stop_segment_clean`
* :ref:`test_sound_volume`
* :ref:`upd_server_timer`


Robot status
------------

get_status
~~~~~~~~~~

Description: Returns the current status of the vacuum

Parameters: None

Returns:

    msg_ver:

    msg_seq:

    state:

    battery: Battery level of your device.

    clean_time: Total clean time in hours.

    clean_area: Total clean area in meters.

    error_code:

    map_reset:

    in_cleaning:

    in_returning:

    in_fresh_state:

    lab_status:

    water_box_status:

    back_type:

    wash_phase:

    wash_ready:

    fan_power:

    dnd_enabled:

    map_status:

    is_locating:

    lock_status:

    water_box_mode:

    water_box_carriage_status:

    mop_forbidden_enable:

    camera_status:

    is_exploring:

    home_sec_status:

    home_sec_enable_password:

    adbumper_status:

    water_shortage_status:

    dock_type:

    dust_collection_status:

    auto_dust_collection:

    avoid_count:

    mop_mode:

    debug_mode:

    collision_avoid_status:

    switch_map_mode:

    dock_error_status:

    charge_status:

    unsave_map_reason:

    unsave_map_flag:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

App vacuum control
------------------

app_start
~~~~~~~~~

Description:

Parameters:

app_pause
~~~~~~~~~

Description: This pauses the vacuum's current task

Parameters: None

Returns ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

app_stop
~~~~~~~~

Description:

Parameters:


app_start_collect_dust
~~~~~~~~~~~~~~~~~~~~~~

Description: This empties the bin while docked

Parameters: None

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

app_stop_collect_dust
~~~~~~~~~~~~~~~~~~~~~~

Description: This stops the emptying of the dust bin while docked

Parameters: None

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

app_start_wash
~~~~~~~~~~~~~~

Description: This washes the mop while docked

Parameters: None

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========


app_stop_wash
~~~~~~~~~~~~~

Description: This stops washing the mop whiloe docked

Parameters: None

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

app_goto_target
~~~~~~~~~~~~~~~

Description: Got to target

Parameters:
    - X coordinate as integer (e.g.: 23450)
    - Y coordinate as integer (e.g.: 16450)

Returns ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

app_charge
~~~~~~~~~~

Description: This tells your vacuum to go back to the dock and charge.

Parameters: None

Returns : ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


App status
----------

app_get_init_status
~~~~~~~~~~~~~~~~~~~

Description: Returns details on the app being used to interact with Roborock servers ?? In this case  the app is backend supporting the HA integration ?

Parameters: None

Returns:

     local_info:

        name: Name of the app

        bom: Version of the app

        location: Location of the app

        language: Language of the app

        wifiplan: Wifi plan of the app

        timezone: Timezone of the app

        logserver: Log server of the app

        featureset: Featureset of the app

     feature_info: List of features

     new_feature_info: New feature info

Return example::
    {'local_info': {'name': 'custom_A.03.0342_CE', 'bom': 'A.03.0342', 'location': 'de', 'language': 'en', 'wifiplan': '', 'timezone': 'Europe/Berlin', 'logserver': 'awsde0.fds.api.xiaomi.com', 'featureset': 3}, 'feature_info': [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125], 'new_feature_info': 2247395306799103, 'new_feature_info_str': '00000008009EFFFE'}


======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

App dryer settings
------------------

app_get_dryer_setting
~~~~~~~~~~~~~~~~~~~~~

Description: Get dock dryer settings.

Parameters: None

Returns:

    status:

    on:

        cliff_on:

        cliff_off

        count:

        dry_time: Duration dryer remains on in seconds.

    off:

        cliff_on:

        cliff_off:

        count:

Return example::

    {'status': 1, 'on': {'cliff_on': 1, 'cliff_off': 1, 'count': 10, 'dry_time': 7200}, 'off': {'cliff_on': 2, 'cliff_off': 1, 'count': 10}}

Source: Roborock S7 MaxV Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

app_set_dryer_setting
~~~~~~~~~~~~~~~~~~~~~

Description: Set the time for the dryer to run

Parameters:  '{"status":1,"on":{"dry_time":14400}}'

dry_time is the time in seconds the dryer will run for

Returns ok or error


======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

App remote control
------------------

app_rc_start
~~~~~~~~~~~~

Description: Starts remote control.

Parameters: None

Returns ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========


app_rc_move
~~~~~~~~~~~

Description: Moves the robot in the direction specified

Parameters: To be documented

Returns ok or error

..
    Need to document the parameters - will need to explore the app to find out what they are


app_rc_stop
~~~~~~~~~~~

Description: Stops the remote control

Parameters: None

Returns ok or error

..
    Assume stop stops a move ?? Need to check

app_rc_end
~~~~~~~~~~

Description: Ends the remote control task

Parameters:

Returns ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========



App other
---------

app_set_smart_cliff_forbidden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:


app_spot
~~~~~~~~

Description:

Parameters:


app_stat
~~~~~~~~

Description: This returns the current status of the vacuum

Parameters: None

Returns: ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

app_wakeup_robot
~~~~~~~~~~~~~~~~

Description:

Parameters:


app_zoned_clean
~~~~~~~~~~~~~~~

Description: Starts a zone clean

Parameters:

..
    Us this the last known zone

Returns: ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

Segments and Zones
------------------

app_segment_clean
~~~~~~~~~~~~~~~~~

Description: This starts a segment clean and repeats it the number of times specified.

Parameters: An array of segments to clean. Each segment is an integer with the segment id and the number of times to clean it. For example, to clean segment 18 twice, the parameter would be

 [{'segments': [18], 'repeat': 2}]

.. Comment: The segment id can be obtained from the initial data returned on login

Command:
    roborock -d command --device_id deviceIdRedacted --cmd app_segment_clean --params '[{"segments": [17,19], "repeat": 2}]'

Returns ok or error

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_segment_ground_material
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description: Sets the groud material for the segment

Parameters: "{'data':[[22,3,0]]}"

Returns ok or error

name_segment
~~~~~~~~~~~~

Description:

Parameters: To be determined

..
    Need to work out parameter format
    Does this allow us to name a segment ?


resume_segment_clean
~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

stop_segment_clean
~~~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_scenes_zones
~~~~~~~~~~~~~~~~

Description:

Parameters:

set_scenes_segments
~~~~~~~~~~~~~~~~~~~

Description:

Parameters:


get_scenes_valid_tids
~~~~~~~~~~~~~~~~~~~~~

Description: To be confirmed

Parameters: None

..
    Appears to be associated with rooms ??

Returns::

[{'tid': '1699679077347', 'map_flag': 0, 'segs': [{'sid': 24}, {'sid': 20}, {'sid': 22}, {'sid': 18}]}, {'tid': '1699679236553', 'map_flag': 0, 'segs': [{'sid': 24}, {'sid': 20}, {'sid': 22}]}, {'tid': '1699679386045', 'map_flag': 0, 'segs': [{'sid': 16}, {'sid': 19}, {'sid': 17}]}, {'tid': '1699679335823', 'map_flag': 0, 'segs': [{'sid': 19}, {'sid': 16}, {'sid': 17}]}]

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

resume_zoned_clean
~~~~~~~~~~~~~~~~~~

Description:

Parameters:

reunion_scenes
~~~~~~~~~~~~~~

Description:

Parameters:

Camera
------

start_camera_preview
~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========

stop_camera_preview
~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========

get_camera_status
~~~~~~~~~~~~~~~~~

Description: Get camera status.

Parameters: None

Returns: 3457
         387 Roborock S8 Pro Ultra

Source: Roborock S7 MaxV Ultra


set_camera_status
~~~~~~~~~~~~~~~~~

Description:

Parameters:



start_voice_chat
~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========


Clean modes
-----------------

get_carpet_clean_mode
~~~~~~~~~~~~~~~~~~~~~

Description: Get carpet clean mode.

Parameters:

Returns:

    carpet_clean_mode: Enumeration for carpet clean mode.

Return example::

    {'carpet_clean_mode': 3}

Source: Roborock S7 MaxV Ultra


set_carpet_clean_mode
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

get_carpet_mode
~~~~~~~~~~~~~~~

Description:

Parameters: None

Returns:

    enable:

    current_integral:

    current_high:

    current_low:

    stall_time:

Return example::

    {'enable': 1, 'current_integral': 450, 'current_high': 500, 'current_low': 400, 'stall_time': 10}

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

set_carpet_mode
~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

get_smart_wash_params
~~~~~~~~~~~~~~~~~~~~~

Description: Returns the smartwash parameters

Parameters: None

..
    Not clear what this does

Returns:

        smart_wash: 0 is off, 1 is on

        wash_interval: The interval in seconds between washes

Example::

{'smart_wash': 0, 'wash_interval': 1200}


======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_smart_wash_params
~~~~~~~~~~~~~~~~~~~~~

Description: Sets the smartwash parameters

Parameters:

        smart_wash: 0 is off, 1 is on

        wash_interval: The interval in seconds between washes


{'smart_wash': 0, 'wash_interval': 1200}


======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

Cleaning history
----------------

get_clean_record
~~~~~~~~~~~~~~~~

Description:

Parameters: To be determined


get_clean_record_map
~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:


get_clean_sequence
~~~~~~~~~~~~~~~~~~

Description:

Parameters:


get_clean_summary
~~~~~~~~~~~~~~~~~

Description: Get a summary of cleaning history.

Parameters: None

Returns:

    clean_time:

    clean_area:

    clean_count:

    dust_collection_count:

    records:

Return example::

    {'clean_time': 568146, 'clean_area': 8816865000, 'clean_count': 178, 'dust_collection_count': 172, 'records': [1689740211, 1689555788, 1689259450, 1688999113, 1688852350, 1688693213, 1688692357, 1688614354, 1688613280, 1688606676, 1688325265, 1688174717, 1688149381, 1688092832, 1688001593, 1687921414, 1687890618, 1687743256, 1687655018, 1687631444]}

Source: Roborock S7 MaxV Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


get_mop_template_params_summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========

Child lock
----------

get_child_lock_status
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description: This gets the child lock status of the device. 0 is off, 1 is on.

Parameters: None

Returns:

    lock_status:

Return example::

    {'lock_status': 0}

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_child_lock_status
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description: This sets the child lock status of the device.

Parameters: '{"lock_status" :0}'

Returns: ok

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========




Consumables
-----------

get_consumable
~~~~~~~~~~~~~~

Description: This gets the status of all of the consumables for your device.

Parameters: None

Returns:

    main_brush_work_time: This is the amount of time the main brush has been used in seconds since it was last replaced

    side_brush_work_time:  This is the amount of time the side brush has been used in seconds since it was last replaced

    filter_work_time: This is the amount of time the air filter inside the vacuum has been used in seconds since it was last replaced

    filter_element_work_time:

    sensor_dirty_time: This is the amount of time since you have cleaned the sensors on the bottom of your vacuum.

    strainer_work_times:

    dust_collection_work_times:

    cleaning_brush_work_times:

Return examples::

    {'main_brush_work_time': 14151, 'side_brush_work_time': 41638, 'filter_work_time': 14151, 'filter_element_work_time': 0, 'sensor_dirty_time': 41522, 'strainer_work_times': 44, 'dust_collection_work_times': 19, 'cleaning_brush_work_times': 44}


reset_consumable
~~~~~~~~~~~~~~~~

Description:

Parameters: List of consumables to reset. For example, to reset consumables 'strainer_work_times' and 'sensor_dirty_time' the parameter would be

 ['strainer_work_times', 'sensor_dirty_time']

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


Custom modes
------------

get_custom_mode
~~~~~~~~~~~~~~~~~~~~

Description: It returns the current custom mode.

Parameters: None

Returns:

    integer value of the current custom mode

Return example::

    102

..
  Not clear what a custom mode is = will explore

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

set_custom_mode
~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

get_customize_clean_mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:


set_customize_clean_mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

Furniture and ground material
-----------------------------

get_identify_furniture_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

..
    Does not return anything for S8 Pro Ultra when docked may require vacumm to be cleaning

set_identify_furniture_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

..
    Method not known for S8 Pro Ultra


get_identify_ground_material_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

..
    Does not return anything for S8 Pro Ultra when docked may require vacumm to be cleaning


set_identify_ground_material_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

..
    Method not known for S8 Pro Ultra



LEDs
----

get_flow_led_status
~~~~~~~~~~~~~~~~~~~

Description:

Parameters:


set_flow_led_status
~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

get_led_status
~~~~~~~~~~~~~~~~~~~

Description: Returns the LED status. If disabled the indicator light will turn off 1 minute after fully charged

Parameters:

Returns:

    led_status: 0 is off, 1 is on


======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_led_status
~~~~~~~~~~~~~~

Description:  Sets the LED status. If disabled the indicator light will turn off 1 minute after fully charged

Parameters: ????

..
    Need to work out parameter format




Maps
----

get_multi_map
~~~~~~~~~~~~~

Description:

Parameters:

Comment: Response timed out for S8 Pro Ultra

..
    times out after 4 secs

get_multi_maps_list
~~~~~~~~~~~~~~~~~~~

Description: Returns a list of map information stored on the device.

Parameters: None required

Returns:

    max_multi_map:
    max_bak_map:
    multi_map_count:
    map_info::

            mapFlag:
            add_time:
            length:
            name:
            bak_maps::

                mapFlag:
                add_time:


Return example::

    {'max_multi_map': 4, 'max_bak_map': 1, 'multi_map_count': 2, 'map_info': [{'mapFlag': 0, 'add_time': 1699919699, 'length': 4, 'name': 'Home', 'bak_maps': [{'mapFlag': 4, 'add_time': 1699823921}]}, {'mapFlag': 1, 'add_time': 1699828035, 'length': 13, 'name': 'Boys bathroom', 'bak_maps': [{'mapFlag': 5, 'add_time': 1699828035}]}]}

Source: S8 Pro Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

get_map_v1
~~~~~~~~~~

Description: Returns the map

Parameters: Unknown

Comment: Returns a map in a format that is not yet understood by me

..
    Explore what parameters it may take
    Extend code to return byte stream ?

start_edit_map
~~~~~~~~~~~~~~

Description:

Parameters:


get_room_mapping
~~~~~~~~~~~~~~~~

Description: Returns a list of rooms, ids as discovered by

Parameters: None

Returns:

    room_id

Return example::

    [[16, '14731399', 12], [17, '2220009', 2], [18, '2219688', 12], [19, '2219685', 9], [20, '2219691', 12], [21, '2431758', 12], [22, '2219677', 13], [23, '2312548', 12], [24, '2219678', 14], [25, '2219686', 15], [26, '2219772', 12], [27, '14768755', 12]]

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

load_multi_map
~~~~~~~~~~~~~~

Description:

Parameters: number (the floor/map index)

..
    Need to work out parameter format


save_map
~~~~~~~~

Description:

Parameters:

Operating modes
---------------

get_mop_mode
~~~~~~~~~~~~

Description: Get mop mode.

Parameters: None

Returns: Enumeration for mop mode. 300

Example for S8 Pro Ultra::

    standard = 300
    deep = 301
    deep_plus = 303
    fast = 304
    custom = 302

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_mop_mode
~~~~~~~~~~~~

Description: Set mop mode.

Parameters: mop_mode 300

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_clean_motor_mode
~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

get_dust_collection_mode
~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters: None

Returns:

    mode:

Return example::

    {'mode': 0}

Source: Roborock S7 MaxV Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


set_dust_collection_mode
~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

get_wash_towel_mode
~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters: None

Returns:

    wash_mode:

Return example::

    {'wash_mode': 1}

Source: Roborock S7 MaxV Ultra


    unknown = -9999

    light = 0

    balanced = 1

    deep = 2


======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


set_wash_towel_mode
~~~~~~~~~~~~~~~~~~~~~~~~

Description: Sets the wash wash_towel_mode

Parameters: {'wash_mode': 2}

Returns: ok or error

Source: S8 Pro Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

get_collision_avoid_status
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters: None

Returns:

    status:

Return example::

    {'status': 1}

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


set_collision_avoid_status
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description: Update collision avoid status.

Parameters: '{"status" :1}'

Returns:

    ok

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


start_wash_then_charge
~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

..
    While this returns ok on the S8 Pro Ultra it does not appear to do anything

switch_water_mark
~~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========

..
    Not found for S8 Pro Ultra

System information
------------------

get_network_info
~~~~~~~~~~~~~~~~

Description: Get the device's network information.

Parameters: None

Returns:

    ssid: SSID of the wirelness network the device is connected to.

    ip: IP address of the device.

    mac: MAC address of the device.

    bssid: BSSID of the device.

    rssi: RSSI of the device.

Return example::

    {'ssid': 'My WiFi Network', 'ip': '192.168.1.29', 'mac': 'a0:2b:47:3d:24:51', 'bssid': '18:3b:1a:23:41:3c', 'rssi': -32}

Source: Roborock S7 MaxV Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


get_serial_number
~~~~~~~~~~~~~~~~~

Description: Get serial number of the vacuum.

Parameters: None

Returns::

    serial_number: Serial number of the vacuum.

Return example::

    {'serial_number': 'B16EVD12345678'}

Source: Roborock S7 MaxV Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

get_prop
~~~~~~~~

Description: Generic get property command

Parameters: The property to get

Example::

    roborock -d command --device_id aHiddenDeviceId --cmd get_prop --params '["battery"]'



Comment : This example returns the same as get_status. Initial testing has shown that not all get commands are supported by this method


get_turn_server
~~~~~~~~~~~~~~~

Description:

Parameters:

..
    Not found for S8 Pro Ultra

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========


enable_log_upload
~~~~~~~~~~~~~~~~~

Description:

Parameters:


find_me
~~~~~~~

Description: This makes your vacuum speak so you can find it.

Parameters: None

upd_server_timer
~~~~~~~~~~~~~~~~

Description:

Parameters:

get_homesec_connect_status
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========


set_fds_endpoint
~~~~~~~~~~~~~~~~

Description:

Parameters:

send_ice_to_robot
~~~~~~~~~~~~~~~~~

Description:

Parameters:


send_sdp_to_robot
~~~~~~~~~~~~~~~~~

Description:

Parameters:

get_device_ice
~~~~~~~~~~~~~~

..
    This doeas not appear to be supported on S8 Pro Ultra

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========

get_device_sdp
~~~~~~~~~~~~~~

Description:

Parameters:

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   No
======================  =========

retry_request
~~~~~~~~~~~~~

Description:

Parameters:

Timers
------

del_server_timer
~~~~~~~~~~~~~~~~

Description:

Parameters:


dnd_timer
~~~~~~~~~

get_dnd_timer
~~~~~~~~~~~~~

Description: Gets the do not disturb timer

    start_hour: The hour you want dnd to start

    start_minute: The minute you want dnd to start

    end_hour: The hour you want dnd to be turned off

    end_minute: The minute you want dnd to be turned off

    enabled: If the switch is currently turned on in the app for DnD

Parameters: None


set_dnd_timer
~~~~~~~~~~~~~

Description:

Parameters:


close_dnd_timer
~~~~~~~~~~~~~~~

Description: This disables the dnd timer

Parameters: None

get_server_timer
~~~~~~~~~~~~~~~~

Description:

Parameters:


set_server_timer
~~~~~~~~~~~~~~~~

Description:

Parameters:

get_timezone
~~~~~~~~~~~~~~~~~

Description: Get the device's time zone.

Parameters: None

Returns: Time zone by the TZ identifier (e.g., America/Los_Angeles)

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========


set_timezone
~~~~~~~~~~~~~~~~~

Description: Sets the device's time zone

Parameters:





Sound
------------

get_sound_volume
~~~~~~~~~~~~~~~~

Description: Returns the volume of the sound played by the vacuum

Parameters: None

Returns:

    volume: The volume of the sound played by the vacuum

Example::

    72

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

change_sound_volume
~~~~~~~~~~~~~~~~~~~

Description: Sets the volume of the sound played by the vacuum

Parameters: volume

Returns: ok or error

roborock -d command --device_id aHiddenDeviceId --cmd change_sound_volume --params 72

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

test_sound_volume
~~~~~~~~~~~~~~~~~

Description: Plays a sound on the vacumm to identity volume

Parameters: None

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========


get_sound_progress
~~~~~~~~~~~~~~~~~~

Description:

Parameters:

Returns::

{'sid_in_progress': 0, 'progress': 0, 'state': 0, 'error': 0}

..
    Is this where the vacumm is currently located ?


get_current_sound
~~~~~~~~~~~~~~~~~

..
    Is this an app setting ?

Description:

Parameters:

Return example::

    {'sid_in_use': 122, 'sid_version': 1, 'sid_in_progress': 0, 'location': 'de', 'bom': 'A.03.0342', 'language': 'en', 'msg_ver': 2}

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S7 MaxV Ultra  Yes
Roborock S8 Pro Ultra   Yes
======================  =========

dnld_install_sound
~~~~~~~~~~~~~~~~~~

Description:

Parameters:

Off peak charging
-----------------

get_valley_electricity_timer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:  Get valley electricity timer.

Parameters: None

Returns:

    start_hour: The hour you want valley electricity to start

    start_minute: The minute you want valley electricity to start

    end_hour: The hour you want valley electricity to be turned off

    end_minute: The minute you want valley electricity to be turned off

    enabled: If the switch is currently turned on in the app for valley electricity


```
{'start_hour': 0, 'start_minute': 0, 'end_hour': 0, 'end_minute': 0, 'enabled': 0}
```

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_valley_electricity_timer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description: Sets the valley electricity timer

Parameters:

    start_hour: The hour you want valley electricity to start

    start_minute: The minute you want valley electricity to start

    end_hour: The hour you want valley electricity to be turned off

    end_minute: The minute you want valley electricity to be turned off

    enabled: If the switch is currently turned on in the app for valley electricity

Example::

{'start_hour': 0, 'start_minute': 0, 'end_hour': 0, 'end_minute': 0, 'enabled': 0}


..
    This does not appear to have any effect on the S8 Pro Ultra - Params accepted however no affect ??

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   ???
======================  =========




Water box mode
--------------

get_water_box_custom_mode
~~~~~~~~~~~~~~~~~~~~~~~~~

Description: Get water box mode.

Parameters: None

Returns: Enumeration for water box mode. 203

..
    Not clear what this does - require Enumeration


get_clean_follow_ground_material_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:

Parameters: None
======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========

set_water_box_custom_mode
~~~~~~~~~~~~~~~~~~~~~~~~~

Description: Set the water box mode.

Parameters: {'water_box_mode': 203}

Returns: ok or error

..
    Not clear what this does - require Enumeration

======================  =========
Vacuum Model            Supported
======================  =========
Roborock S8 Pro Ultra   Yes
======================  =========
