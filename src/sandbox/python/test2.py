from ampy.pyboard import Pyboard

from ampy.files import Files

print("test")
pyb = Pyboard('/dev/tty.SLAB_USBtoUART')
f = Files(pyb)
print(f.ls())
