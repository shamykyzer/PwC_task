from pynput.keyboard import *
from pynput.mouse import *
import time
import pyautogui
import logging


logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")


def press_on(key):
    print('Press ON: {}'.format(key))


def press_off(key):
    print('Press OFF: {}'.format(key))
    if key == Key.esc:
        return False


def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        logging.info("Mouse clicked to ({0}, {1} with {2})".format(x, y, button, pressed))


def on_scroll(x, y, dx, dy):
    logging.info("Mouse clicked to ({0}, {1} with {2})".format(x, y, dx, dy))


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll, on_press=press_on,
              on_release=press_off) as listener:
    listener.join()