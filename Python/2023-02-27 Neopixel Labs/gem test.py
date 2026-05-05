import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

pixels.fill((0,0,0))
while True: 
    pixels[0]=(80,246,253) #sets light blue (diamond)
    pixels[1]=(80,246,253)
    pixels[2]=(80,246,253)
    pixels[3]=(80,246,253)
    pixels[4]=(80,246,253)
    pixels[5]=(80,246,253)
    pixels[6]=(80,246,253)
    pixels[7]=(80,246,253)
    pixels[8]=(80,246,253)
    pixels[9]=(80,246,253)