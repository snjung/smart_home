import serial
from time import sleep

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
    # Let's wait for 5 periodic signals by the boiler 
    for idx in range(5):
        while ser.waiting == 0:
            sleep(10E-3)
        serial_data = ser.readline()
        print(f"Waiting, received {idx+1}/5 messages")
        print(format_bytestring(f"Received:", serial_data))
    request = b''
    
    # The boiler expects to receive a telegram right after sending out its periodic signal
    # Accepted delay unknown, let's wait a brief moment:
    sleep(1E-3)

    message = "\x01"    # Confirm the periodic signal, needed for sending further commands
    ser.write(message)
    
    print("Requesting Vitodens ID")

    message = "\xF7\x55\x25\x02" # Command to Read (\xF7: normales Lesen) Adresse: \X55\X25 Expect two bytes of data
    ser.write(message)

    serial_data = ser.readline()
    print(format_bytestring("Received Response:", serial_data))
    print("Expected for e.g. V200KW2: 0x2098")
    
except KeyboardInterrupt:
    print("Program stopped by user.")
    ser.close()  # Close the serial port