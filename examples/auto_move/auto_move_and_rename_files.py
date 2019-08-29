#!/usr/bin/python3
# -*- coding: utf-8 -*-

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
                
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)
            
folder_to_track = "/Users/oguzhan/Desktop/folder_to_track"
folder_destination = "/Users/oguzhan/Desktop/folder_destination"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
print("Waiting Keyboard Interrupt")

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Stopping...")
    observer.stop()
observer.join()