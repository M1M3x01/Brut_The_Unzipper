
import optparse
import zipfile
from threading import Thread

def extract_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print "Here is your password:" + password + '\n'
    except:
        pass

def main():
    parser = optparse.OptionParser("ZipFile Password Cracker with Brute-Force Attack"'\n''\n' +"Example Script:- python brut_the_unzipper.py -f <locked.zip> -p <password.txt> ")
    parser.add_option('-f', dest='zname', type='string',\
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',\
                      help='specify dictionary file')
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()


