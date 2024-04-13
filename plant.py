from smbus import SMBus
from time import sleep
import os

from config import ADS_COMMANDS, DURATION_BETWEEN_CHECKS, OPENING_MESSAGE, DRY_VALUE, DRY_SOIL_VALUE, MOIST_SOIL_VALUE, WET_SOIL_VALUE, WATER_VALUE, CLEAR_SCREEN_BEFORE_PRINT, DRY_COUNT_BEFORE_WATERING
from logger import console_and_log

bus = SMBus(1)
is_dry_counter = 0

def read_sensor(input):
    bus.write_byte(0x4b, ADS_COMMANDS[input])
    return bus.read_byte(0x4b)


def output_sensor_data(value, status):
    global is_dry_counter

    if CLEAR_SCREEN_BEFORE_PRINT:
        os.system("clear")

    console_and_log(f"{status} ({value}) [count: {is_dry_counter}]")


def determine_soil_status(value):
    global is_dry_counter

    if value >= DRY_VALUE:
        is_dry_counter = is_dry_counter + 1
        return "Dry: No Soil"
    
    elif value >= DRY_SOIL_VALUE:
        is_dry_counter = is_dry_counter + 1
        return "Dry Soil"
    
    elif value >= MOIST_SOIL_VALUE:
        is_dry_counter = 0
        return "Moist Soil"
    
    elif value >= WET_SOIL_VALUE:
        is_dry_counter = 0
        return "Wet Soil"
    
    elif value >= WATER_VALUE:
        is_dry_counter = 0
        return "Water"
    else:
        return "Low Value"
    
def check_water_status():
    global is_dry_counter

    if is_dry_counter >= DRY_COUNT_BEFORE_WATERING:
        water_plant()
        
    

def water_plant():
    global is_dry_counter

    console_and_log("*****WATER DISPENSED*****")

    is_dry_counter = 0


if __name__ == "__main__":
    try:
        os.system("clear")
        console_and_log(OPENING_MESSAGE)

        while True:
            sensor_value = read_sensor(0)

            soil_status = determine_soil_status(sensor_value)
            
            output_sensor_data(sensor_value, soil_status)

            check_water_status()

            sleep(DURATION_BETWEEN_CHECKS)

    except Exception as e:
        console_and_log(f"An exception was caught in the main function: {e}\n\n\n")

    except KeyboardInterrupt:
        console_and_log(f"The program was terminated using Ctrl+C\n\n\n")