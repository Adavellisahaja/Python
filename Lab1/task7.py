import nltk
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.stem import WordNetLemmatizer
from nltk import ngrams, FreqDist

#reading the data from a file
with open('nlp_input.txt','r') as text_file:
    read_data = text_file.read()

# Word and Sentence Tokenization
nltk.download('punkt')
stokens = nltk.sent_tokenize(read_data)
print("Sentence Tokenization : \n", stokens)
wtokens = nltk.word_tokenize(read_data)
print ("Word Tokenization : \n", wtokens)

# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("Lemmatization:")
print(lemmatizer.lemmatize(read_data))
print('\n')

# Trigrams
trigrams = list(ngrams(wtokens,3))
print("trigrams:")
print(trigrams)
# Fetching the Top 10 trigrams
word_freq = FreqDist(trigrams)
mostCommon = word_freq.most_common()
print("Frequency of each trigram : \n", mostCommon)
top10 = word_freq.most_common(10)
print("Top 10 triGrams : \n", top10)

# Sentence with most repeated trigram and concatenating the sentence
# print(sentTokens)
concatenatedArray = []
for sentence in stokens:
    for x, y, z in trigrams:
        for ((a, b, c), length) in top10:
            if(x, y, z == a, b, c):
                concatenatedArray.append(sentence)
print("Concatenated Array : ",concatenatedArray)
print("Maximum of Concatenated Array : ", max(concatenatedArray))