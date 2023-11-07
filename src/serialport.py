import serial


class SerialPort(object):
    def __init__(self) -> None:
        self.serial = None

    def open(self, port, baudrate, databit, checkbit, stopbit, xonxoff, rtscts, dsrdtr) -> bool:
        if self.serial is None:
            try:
                self.serial = serial.Serial(port, baudrate, databit, checkbit, stopbit, 0.01, xonxoff, rtscts, 0, dsrdtr)
            except Exception as e:
                print(e)
                return False
            self.oneByteInter = (databit + 2 + (0 if checkbit == "N" else 1)) / baudrate
            return True

    def close(self) -> bool:
        if self.serial is not None:
                self.serial.reset_output_buffer()
                self.serial.reset_input_buffer()
                self.serial.flush()
                self.serial.close()
                self.serial = None
                return True
        return False


    def isOpen(self) -> bool:
        if self.serial is None:
            return False
        else:
            return True

    def write(self, data: bytes) -> None:
        if self.serial is not None:
            self.serial.write(data)

    def read(self) -> bytes:
        if self.serial is not None:
            num = max(1, self.serial.inWaiting())
            return self.serial.read(num)
        return bytes()
