import pyshorteners
url = ("https://www.youtube.com/channel/UC1SB4wu5760RERv_ujVPz2g?view_as=subscriber")
s = pyshorteners.Shortener()
print("your shortened url is:  ",s.tinyurl.short(url))


