#!/usr/bin/python
import MySQLdb,sys,getopt # sudo apt-get install python-mysqldb
from termcolor import colored

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="password", # your password
                     db="seckc") # name of the data base
def banner():
  PrintInColor.green("#" * 30)
  PrintInColor.grey("     SecKC Banning Script")
  PrintInColor.green("#" * 30)

def writefile(target,data):
  print data
  target.write(data)
  target.write("\n")

def display(data):
  print "No output file selected, printing results"
  print data

def readDb(write=False,file=""):
  cur = db.cursor()  # Create Db cursor object. 
  cur.execute("SELECT macaddress from Banned")
  for row in cur.fetchall() :
    if write:
      writefile(file, row[0])
    else:
      display(row[0])

def main(argv):
  outputfile = ''
  banner()
  try:
    opts, args = getopt.getopt(argv,"ho:",["ofile="])
  except getopt.GetoptError:
    print 'getlist.py -o <outputfile>'
    sys.exit(2)
  if len(opts) > 0: 
    for opt, arg in opts:
      if opt == '-h':
        print 'getlist.py -o <outputfile>'
        sys.exit()
      elif opt in ("-o", "--ofile"):
        print '  [+] Writing to %s' % arg
        target = open(arg, 'w')
        readDb(True,target)
        target.close()
        print '  [+] Done.'
  else:
    readDb()

class PrintInColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'

    @classmethod
    def red(cls, s, **kwargs):
        print(cls.RED + s + cls.END, **kwargs)

    @classmethod
    def green(cls, s, **kwargs):
        print(cls.GREEN + s + cls.END, **kwargs)

    @classmethod
    def yellow(cls, s, **kwargs):
        print(cls.YELLOW + s + cls.END, **kwargs)

    @classmethod
    def lightPurple(cls, s, **kwargs):
        print(cls.LIGHT_PURPLE + s + cls.END, **kwargs)

    @classmethod
    def purple(cls, s, **kwargs):
        print(cls.PURPLE + s + cls.END, **kwargs)

if __name__ == "__main__":
   main(sys.argv[1:])
