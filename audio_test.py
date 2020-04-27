#!/usr/bin/env python
# -*- coding: utf-8 -*-

audio_path = '/home/pi/TelegramBot/maks_nezemnaja.mp3'

import subprocess

def play(audio_path):
    subprocess.call(['omxplayer',audio_path])
play(audio_path)
