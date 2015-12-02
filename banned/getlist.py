#!/usr/bin/python
import MySQLdb,sys,getopt
write=False
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="password", # your password
                     db="seckc") # name of the data base

def readDb():
        # Create a Cursor object. It will let
        cur = db.cursor()

        # Use all the SQL you like
        cur.execute("SELECT macaddress from Banned")
        if not write:
                print "No output file selected, printing results"
        # print all the first cell of all the rows
        for row in cur.fetchall() :
                if not write:
                        print row[0]
                else:
                        print row[0]

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"ho:",["ofile="])
   except getopt.GetoptError:
      print 'test.py -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -o <outputfile>'
         sys.exit()
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   readDb()


if __name__ == "__main__":
   main(sys.argv[1:])
