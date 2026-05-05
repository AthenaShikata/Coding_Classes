import time
import board
import neopixel
# Imports required libraries needed to function

# Specifies the board, NeoPixel pins, and number of NeoPixels to access.
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True: #loop
    pixels.fill((0,0,0)) #sets all the NeoPixels blank
    pixels[0]=(255,0,255) #sets all selected NeoPixels purple
    pixels[2]=(255,0,255)
    pixels[4]=(255,0,255)
    pixels[6]=(255,0,255)
    pixels[8]=(255,0,255)
    time.sleep(1) #wait 1 second
    pixels.fill((0,0,0)) #sets all the NeoPixels blank
    pixels[1]=(0,200,0) #sets all selected NeoPixels green
    pixels[3]=(0,200,0)
    pixels[5]=(0,200,0)
    pixels[7]=(0,200,0)
    pixels[9]=(0,200,0)
    time.sleep(1) #wait 1 second