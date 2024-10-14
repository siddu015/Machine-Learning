from urllib.request import urlopen
url = "https://gutenberg.org/cache/epub/39561/pg39561.txt"
raw = urlopen(url).read().decode('utf-8')
print(raw[:1000])

type(raw)
len(raw)