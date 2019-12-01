"""OSC Interface for Wireworld"""
from pythonosc.udp_client import SimpleUDPClient
from .loader import OscConfig
from threading import Thread
from queue import Queue
class OSCSink(Thread):
    """Sender Thread to Sink messages"""
    def __init__(self, config:OscConfig):
        super().__init__()
        self.daemon = True
        self.sender = SimpleUDPClient(config.host, config.port)
        self.queue = Queue()
        self.addr = config.addr

    def send(self, sink, x, y, electrons):
        """Queue up a message to go"""
        self.queue.put_nowait([
            chr(sink), int(x), int(y), int(electrons)
        ])

    def run(self):
        while True:
            msg = self.queue.get()
            addr = self.addr + "/" + msg[0]
            self.sender.send_message(addr, msg[1:])

class PrintSender(Thread):
    """Sender Thread to Sink messages"""
    def __init__(self, config:OscConfig):
        super().__init__()
        self.daemon = True
        self.queue = Queue()

    def send(self, *args):
        """Queue up a message to go"""
        self.queue.put_nowait(args)

    def run(self):
        while True:
            msg = self.queue.get()
            print(msg)