import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
 
 
SOURCE_DIR = 'C:/Users/LENOVO/Downloads'
DEST_DIR = 'F:/Copy Data'
TEXT_DIR = os.path.join(DEST_DIR, 'TextFiles')
IMAGE_DIR = os.path.join(DEST_DIR, 'Images')

os.makedirs(TEXT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        _, ext = os.path.splitext(file_path)
        if ext in ['.txt']:
            self.move_file(file_path, TEXT_DIR)
        elif ext in ['.jpg', '.png', '.jpeg']:
            self.move_file(file_path, IMAGE_DIR)

    def move_file(self, src_path, dest_dir):
        file_name = os.path.basename(src_path)
        dest_path = os.path.join(dest_dir, file_name)
        os.rename(src_path, dest_path)
        print(f'Moved: {src_path} to {dest_path}')

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, SOURCE_DIR, recursive=False)

observer.start()
print(f'Running {SOURCE_DIR}...')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
