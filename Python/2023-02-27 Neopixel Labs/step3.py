# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import neopixel


# Calls the circuit Python neopixel library, specifies the default board
# pins for the Neopixels, and the number of neopixels to access.  Returns a
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 3)


while True:
    # indexes the first element of the 'pixels' list and points to the
    # first 3 Neopixels in the 'pixels' list
    pixels[0]=(255, 0, 0)
    pixels[1]=(0, 255, 0)
    pixels[2]=(0, 0, 255)
    time.sleep(0.5) #delay equivalent
    pixels.fill((0, 0, 0)) #writes the Neopixels to off
    time.sleep(0.5)