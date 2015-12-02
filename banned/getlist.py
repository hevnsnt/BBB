#!/usr/bin/python
import MySQLdb,sys,getopt # sudo apt-get install python-mysqldb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="password", # your password
                     db="seckc") # name of the data base
def banner():
  print "#" * 30
  print "     SecKC Banning Script"
  print "#" * 30


def readDb(write=False,file=""):
        # Create a Cursor object. It will let
        cur = db.cursor()

        # Use all the SQL you like
        cur.execute("SELECT macaddress from Banned")
        if not write:
                print "No output file selected, printing results"
                banner()
        # print all the first cell of all the rows
        for row in cur.fetchall() :
          if not write:
            print row[0]
          else:
            print "Writing to %s" % file
            target = open(filename, 'w')
            target.write(row[0])
            target.write("\n")
        if file != "" : target.close()


def main(argv):
  outputfile = ''
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
        readDb(True,arg)
  else:
    readDb()


if __name__ == "__main__":
   main(sys.argv[1:])
