
import RPi.GPIO as GPIO
import threading
from datetime import datetime
from time import sleep
from config import LIGHT_DURATION, LIGHT_LOG_MESSAGE, LIGHT_RELAY_PIN, LIGHT_START_TIME
from logger import light_log


light_is_on = False


def check_if_light_toggle_is_needed():
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == LIGHT_START_TIME and light_is_on == False:
        toggle_light(True)
        start_a_timer(LIGHT_DURATION)

def countdown_timer_to_turn_off_light(seconds):
    while seconds > 0:
        sleep(1)
        seconds = seconds - 1

    toggle_light(False)


def setup_pins():
        # Board Mode: BCM
        GPIO.setmode(GPIO.BCM)

        # Disable Warnings
        GPIO.setwarnings(False)

        GPIO.setup(LIGHT_RELAY_PIN, GPIO.OUT)
        GPIO.output(LIGHT_RELAY_PIN, GPIO.LOW)   


def start_a_timer(seconds):
    timer_thread = threading.Thread(target=countdown_timer_to_turn_off_light, args=(seconds,))
    timer_thread.daemon = True      # This is set to True so that the timer runs in the background.
    timer_thread.start()


def toggle_light(value):
    global light_is_on

    if value:
        light_log("Light ON")
        GPIO.output(LIGHT_RELAY_PIN, GPIO.HIGH)
        light_is_on = True

    else:
        light_log("Light OFF")
        GPIO.output(LIGHT_RELAY_PIN, GPIO.LOW)
        light_is_on = False



if __name__ == "__main__":
    try:
        setup_pins()
        print(LIGHT_LOG_MESSAGE)
        light_log(LIGHT_LOG_MESSAGE)

        while True:
            check_if_light_toggle_is_needed()

    except Exception as e:
        print(e)
        light_log(e)

    except KeyboardInterrupt:
        light_log("The light Program was closed using Ctrl+C")