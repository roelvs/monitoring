#warning: do not forget to install pyserial. (pip install pyserial)
#this code is based on various sources on the internet. 

import serial
import time
import sys

class TextMessage:
    def __init__(self, recipient="01234562313", message="TextMessage content not set."):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, stopbits=2,timeout=5,parity='N', rtscts=1)
        time.sleep(1)
        echo str(self.ser)

    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def disconnectPhone(self):
        self.ser.close()

if __name__ == '__main__':
    print "usage: python sms.py <number> <message>"
    print sys.argv[1]
    print sys.argv[2]
    sms=TextMessage(number,message)
    print "message sent"
