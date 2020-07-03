logger.info("== S T A R T == ")
logger.info("== Battery Replacement Logic == ")
today = datetime.datetime.now().date()

BATTERY_LIST = data.get("replaced", [])
# number oof days to turn on sensor.
SENSOR_ON_DAYS = data.get("sensor_on_days", [])
# Display can only be days or date
DISPLAY = data.get("display", [])
ENTITY_ID = data.get("entity_id", None)
sensor_on_days = data.get("sensor_on_days", None)
on_off = 'off'
friendly_name = data.get("friendly_name", None)
icon = data.get("icon", None)
SensorName = "sensor.{}".format(ENTITY_ID.replace(" " , "_"))

BATTERY_LIST_NEW = {'friendly_name' : friendly_name ,'icon' : icon ,'Battery = Usage':'Next'}

def Get_state(entity_id):
    check_time = today
    state = hass.states.get(entity_id)
    return state.state  

def Get_name(entity_id):
    check_time = today
    state = hass.states.get(entity_id)
    return state.name 

for battery in BATTERY_LIST:
    aa = battery.split(",")
    battery_ID = aa[0].rstrip()
    replaced_it =  aa[1].rstrip()
    #logger.info("battery_name =  '%s' ",battery_ID)
    #logger.info("replaceit =  '%s' ",replaced_it)
    dateSplit = replaced_it.split("/")
    dateDay = int(dateSplit[0])
    dateMonth = int(dateSplit[1])
    dateYear =  int(dateSplit[2])
    battery_st = datetime.date(dateYear,dateMonth,dateDay)
    battery_age_days = int((today - battery_st).days)
    #logger.info("battery_age_days = %s ",battery_age_days)
    battery_name = Get_name(battery_ID)
    battery_state = int(100 - int(Get_state(battery_ID)))
    #logger.info("battery_state = %s ",battery_state)
    if battery_state > 0:
        battery_per_day = (battery_state / battery_age_days)
        #logger.info("battery_per_day = %s ",battery_per_day)
        battery_per_day = int((100 / battery_per_day))
        #logger.info("battery_per_day = %s ",battery_per_day)
        if (battery_per_day <= sensor_on_days):
            on_off = 'on'
        else:
            on_off = 'off'
        battery_next = battery_st + datetime.timedelta(days=battery_per_day)
        if DISPLAY == "days":
            BATTERY_LIST_NEW[battery_name + ' = ' + str(battery_state) +'%']  =  str(battery_per_day) + ' day(s)'
        else:
            BATTERY_LIST_NEW[battery_name]  =  '{}/{}/{}'.format(battery_next.day,battery_next.month,battery_next.year)
    else:
        BATTERY_LIST_NEW[battery_name]  = '--'

hass.states.set(SensorName , on_off , BATTERY_LIST_NEW )

#logger.info("== E N D == %s created",SensorName)


