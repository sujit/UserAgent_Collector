#######################################################################################
##   Tiny program to parse useragentstring.com website and export all the user       ##
##   agents for the given web browser.                                               ##
##   Script crawls the same host each time with a different user-agent string.       ##
##                                                                                   ##
##   Author  :   Sujit Ghosal                                                        ##
##   Email   :   x13.x37@gmail.com                                                   ##
##   Blog    :   http://wikisecure.net                                               ##
#######################################################################################
try:
    from BeautifulSoup import BeautifulSoup
    from urllib import urlopen
    import os, re, string, sys, time
except ImportError:
    print '[+] Required modules not found.'
    print '[+] Please install all the required modules and try again.'

print '\n[+] Python libraries check passed.'
try:
    url = sys.argv[1]
except IndexError:
    print '[+] ERROR: Invalid number of arguments passed.'
    print '[+] Usage: python <main.py> <target_host> <return>'
    sys.exit(0)

def crawl():
    try:
        time.sleep(2)
        print '[+] Retrieving webpage contents.'
        buf = urlopen(url).read()
        print '[+] Analysing retrieved webpage contents.'
        soupObj = BeautifulSoup(buf)
    except IOError:
        print '[+] Error while fetching the contents of the host:', url
        print '[+] Please make sure the target website is running!'
        sys.exit(0)

    uaStrings = []
    print '[+] Processing the appropriate attribute values for parsing.'
    tags = soupObj.findAll('li') # fetch the values from li tag

    for eachStr in tags:
        filters = str(eachStr)
        filters = re.findall('\<li\>\<a\ href=\"\/.*\"\>(.+)\<\/a\>\<\/li\>', filters)
        uaStrings.insert(0, filters)

    uaStrings = '\n'.join(sum(uaStrings, []))
    fObj = open('strings.txt', 'w')
    for eachLine in uaStrings:
        fObj.writelines(eachLine)

    fObj.close()
    print '[+] User-Agent strings output exported to strings.txt'
    print '[+] Now running HTTP request generator...\n'
    time.sleep(3)
    print os.system('python generateReq.py strings.txt')

if __name__ == '__main__':
    crawl()
