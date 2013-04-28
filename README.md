UserAgent_Collector
===================
Description:
Script to collect UA from UserAgentString.com

Module requirements:
* BeautifulSoup
* httplib2

Script usage:
* $ sudo chmod a+x main.py
* $ sudo chmod a+x genereateReq.py
* $ python main.py http://www.useragentstring.com/pages/Chrome/

Now, script will generate multiple HTTP GET Requests based on the user agents collected
from UserAgentString.com for Google Chrome Browser.
