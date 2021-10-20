import urllib.request
def connect():
    try:
        urllib.request.urlopen('http://google.com') 
        return True
    except:
        return False
print( 'connected' if connect() else 'no internet!' )
