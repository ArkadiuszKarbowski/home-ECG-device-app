import serial
import serial.tools.list_ports
import queue


class EkgReader:
    def __init__(self, ekg_app, baudrate=115200):
        self.baudrate = baudrate
        self.port = self.find_port()
        self.serial = serial.Serial(self.port, baudrate)
        self.q = ekg_app.q  
        
    def read(self):
        while True:
            data = self.serial.readline()
            data = data.decode().strip()
            self.q.put(int(data))
            

    def find_port(self):
        ports = list(serial.tools.list_ports.comports())
        if len(ports) == 0:
            raise ValueError("Nie znaleziono żadnego portu szeregowego.")
        elif len(ports) > 1:
            print("Wykryto więcej niż jeden port szeregowy. Wybierz numer portu:")
            for i, port in enumerate(ports):
                print(f"{i+1}: {port}")
            selection = input("> ")
            try:
                selection = int(selection)
                if selection < 1 or selection > len(ports):
                    raise ValueError
                port = str(ports[selection-1].device)
            except:
                print("Nieprawidłowy wybór. Używam pierwszego portu.")
                port = str(ports[0].device)
        else:
            port = str(ports[0].device)
        print(f"Wybrano port szeregowy {port}.")
        return port
