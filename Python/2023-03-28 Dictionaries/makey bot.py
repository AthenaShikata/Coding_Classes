makey_bot = {
'wave_pattern':[30,5,150,2,90,1],
'eyes_rgb_status':1,
'rgb_eye_color_1':0xff0000,
'rgb_eye_color_2':0x00a5ff,
'7seg_value':5,
'led_1_status':1,
'led_1_blink':1,
'led_2_status':1,
'led_2_blink':2,
'led_3_status':1,
'led_3_blink':3
}

print(makey_bot)

while True :
    key = input('Enter a key: (blank to quit) ')
    if key == '':
        break

    if key in makey_bot:
        print(str(makey_bot[key]) + ' is the value of ' + key)
    else:
        print('I do not have value information for ' + key)
        value = input('What is their value? ')
        makey_bot[key] = value
        print('MakeyBot updated.')