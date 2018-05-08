import os,sys; sys.path.insert(0, os.path.abspath('..'))
from binascii import hexlify
import click

class CSRNG:
    def __init__(self,length):
        self.length=length

    def hex_osrandom(self):
        return hexlify(os.urandom(self.length)).decode()[self.length:]