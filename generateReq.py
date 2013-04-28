#######################################################################################
##   Tiny program to craft custom HTTP Header along with feeded User-Agent strings.  ##
##   Script crawls the same host each time with a different user-agent string.       ##
##                                                                                   ##
##   Author  :   Sujit Ghosal                                                        ##
##   Email   :   x13.x37@gmail.com                                                   ##
##   Blog    :   http://wikisecure.net/                                              ##
#######################################################################################
import os, sys, time

txtFile = 'strings.txt'
host    = 'http://www.guimp.com/'

def readTxt():
    agents = []
    fileObj = open(txtFile)
    for eachAgent in fileObj:
        agents.insert(0, eachAgent)

    try:
        import httplib2
    except ImportError:
        print '[-] httplib2 library not found!'
        print '[-] Please install httplib2 module and try again.'
        sys.exit(0)

    for i in agents:
        # Define properties to make HTTP Queries for httplib2 object
        props = { 'Referer':            'http://google.co.in/', \
                  'Accept-Language':    'en-in', \
                  'Accept-Encoding':    'gzip, deflate', \
                  'User-Agent':          i, \
                  'Connection':         'Keep-Alive', \
                  'Host':               'guimp.com', \
                  'Cookie':             'remember=false' }

        time.sleep(2)
        http = httplib2.Http()

        try:
            print '[+] Processing User-Agent:', i,
            response, content = http.request(host, 'GET', headers=props)
        except httplib2.ServerNotFoundError:
            print '[+] Server unreachable.'
            print '[+] Please check if the target host is up.'
            sys.exit(0)
        except:
            print '[+] Unknown exception caught!'
            print '[+] Program terminated.'
            sys.exit(0)

    print '[+] Voilla, crawling completed for all the user agents.'
    print '[+] Program completed all its operations gracefully.'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        readTxt()
    else:
        print '[+] ERROR: Invalid number of arguments passed.'
        print '[+] Usage: $python useragent.py <strings.txt>'
        sys.exit(0)
