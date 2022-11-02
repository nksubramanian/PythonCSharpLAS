import time
import struct
import pandas as pd
import lasio as lasio



class LASProcessor:
  def __init__(self, file):
    print("file "+ file )
    self.file = file

  def Getprocessor(self, operation):
      return {
          'Well': LASProcessor.OutputWells,
          'Data': LASProcessor.OutputData,
          'Curves': LASProcessor.OutputCurves,
          'Keys': LASProcessor.OutputKeys,
          'Version': LASProcessor.OutputVersion,
          "Statistics":LASProcessor.OutputStatistics,
      }.get(operation, LASProcessor.OutputWells)
  def process(self, operation,outputfile):
      process1 = self.Getprocessor(operation)
      process1(self, outputfile)
  def OutputWells(self, outputfile):
      print("I am here")
      with open(self.file, 'r') as LASfile:
          las = lasio.read(LASfile.read())
      with open(outputfile, 'w') as file:
          file.write(str(las.well))
  def OutputData(self,outputfile):
      with open(self.file, 'r') as LASfile:
          las = lasio.read(LASfile.read())
          pd.set_option('display.max_rows', None)
          pd.set_option('display.max_columns', None)
          pd.set_option('display.width', None)
          pd.set_option('display.max_colwidth', None)
          df = las.df()
      with open(outputfile, 'w') as file:
          file.write(str(df))
  def OutputCurves(self,outputfile):
      with open(self.file, 'r') as LASfile:
          las = lasio.read(LASfile.read())
      with open(outputfile, 'w') as file:
          file.write(str(las.curves))
  def OutputKeys(self,outputfile):
      with open(self.file, 'r') as LASfile:
          las = lasio.read(LASfile.read())
      with open(outputfile, 'w') as file:
          file.write(str(las.keys()))
  def OutputVersion(self, outputfile):
      with open(self.file, 'r') as LASfile:
          las = lasio.read(LASfile.read())
      with open(outputfile, 'w') as file:
          file.write(str(las.version))

  def OutputStatistics(self, outputfile):
      with open(self.file, 'r') as LASfile:
          las = lasio.read(LASfile.read())
          pd.set_option('display.max_rows', None)
          pd.set_option('display.max_columns', None)
          pd.set_option('display.width', None)
          pd.set_option('display.max_colwidth', None)
      with open(outputfile, 'w') as file:
          df = las.df()
          file.write(str(df.describe()))



try:
    f = open(r'\\.\pipe\testing', 'r+b', 0)
    while True:
        n = struct.unpack('I', f.read(4))[0]  # Read str length
        s = f.read(n).decode('ascii')  # Read str
        f.seek(0)
        print('Read:', s)
        #time.sleep(3)
        words = s.split(',')
        print("_________________________")
        #with open(r'C:\Users\H261112\source\repos\pyout\subbu.txt', 'w') as files:
        #    files.write(words[0]+" "+words[1]+" "+words[2])
        print("___________________________")
        LASfile = words[0]
        OpToBeDone = words[0]
        OutputFile = words[2]

        lasprocessor = LASProcessor(LASfile)
        lasprocessor.process(OpToBeDone, OutputFile)

        s = "Completed- " + s
        f.write(struct.pack('I', len(s)) + s.encode('ascii'))  # Write str length and str
        f.seek(0)
        print('Wrote:', s)
except FileNotFoundError:
    raise

