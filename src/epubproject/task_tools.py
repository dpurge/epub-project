import shutil
from pathlib import Path
import uuid


def create_directories(*directories):
    
    for directory in directories:
        d = Path(directory)
        if (not d.exists()):
            print(
                "Creating directory: {directory}".format(
                    directory = directory))
            try:  
                d.mkdir(parents = True, exist_ok = True)
            except OSError:  
                print(
                    "Cannot create directory: {directory}".format(
                        directory = directory))


def delete_directories(*directories):
        
    for directory in directories:
        d = Path(directory)
        if (d.exists()):
            print(
                "Deleting directory: {directory}".format(
                    directory = directory))
            shutil.rmtree(d)


def sequence():
    x = 0
    while True:
        x += 1
        yield x


def uid_for_path(path):
    return uuid.uuid5(uuid.NAMESPACE_DNS, path).hex