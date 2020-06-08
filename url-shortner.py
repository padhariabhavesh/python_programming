import pyshorteners
url = ("https://www.youtube.com/watch?v=dXHYE9Zf7YY&t=47s")
s = pyshorteners.Shortener()
print("your shortened url is:  ",s.tinyurl.short(url))


