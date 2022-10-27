import time
import struct

try:
    f = open(r'\\.\pipe\testing', 'r+b', 0)
    while True:
        n = struct.unpack('I', f.read(4))[0]  # Read str length
        s = f.read(n).decode('ascii')  # Read str
        f.seek(0)
        print('Read:', s)
        time.sleep(3)
        words = s.split(',')
        print("_________________________")
        with open(r'C:\Users\H261112\source\repos\pyout\subbu.txt', 'w') as files:
            files.write(words[0]+" "+words[1]+" "+words[2])
        print("___________________________")
        s = "Completed- " + s
        f.write(struct.pack('I', len(s)) + s.encode('ascii'))  # Write str length and str
        f.seek(0)
        print('Wrote:', s)
except FileNotFoundError:
    raise

