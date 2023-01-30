from pynput.keyboard import *
import logging

logging.basicConfig(filename="keyboard_log.txt", level=logging.DEBUG, format="%(asctime)s: %(key)s")

def press_on(key):
    print('Press ON: {}'.format(key))


def press_off(key):
    print('Press OFF: {}'.format(key))
    if key == Key.esc:
        return False


with Listener(on_press=press_on, on_release=press_off) as listener:
    listener.join()
