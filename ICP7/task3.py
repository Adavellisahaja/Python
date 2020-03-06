import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import pos_tag, wordpunct_tokenize, ne_chunk
from nltk.util import ngrams


with open('Input', 'r') as text_file:
    read_data = text_file.read()

# Tokenization
nltk.download('punkt')
stokens = nltk.sent_tokenize(read_data)
print("Sentence Tokenization : \n", stokens)
wtokens = nltk.word_tokenize(read_data)
# wtokens = [word_tokenize(t) for t in stokens]
print ("Word Tokenization : \n", wtokens)

#PartOfSpeech tagging
# pos_tag: processes a sequence of words and attaches a part of speech tag to each word.
tagged = nltk.pos_tag(read_data)
print("Part Of Speech taggin:")
print(tagged)

#Stemming
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
pStemmer = PorterStemmer()
print("PosterStemmer:")
for i in wtokens:
 print(pStemmer.stem(i), end='')
print('\n')
lStemmer = LancasterStemmer()
print("Lancaster Stemmer:")
for i in wtokens:
 print(lStemmer.stem(i), end='')
print('\n')
sStemmer = SnowballStemmer('english')
print("SnowballStemmer:")
for i in wtokens:
 print(sStemmer.stem(i), end='')
print('\n')

 # Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("Lemmatization:")
print(lemmatizer.lemmatize(read_data))
print('\n')

# Named Entity Recognition
print("Named Entity Recognition:")
x= ne_chunk(pos_tag(wordpunct_tokenize(read_data)))
print(type(x))
for t in x:
    print(t)

# trigram
trigrams = list(ngrams(wtokens,3))
print("trigrams:")
print(trigrams)


