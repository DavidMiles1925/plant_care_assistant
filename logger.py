from datetime import datetime
import os
from config import LOG_DIRECTORY_PATH, CONSOLE_OUTPUT_ON, LOGGING_ENABLED

def write_to_log(message):
    datestamp = datetime.now().strftime("%m.%d.%y")
    timestamp = datetime.now().strftime("%H.%M.%S")

    fname = f"{datestamp}_log.txt"

    path_str = f"{LOG_DIRECTORY_PATH}"

    if os.path.exists(path_str) == False:
        os.mkdir(path_str)

    os.chdir(path_str)
    if os.path.exists(fname):
        fout = open(fname, 'a')
        fout.write(f"{timestamp}:   ")
        fout.write(f"{message}\n\n")
    else:
        fout = open(fname, 'w')
        fout.write(f"{timestamp}:   ")
        fout.write(f"{message}\n\n")

    fout.close()


def console_and_log(message=""):
    if CONSOLE_OUTPUT_ON:
        print(message)

    if LOGGING_ENABLED:
        write_to_log(message)