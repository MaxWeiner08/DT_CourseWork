import serial.tools.list_ports

def find_pico_port():
    print("Listing all serial devices: ")
    ports = serial.tools.list_ports.comports()
    data = (None, None)
    for port in ports:
        if not port.vid:
            continue
        print(port)
        if (port.vid, port.pid) == (0x2E8A, 0x0005):
            data = (port.device, port.description)
    
    return data

if __name__ == "__main__":
    port, description = find_pico_port()
    print("\n") 
    if port:
        print(f"Rpi Pico detected on {port} ({description}), Please copy and run following")
        print(f"export AMPY_PORT={port}")
    else:
        print("No Raspberry Pi Pico detected")
