#!/usr/bin/env python3
import os
import subprocess
import platform
import ctypes

# ---------------------- #

ngrok = ''

# Determine OS type more robustly
_system = platform.system().lower()
if _system == "linux":
    osType = "Linux"
elif _system == "windows":
    osType = "Windows"
else:
    osType = "Other"

def payload():
    if ostype == "Windows":
        
    if ostype == "Linux"

    else:
        print("Error. Run this on a linux or windows based system.")