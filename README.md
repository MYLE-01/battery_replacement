# Battery Replacement

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

I have a lot of sensor that tell me the battery level % 

![battery](https://github.com/MYLE-01/battery_replacement/blob/master/img/battery_level.PNG)

## Update 16/09/2020
It can now create a replacement sensor.

![Replacement](https://github.com/MYLE-01/battery_replacement/blob/master/img/replacement.PNG)

```yaml
card:
  type: entities
  title: Battery Replacement
filter:
  include:
    - entity_id: sensor.replacement*
type: 'custom:auto-entities'
```

Its popup

![Newpopup](https://github.com/MYLE-01/battery_replacement/blob/master/img/newpopup.PNG)

https://github.com/MYLE-01/battery_replacement/blob/master/img/newpopup.PNG

## How it works
This script creates a sensor that guesses the next battery change base of % Used and date of replacement

Requires `python_script:` to be enabled in you configuration


## My logic (my thinking is ....)
so as I know the date I replace the battery ( 01/07/2020 ) dd/mm/yy  Dimmer Switch Battery Level

so my logic is
If between 01/07/2020 and now 06/07/2020 it has used 50% of battery.

If for 5 day its used 50% then it will take other 5 days and it be flat. base of these 5 days been the same as the last 5 days 

So all we need to do is tell a python script the entity_id of battery and the date we replace it 
and run it once a day and at startup of home assistant

remember: the maths is base on the % level at the battery the script was run and date it was given.
 
so we have the entity_id , replacement date dd/mm/yyy
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
      replacement_sensor: 'Yes'
      replace_patten: '_battery_level'
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
replacement_sensor: | yes/no | String | Make replacement sensor
replace_patten: | '_battery_level' | String | what you want taken out of old entity_id

the replace_patten is
used if you and "custom:auto-entities" have a filter "sensor.*.battery_level*"

eg this is mine

```yaml
card:
  align: split
  columns: 1
  height: 20
  title_position: inside
  type: 'custom:bar-card'
  unit_of_measurement: '%'
  width: 100%
filter:
  include:
    - entity_id: sensor.*.battery_level*
      state: <=100
type: 'custom:auto-entities'
```
which create the 

![Bar](https://github.com/MYLE-01/battery_replacement/blob/master/img/bar.PNG)

as I dont want to mixing so I used a replace to taken out the *.battery_level*


so this automation runs on start and at 00:00:01 midnite

```yaml
- alias: Do a percentage check on battery work replace days
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
          replacement_sensor: 'Yes'
          replace_patten: '_battery_level'
          entity_id: status_battery
          friendly_name: Battery Status 
          icon: mdi:calendar-star
          display: days
        service: python_script.battery_replacement
        
```        

its popup

![battery](https://github.com/MYLE-01/battery_replacement/blob/master/img/popup.PNG)

if you have the custom:fold-entity-row you can put them into a card
```yaml
entities:
  - entity: sensor.status_battery
  - head: script.python_script_battery
    items:
      - card:
          type: entities
        filter:
          include:
            - entity_id: sensor.replacement*
        type: 'custom:auto-entities'
    type: 'custom:fold-entity-row'

```


sorry about the bad english i have dyslexia taken me more time to right this than right the code.
