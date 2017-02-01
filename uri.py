"""
In Python, write a class or module with a bunch of functions for manipulating a URI.
For this exercise, pretend that the urllib, urllib2, and urlparse modules don't exist.
You can use other standard Python modules, such as re, for this. The focus of the class or module
you write should be around usage on the web, so you'll want to have things that make it easier to
update or append a querystring var, get the scheme for a URI, etc., and you may want to include ways
to figure out the domain for a URL (british-site.co.uk, us-site.com, mailto: yourname@example.com, etc)

We're looking for correctness (you'll probably want to read the relevant RFCs; make sure you handle
edge cases), and elegance of your API (does it let you do the things you commonly want to do with URIs
in a really straightforward way?,) as well as coding style. If you don't know Python already, then
this is also an exercise in learning new things quickly and well. Your code should be well-commented
and documented and conform to the guidelines in the PEP 8 Style Guide for Python Code. Include some
instructions and examples of usage in your documentation. You may also want to write unit tests.
"""






import re
from urllib.parse import urlparse

class url_parse:
    def __init__(self,URL):
        scheme = ''
        netloc = ''
        path = ''
        params = ''
        query= ''
        fragment=''

    def _scheme_(self,URL):
        self.sc = re.search(r'(.*)://(.*)',URL)
        self.scheme = self.sc.group(1)
        print("Scheme by re::",self.scheme)

    def _netloc_(self,URL):
        self.nt = re.search(r'(.*)//(.*)/(.*)',URL)
        self.netloc = self.nt.group(2)
        print("Netloc by re::",self.netloc)

    def _path_(self,URL):
        self.pt = re.search(r'(.*)/(.*)\?(.*)',URL)
        self.path = self.pt.group(2)
        print("Path by re::",'/'+self.path)

    def _query_(self,URL):
        self.qt = re.search(r'(.*)\?(.*)\#(.*)',URL)
        self.query = self.qt.group(2)
        print("Query by re::",self.query)

    def _fragment_(self,URL):
        self.ft = re.search(r'(.*)#(.*)',URL)
        self.fragment = self.ft.group(2)
        print("Fragment by re::",self.fragment)


class test_url_parse:
    def __init__(self,URL):
        self.Parse = urlparse(URL)

    def _scheme_(self,URL):
        print("Scheme by urlparse::",self.Parse.scheme)

    def _netloc_(self,URL):
        print("Netloc by urlparse::",self.Parse.netloc)

    def _path_(self,URL):
        print("Path by urlparse::",self.Parse.path)

    def _query_(self,URL):
        print("Query by urlparse::",self.Parse.query)

    def _fragment_(self,URL):
        print("Fragment by urlparse::",self.Parse.fragment)

        

if __name__ == '__main__':
    print("Three test cases are there")
    URL = []
    URL.append('https://www.google.com/search?q=setter+python&oq=setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid=chrome&ie=UTF-8#q=regular+expression+in+python')
    URL.append('https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=rahul+khanna')
    URL.append('https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=loktra')

    for i in range(0,3):
        a = url_parse(URL[i])
        b = test_url_parse(URL[i])
        print("TEST CASE ::",i+1)
        a._scheme_(URL[i])
        b._scheme_(URL[i])      

        a._netloc_(URL[i])
        b._netloc_(URL[i])

        a._path_(URL[i])
        b._path_(URL[i])
    
        a._query_(URL[i])
        b._query_(URL[i])

        a._fragment_(URL[i])
        b._fragment_(URL[i])

        print("-"*30)

        



    
    
