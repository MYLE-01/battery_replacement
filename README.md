# Battery Replacement

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

want to learn python and give back to home assistant
I have a lot of sensor that tell me the battery level % used


![battery](https://github.com/MYLE-01/battery_replacement/blob/master/img/battery_level.PNG)


## How it works
This script creates a sensor that work out weather you are on/off for today
with a heap of attribute 

Requires `python_script:` to be enabled in you configuration


## my logic
so as I know the date I replace the battery ( 01/07/2020 ) dd/mm/yy   Dimmer Switch Battery Level

so my logic is
if between 01/07/2020 and now 06/07/2020 it has used 50% battery left 

 for 5 day its used 50% then it will take other 5 days and it be flat. right
 
 so all we need to do is tell a python script  the entity_id of battery and its date i replace it 
 
```yaml
- sensor.dryer_door_battery , 01/01/2020
```

putting it all together

```yaml
  - data:
      replaced:
      - sensor.dryer_door_battery , 01/01/2020
      - sensor.dimmer_switch_battery_level , 01/02/2020
      - sensor.bathroom_battery_level , 08/06/2020
      - sensor.cupboard_battery_level , 08/06/2020
      - sensor.hall_battery , 05/05/2020
      - sensor.lounge_battery_level , 08/06/2020
      sensor_on_days: 30
      entity_id: status_battery
      friendly_name: Battery Status 
      icon: mdi:calendar-star
      display: days
```

# what is required

key | required | type | description
-- | -- | -- | --
replaced: | True | string | entity_id , its replace date in format or dd/mm/yyyy 
sensor_on_days: | True |number| number of days sensor set to on
entity_id: |True|string| the name of the new entity_id:
friendly_name:| True| string|the display name
icon: | True | string | its icon 
display: | True | string | days to shows days count of date to show date next change


so this automation runs on start and at 00:00:01 midnite

```yaml
- alias: Reminder - Refresh date countdown sensors
    initial_state: on
    trigger:
      - platform: time
        at: '00:00:01'
      - platform: homeassistant
        event: start
    action:
      - data:
          replaced:
          - sensor.dryer_door_battery , 01/01/2020
          - sensor.dimmer_switch_battery_level , 01/02/2020
          - sensor.bathroom_battery_level , 08/06/2020
          - sensor.cupboard_battery_level , 08/06/2020
          - sensor.hall_battery , 05/05/2020
          - sensor.lounge_battery_level , 08/06/2020
          sensor_on_days: 30
          entity_id: status_battery
          friendly_name: Battery Status 
          icon: mdi:calendar-star
          display: days
        service: python_script.battery_replacement
        
```        

its popup

![battery](https://github.com/MYLE-01/battery_replacement/blob/master/img/popup.PNG)


