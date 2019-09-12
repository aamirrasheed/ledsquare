#!/bin/bash
cd ledsquare
git pull
sudo ./rpi-rgb-led-matrix/utils/led-image-viewer --led-rows=64 --led-cols=64 --led-brightness=20 --led-pwm-lsb-nanoseconds=50 --led-pixel-mapper=Rotate:-90 -f -w1 finaldisplay/frame_1* finaldisplay/frame_2*
