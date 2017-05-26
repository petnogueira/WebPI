#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.005

#File with text
FILE_PATH = '../_model/display.txt'

def main():
  lcd_init()

  resp_old = ""
  while True:
    f = open(FILE_PATH, 'r+')
    resp = f.read()
    if (resp != resp_old):
        resp_old = resp
        wmsg(resp)
    f.close()

def wmsg(msg):
  #Clear LCD and send cursor to home
  lcd_byte(0x01,LCD_CMD)
  # Send some centred test
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string(msg,1)
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("Line 2",1)
 
def lcd_init():
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)

def lcd_string(message,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified

  if style==1:
    message = message.ljust(LCD_WIDTH," ")  
  elif style==2:
    message = message.center(LCD_WIDTH," ")
  elif style==3:
    message = message.rjust(LCD_WIDTH," ")

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def toggle_enable_pin()
  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY) 

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  GPIO.output(LCD_D4, bits&0x10==0x10)
  GPIO.output(LCD_D5, bits&0x20==0x20)
  GPIO.output(LCD_D6, bits&0x40==0x40)
  GPIO.output(LCD_D7, bits&0x80==0x80)

  toggle_enable_pin()

  GPIO.output(LCD_D4, bits&0x01==0x10)
  GPIO.output(LCD_D5, bits&0x02==0x20)
  GPIO.output(LCD_D6, bits&0x04==0x40)
  GPIO.output(LCD_D7, bits&0x08==0x80)

  toggle_enable_pin()

if __name__ == '__main__':
  main()
