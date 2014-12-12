#warning: do not forget to install pyserial. (pip install pyserial)
#this code is based on various sources on the internet. 

import serial
import time

class TextMessage:
    def __init__(self, recipient="01234562313", message="TextMessage.content not set."):
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

print "test"
sms= TextMessage("043423422","test")
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()
print "einde"
