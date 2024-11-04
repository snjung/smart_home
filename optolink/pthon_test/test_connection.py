import serial


# Serial Protocol uses 8 E 2 at 4800 baud
# Even Parity
# 2 Stop-Bits 

# - Parity Bit is a simple failure-check-mechanism
# E (Even): Bit will be 1 if a even number of bits were transmitted before
# Can detect, if a bit (or any odd number of bits) was lost in transmission 
# (won't detect loss of any even number of bits)

com_port = 'COM4'
baudrate = 4800
parity = serial.PARITY_EVEN
stop_bits = serial.STOPBITS_TWO
timeout = 2     # timeout in seconds, let's give it plenty of time

ser = serial.Serial(port = com_port, baudrate = baudrate, parity = parity, stopbits = stop_bits, timeout = timeout)

def format_bytestring(text_before, data):
    """ Function to format a bytestring in a readable form used for debug-messages"""
    delimiter = "\\x"
    formated_string = f"{text_before} {delimiter}{delimiter.join('{:02x}'.format(x) for x in data)}"
    return(formated_string)

try:
    while True:
        if ser.in_waiting > 0:
            print("serial data available - reading ...")
            serial_data = ser.readline()
            serial_decoded = serial_data.decode('utf-8')
            print(f"Raw received: {serial_data} Decoded: {serial_decoded}")  # Print the received serial data
            print(format_bytestring("Formated Data:", serial_data))

except KeyboardInterrupt:
    print("Program stopped by user.")
    ser.close()  # Close the serial port