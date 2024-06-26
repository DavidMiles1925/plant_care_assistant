
import os
import RPi.GPIO as GPIO
import subprocess
from smbus import SMBus
from datetime import datetime
from time import sleep

from config import ADS_BYTE_ADDRESS,\
            ADS_COMMANDS, \
            CLEAR_SCREEN_BEFORE_PRINT, \
            DRY_COUNT_BEFORE_WATERING, \
            DURATION_BETWEEN_CHECKS, \
            DRY_SOIL_VALUE, \
            DRY_VALUE, \
            LED_ARRAY_WATER_STATUS, \
            LIGHT_SCRIPT_PATH, \
            MOIST_SOIL_VALUE, \
            NUMBER_OF_ANALOG_INPUTS, \
            OPENING_MESSAGE, \
            PUMP_ON_TIME, \
            WET_SOIL_VALUE, \
            WATER_VALUE, \
            WATER_IF_DRY, \
            WATER_PUMP_ARRAY
            
from logger import console_and_log

# Bus
bus = SMBus(1)

# List that will be used to keep track of 
is_dry_list = []

def check_if_water_is_needed(analog_input):
    global is_dry_list

    if is_dry_list[analog_input] >= DRY_COUNT_BEFORE_WATERING and WATER_IF_DRY:
        water_plant(analog_input)





def determine_soil_moisture(value, analog_input):
    global is_dry_list

    if value >= DRY_VALUE:
        is_dry_list[analog_input] = is_dry_list[analog_input] + 1
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.HIGH)
        return "Dry: No Soil"
    
    elif value >= DRY_SOIL_VALUE:
        is_dry_list[analog_input] = is_dry_list[analog_input] + 1
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.HIGH)
        return "Dry Soil    "
    
    elif value >= MOIST_SOIL_VALUE:
        is_dry_list[analog_input] = 0
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.LOW)
        return "Moist Soil  "
    
    elif value >= WET_SOIL_VALUE:
        is_dry_list[analog_input] = 0
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.LOW)
        return "Wet Soil    "
    
    elif value >= WATER_VALUE:
        is_dry_list[analog_input] = 0
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.LOW)
        return "Water       "
    else:
        return "Low Value"


def output_sensor_data(value, status, analog_input):
    global is_dry_list

    console_and_log(f"Sensor: {analog_input+1}\t{status}\t\t({value})\t\t[count: {is_dry_list[analog_input]}]")
    #console_and_log(f"{status}")


def read_sensor(input):
    bus.write_byte(ADS_BYTE_ADDRESS, ADS_COMMANDS[input])
    return bus.read_byte(ADS_BYTE_ADDRESS)


def setup_pins():
    # Board Mode: BCM
        GPIO.setmode(GPIO.BCM)

        # Disable Warnings
        GPIO.setwarnings(False)

        for led in range(len(LED_ARRAY_WATER_STATUS)):
            GPIO.setup(LED_ARRAY_WATER_STATUS[led], GPIO.OUT)
            GPIO.output(LED_ARRAY_WATER_STATUS[led], GPIO.HIGH)

        for pin in range(len(WATER_PUMP_ARRAY)):
            GPIO.setup(WATER_PUMP_ARRAY[pin], GPIO.OUT)
            GPIO.output(WATER_PUMP_ARRAY[pin], GPIO.LOW)


def toggle_pump(value, analog_input):
    GPIO.output(WATER_PUMP_ARRAY[analog_input], value)


def water_plant(analog_input):
    global is_dry_list

    toggle_pump(True, analog_input)

    sleep(PUMP_ON_TIME)

    toggle_pump(False, analog_input)

    console_and_log(f"*****WATER DISPENSED: Sensor {analog_input + 1}*****")

    is_dry_list[analog_input] = 0


if __name__ == "__main__":
    try:
        # Start script to turn the light on/off at specified time.
        subprocess.Popen(["sudo", "python", LIGHT_SCRIPT_PATH])

        setup_pins()

        os.system("clear")

        console_and_log(OPENING_MESSAGE)
        
        # Set up a counter for each moisture sensor to keep track of how long they have been dry.
        for input_counter in range(NUMBER_OF_ANALOG_INPUTS):
            is_dry_list.append(1)

        while True:

            # Collect metrics for each input and water plants if necessary
            for analog_input in range(NUMBER_OF_ANALOG_INPUTS):
                sensor_value = read_sensor(analog_input)

                soil_status = determine_soil_moisture(sensor_value, analog_input)
                
                output_sensor_data(sensor_value, soil_status, analog_input)

                check_if_water_is_needed(analog_input)


            sleep(DURATION_BETWEEN_CHECKS)

            if CLEAR_SCREEN_BEFORE_PRINT:
                os.system("clear")

    except Exception as e:
        console_and_log(f"An exception was caught in the main function: {e}\n\n\n")
        GPIO.cleanup()

    except KeyboardInterrupt:
        console_and_log(f"The moisture program was terminated using Ctrl+C\n\n\n")
        GPIO.cleanup()