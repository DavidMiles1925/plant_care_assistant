
import os
import RPi.GPIO as GPIO
import threading
from smbus import SMBus
from datetime import datetime
from time import sleep

from config import ADS_COMMANDS, \
            CLEAR_SCREEN_BEFORE_PRINT, \
            DRY_COUNT_BEFORE_WATERING, \
            DURATION_BETWEEN_CHECKS, \
            DRY_SOIL_VALUE, \
            DRY_VALUE, \
            LED_ARRAY_WATER_STATUS, \
            LIGHT_DURATION, \
            LIGHT_RELAY_PIN, \
            LIGHT_START_TIME,\
            MOIST_SOIL_VALUE, \
            NUMBER_OF_ANALOG_INPUTS, \
            OPENING_MESSAGE, \
            WET_SOIL_VALUE, \
            WATER_VALUE, \
            WATER_IF_DRY
            
from logger import console_and_log

# Bus
bus = SMBus(1)

# List that will be used to keep track of 
is_dry_list = []

light_is_on = False

def check_if_light_toggle_is_needed():
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == LIGHT_START_TIME and light_is_on == False:
        toggle_light(True)
        start_a_timer(LIGHT_DURATION)
        


def check_if_water_is_needed(analog_input):
    global is_dry_list

    if is_dry_list[analog_input] >= DRY_COUNT_BEFORE_WATERING and WATER_IF_DRY:
        water_plant(analog_input)


def countdown_timer_to_turn_off_light(seconds):
    while seconds > 0:
        sleep(1)
        seconds = seconds - 1

    toggle_light(False)


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
    bus.write_byte(0x4b, ADS_COMMANDS[input])
    return bus.read_byte(0x4b)


def setup_pins():
    # Board Mode: BCM
        GPIO.setmode(GPIO.BCM)

        # Disable Warnings
        GPIO.setwarnings(False)

        for led in range(len(LED_ARRAY_WATER_STATUS)):
            GPIO.setup(LED_ARRAY_WATER_STATUS[led], GPIO.OUT)
            GPIO.output(LED_ARRAY_WATER_STATUS[led], GPIO.HIGH)

        GPIO.setup(LIGHT_RELAY_PIN, GPIO.OUT)
        GPIO.output(LIGHT_RELAY_PIN, GPIO.LOW)        


def start_a_timer(seconds):
    timer_thread = threading.Thread(target=countdown_timer_to_turn_off_light, args=(seconds,))
    timer_thread.daemon = True      # This is set to True so that the timer runs in the background.
    timer_thread.start()


def toggle_light(value):
    global light_is_on

    if value:
        console_and_log("********** LIGHT TURNED ON **********")
        GPIO.output(LIGHT_RELAY_PIN, GPIO.HIGH)
        light_is_on = True

    else:
        console_and_log("********** LIGHT TURNED OFF **********")
        GPIO.output(LIGHT_RELAY_PIN, GPIO.LOW)
        light_is_on = False


def water_plant(analog_input):
    global is_dry_list

    console_and_log(f"*****WATER DISPENSED: Sensor {analog_input + 1}*****")

    sleep(3)

    is_dry_list[analog_input] = 0


if __name__ == "__main__":
    try:
        setup_pins()
        os.system("clear")
        console_and_log(OPENING_MESSAGE)

        for input_counter in range(NUMBER_OF_ANALOG_INPUTS):
            is_dry_list.append(1)

        while True:
            for analog_input in range(NUMBER_OF_ANALOG_INPUTS):
                sensor_value = read_sensor(analog_input)

                soil_status = determine_soil_moisture(sensor_value, analog_input)
                
                output_sensor_data(sensor_value, soil_status, analog_input)

                check_if_water_is_needed(analog_input)

                check_if_light_toggle_is_needed()

            sleep(DURATION_BETWEEN_CHECKS)

            if CLEAR_SCREEN_BEFORE_PRINT:
                os.system("clear")

    except Exception as e:
        console_and_log(f"An exception was caught in the main function: {e}\n\n\n")
        GPIO.cleanup()

    except KeyboardInterrupt:
        console_and_log(f"The program was terminated using Ctrl+C\n\n\n")
        GPIO.cleanup()