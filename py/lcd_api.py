#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_EN = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

#File with text
FILE_PATH = '../_model/display.txt'

# Commands
LCD_CLEARDISPLAY        = 0x01
LCD_RETURNHOME          = 0x02
LCD_ENTRYMODESET        = 0x04
LCD_DISPLAYCONTROL      = 0x08
LCD_CURSORSHIFT         = 0x10
LCD_FUNCTIONSET         = 0x20
LCD_SETCGRAMADDR        = 0x40
LCD_SETDDRAMADDR        = 0x80

# Entry flags
LCD_ENTRYRIGHT          = 0x00
LCD_ENTRYLEFT           = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

LCD_ROW_OFFSETS = (0x00, 0x40, 0x14, 0x54) # Offset for up to 4 rows.

# Function set flags
LCD_8BITMODE            = 0x10
LCD_4BITMODE            = 0x00
LCD_2LINE               = 0x08
LCD_1LINE               = 0x00
LCD_5x10DOTS            = 0x04
LCD_5x8DOTS             = 0x00

# Control flags
LCD_DISPLAYON           = 0x04
LCD_DISPLAYOFF          = 0x00
LCD_CURSORON            = 0x02
LCD_CURSOROFF           = 0x00
LCD_BLINKON             = 0x01
LCD_BLINKOFF            = 0x00

# Move flags
LCD_DISPLAYMOVE         = 0x08
LCD_CURSORMOVE          = 0x00
LCD_MOVERIGHT           = 0x04
LCD_MOVELEFT            = 0x00

LINES = 2
COLS = 16

def main():
  lcd_init()

  resp_old = ""
  while True:
    f = open(FILE_PATH, 'r+')
    resp = f.read()
    if (resp != resp_old):
        resp_old = resp
        clear()
        message(resp)
    f.close()

def delay_microseconds(microseconds):
    # Busy wait in loop because delays are generally very short (few microseconds).
    end = time.time() + (microseconds/1000000.0)
    while time.time() < end:
        pass

def lcd_init():
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  for pin in (LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7):
    GPIO.setup(pin, GPIO.OUT)

  # Initialize the display.
  write_data(0x33)
  write_data(0x32)

  # Initialize display control, function, and mode registers.
  displaycontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF
  displayfunction = LCD_4BITMODE | LCD_1LINE | LCD_2LINE | LCD_5x8DOTS
  displaymode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT
  # Write registers.
  write_data(LCD_DISPLAYCONTROL | displaycontrol)
  write_data(LCD_FUNCTIONSET    | displayfunction)
  write_data(LCD_ENTRYMODESET   | displaymode)  # set the entry mode

  clear()


def home():
  """Move the cursor back to its home (first line and first column)."""
  write_data(LCD_RETURNHOME)  # set cursor position to zero
  delay_microseconds(3000)  # this command takes a long time!

def clear():
  """Clear the LCD."""
  write_data(LCD_CLEARDISPLAY)  # command to clear display
  delay_microseconds(3000)  # 3000 microsecond sleep, clearing the display takes a long time

def set_cursor(col, row):
  """Move the cursor to an explicit column and row position."""
  # Clamp row to the last row of the display.
  if row > LINES:
      row = LINES - 1
  # Set location.
  write_data(LCD_SETDDRAMADDR | (col + LCD_ROW_OFFSETS[row]))

def message(text):
  """Write text to display.  Note that text can include newlines."""
  line = 0
  # Iterate through each character.
  for char in text:
    # Advance to next line if character is a new line.
    if char == '\n':
      line += 1
      # Move to left or right side depending on text direction.
      col = 0 if displaymode & LCD_ENTRYLEFT > 0 else COLS-1
      set_cursor(col, line)
    # Write the character to the display.
    else:
      write_data(ord(char), True)

def pulse_enable():
  # Pulse the clock enable line off, on, off to send command.
  GPIO.output(LCD_EN, False)
  delay_microseconds(1)       # 1 microsecond pause - enable pulse must be > 450ns
  GPIO.output(LCD_EN, True)
  delay_microseconds(1)       # 1 microsecond pause - enable pulse must be > 450ns
  GPIO.output(LCD_EN, False)
  delay_microseconds(1)       # commands need > 37us to settle

def is_bit_set(value, n):
  return ((value >> n) & 1) > 0

def write_data(value, char_mode=False):
  """Write 8-bit value in character or data mode.  Value should be an int
  value from 0-255, and char_mode is True if character data or False if
  non-character data (default).
  """
  # One millisecond delay to prevent writing too quickly.
  delay_microseconds(1000)
  # Set character / data bit.
  GPIO.output(LCD_RS, char_mode)
  # Write upper 4 bits.
  GPIO.output(LCD_D4, is_bit_set(value, 4))
  GPIO.output(LCD_D5, is_bit_set(value, 5))
  GPIO.output(LCD_D6, is_bit_set(value, 6))
  GPIO.output(LCD_D7, is_bit_set(value, 7))

  pulse_enable()
  # Write lower 4 bits.
  GPIO.output(LCD_D4, is_bit_set(value, 0))
  GPIO.output(LCD_D5, is_bit_set(value, 1))
  GPIO.output(LCD_D6, is_bit_set(value, 2))
  GPIO.output(LCD_D7, is_bit_set(value, 3))

  pulse_enable()

if __name__ == '__main__':
  main()