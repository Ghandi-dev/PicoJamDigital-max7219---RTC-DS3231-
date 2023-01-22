import time
import max7219
from my_lib import RTC_DS3231
from machine import Pin, SPI
from time import sleep
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

def conver(tup):
    str = ''.join(tup)
    return str

rtc = RTC_DS3231.RTC()
display = max7219.Matrix8x8(spi, ss, 4)
display.brightness(1)   # adjust brightness 1 to 15
display.fill(0)
display.show()
sleep(0.5)

while True:
    display.fill(0)
    data = rtc.DS3231_ReadTime(0)
    detik = data[0]
    menit = data[1]
    jam = data[2]
    display.pixel(15,4,0)
    display.pixel(16,3,0)
#     print(detik)
    msg = f"{jam}{menit}"
    display.text(msg,0,0,1)
    display.show()
    time.sleep_ms(500)
    display.pixel(15,4,1)
    display.pixel(16,3,1)
    display.show()
    time.sleep_ms(500)
    if(detik == "00"):
        msg = rtc.DS3231_ReadTime(1)
        length = len(msg)
        length = (length*8)
        for x in range(32, -length, -1):
            display.text(msg ,x,0,1)
            display.show()
            sleep(0.10)
            display.fill(0)
        
    




