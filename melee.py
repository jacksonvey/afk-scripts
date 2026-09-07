# pip install pynput
import time
import threading
from pynput import keyboard

INTERVAL = 0.1  # 10 presses per second

k = keyboard.Controller()
running = threading.Event()
stop_all = threading.Event()

def spam_loop():
    while not stop_all.is_set():
        if running.is_set():
            k.press('v')
            k.release('v')
            time.sleep(INTERVAL)
        else:
            time.sleep(0.05)

def on_press(key):
    if key == keyboard.Key.f8:
        if running.is_set():
            running.clear()
            print("Stopped")
        else:
            running.set()
            print("Started")
    elif key == keyboard.Key.esc:
        stop_all.set()
        running.clear()
        print("Exiting")
        return False

t = threading.Thread(target=spam_loop, daemon=True)
t.start()

print("F8 = start/stop | ESC = quit")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
