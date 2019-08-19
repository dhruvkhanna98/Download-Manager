import time
import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_to_track = '/Users/dhruvkhanna/Downloads'
folder_map = dict()

class DownloadHandler(FileSystemEventHandler): 
    def on_modified(self, event): 
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if "." not in filename: continue
            ext = filename.split(".")[-1]
            if ext not in folder_map: 
                try:
                    os.mkdir(folder_to_track + "/" + ext.upper())
                except FileExistsError:
                    print('Directory not created')
                    pass
                folder_map[ext] = ext.upper()
            new_destination = folder_to_track + "/" + folder_map[ext] + '/' + filename
            os.rename(src, new_destination)

event_handler = DownloadHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track)
observer.start()

try: 
    while True: 
        time.sleep(10)
except KeyboardInterrupt: 
    observer.stop()

observer.join()

