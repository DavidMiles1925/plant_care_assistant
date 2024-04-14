from smbus import SMBus
from time import sleep
import os
import RPi.GPIO as GPIO

from config import ADS_COMMANDS, DURATION_BETWEEN_CHECKS, OPENING_MESSAGE, DRY_VALUE, DRY_SOIL_VALUE, MOIST_SOIL_VALUE, WET_SOIL_VALUE, WATER_VALUE, CLEAR_SCREEN_BEFORE_PRINT, DRY_COUNT_BEFORE_WATERING, WATER_IF_DRY, NUMBER_OF_ANALOG_INPUTS, LED_ARRAY_WATER_STATUS
from logger import console_and_log

bus = SMBus(1)
is_dry_counter = 0

#Substitue for actually watering
BLUE_LED = 23

def setup_pins():
    # Board Mode: BCM
        GPIO.setmode(GPIO.BCM)

        # Disable Warnings
        GPIO.setwarnings(False)

        GPIO.setup(BLUE_LED, GPIO.OUT)
        GPIO.output(BLUE_LED, GPIO.LOW)

        for led in range(len(LED_ARRAY_WATER_STATUS)):
            GPIO.setup(LED_ARRAY_WATER_STATUS[led], GPIO.OUT)
            GPIO.output(LED_ARRAY_WATER_STATUS[led], GPIO.HIGH)

def read_sensor(input):
    bus.write_byte(0x4b, ADS_COMMANDS[input])
    return bus.read_byte(0x4b)


def output_sensor_data(value, status, analog_input):
    global is_dry_counter

    console_and_log(f"Sensor: {analog_input+1}\t{status}\t\t({value})\t\t[count: {is_dry_counter}]")
    #console_and_log(f"{status}")


def determine_soil_status(value, analog_input):
    global is_dry_counter

    if value >= DRY_VALUE:
        is_dry_counter = is_dry_counter + 1
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.HIGH)
        return "Dry: No Soil"
    
    elif value >= DRY_SOIL_VALUE:
        is_dry_counter = is_dry_counter + 1
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.HIGH)
        return "Dry Soil    "
    
    elif value >= MOIST_SOIL_VALUE:
        is_dry_counter = 0
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.LOW)
        return "Moist Soil  "
    
    elif value >= WET_SOIL_VALUE:
        is_dry_counter = 0
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.LOW)
        return "Wet Soil    "
    
    elif value >= WATER_VALUE:
        is_dry_counter = 0
        GPIO.output(LED_ARRAY_WATER_STATUS[analog_input], GPIO.LOW)
        return "Water       "
    else:
        return "Low Value"
    
def check_water_status():
    global is_dry_counter

    if is_dry_counter >= DRY_COUNT_BEFORE_WATERING and WATER_IF_DRY:
        water_plant()
        
    

def water_plant():
    global is_dry_counter

    console_and_log("*****WATER DISPENSED*****")

    GPIO.output(BLUE_LED, GPIO.HIGH)

    sleep(3)

    GPIO.output(BLUE_LED, GPIO.LOW)

    is_dry_counter = 0


if __name__ == "__main__":
    try:
        setup_pins()
        os.system("clear")
        console_and_log(OPENING_MESSAGE)

        while True:
            for analog_input in range(NUMBER_OF_ANALOG_INPUTS):
                sensor_value = read_sensor(analog_input)

                soil_status = determine_soil_status(sensor_value, analog_input)
                
                output_sensor_data(sensor_value, soil_status, analog_input)

                check_water_status()

            sleep(DURATION_BETWEEN_CHECKS)

            if CLEAR_SCREEN_BEFORE_PRINT:
                os.system("clear")

    except Exception as e:
        console_and_log(f"An exception was caught in the main function: {e}\n\n\n")
        GPIO.cleanup()

    except KeyboardInterrupt:
        console_and_log(f"The program was terminated using Ctrl+C\n\n\n")
        GPIO.cleanup()