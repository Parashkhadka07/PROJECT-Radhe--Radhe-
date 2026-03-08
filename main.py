import urllib.request
x=urllib.request.urlopen("https://www.google.com")
print(x.read().decode("utf-8"))