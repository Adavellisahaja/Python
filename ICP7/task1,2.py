import urllib.request
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, wordpunct_tokenize
from bs4 import BeautifulSoup

# Reading from URL
wikiurl = "https://en.wikipedia.org/wiki/Google"
openurl = urllib.request.urlopen(wikiurl)
soup = BeautifulSoup(openurl.read(), "lxml")
# print(soup)

# get text
text = soup.body.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = ' '.join(chunk for chunk in chunks if chunk)


# Saving to a Text File
with open('Input', 'w') as text_file:
    text_file.write(str(text.encode("utf-8")))

# Reading from a Text File
with open('Input', 'r') as text_file:
    read_data = text_file.read()

# Tokenization
nltk.download('punkt')
stokens = nltk.sent_tokenize(text)
print("Sentence Tokenization : \n", stokens)
wtokens = nltk.word_tokenize(text)
# wtokens = [word_tokenize(t) for t in stokens]
print ("Word Tokenization : \n", wtokens)

