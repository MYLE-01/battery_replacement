# Battery Replacement

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

want to learn python and give back to home assistant
I have a lot of sensor that tell me the battery level % used


![battery](https://github.com/MYLE-01/battery_replacement/blob/master/battery_level.PNG)

so as I know the date I replace the battery ( 01/07/2020 ) dd/mm/yy   Dimmer Switch Battery Level

so between 01/07/2020 and now 06/07/2020 it has used 50% battery left 

so my logic is for 5 day its used 50% then it will take other 5 days and it be flat. right

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

in the replaced:
list the battery sensor , and the date it was replace

```yaml
- sensor.dryer_door_battery , 01/01/2020
```
key | required | type | description
-- | -- | -- | --
replaced: | True | string | entity_id , dd/mm/yyyy 
sensor_on_days: | True |number| number of days sensor set to on
entity_id: |True|string| the name of the new entity_id:
friendly_name:| True| string|the display name
icon: | True | string | its icon 
display: | True | string | days to shows days count of date to show date next change




