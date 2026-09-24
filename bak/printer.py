import socket

class Printer:
    def __init__(self, host: str, port: int = 9100, timeout: int = 5):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.connection = None
        self.data = ""

    def connect(self):
        self.connection = socket.create_connection(
            (self.host, self.port),
            timeout=self.timeout)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
        else:
            print("Warning: No active connection to disconnect.")

    # append line / command
    def send(self, line):
        self.data += line

    def print(self):
        if not self.connection:
            raise RuntimeError("Printer is not connected")

        self.connection.sendall(self.data.encode("cp437"))
        # maybe add storing print history
        self.data = "" # clear data object - check this clears global object

    def print_image(data):
            self.connection.sendall(self.data)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.disconnect()


    