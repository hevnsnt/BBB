#!/usr/bin/python
import MySQLdb,sys,os,getopt # sudo apt-get install python-mysqldb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="password", # your password
                     db="seckc") # name of the data base
def banner():
  print ("#" * 30)
  print ("     SecKC Banning Script")
  print ("#" * 30)

def writefile(target,data):
  print("    [-]" + data)
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

def instructions(arg):
  length = int(len(str(os.path.abspath(arg))))
  print("#" * (length + 30))
  print("## Instructions for use:" + " " * (length + 8) + "##")
  print("## edit /etc/hostapd/hostapd.conf to:" + " " * 11 + "##" )
  print("## deny_mac_file=%s") % os.path.abspath(arg)
  print("#" * 50)
  print


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
        print
        instructions(arg)
        
  else:
    readDb()

if __name__ == "__main__":
   main(sys.argv[1:])
