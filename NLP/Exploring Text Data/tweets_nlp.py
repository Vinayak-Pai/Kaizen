"""
Source:Analytics vidya- NLP Introduction
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re

# to read the data
dataset = pd.read_csv('D:\some_code\Kaizen\\NLP\Exploring Text Data\\tweets.csv', encoding='ISO-8859-1')
# print(dataset.head())


# to generate frequency table
def gen_freq(text):
    # Will store the list of words
    word_list = []

    # Loop over all the tweets and extract words into word_list
    for tw_words in text.split():
        word_list.extend(tw_words)

    # Create word frequencies using word_list
    word_freq = pd.Series(word_list).value_counts()
    return word_freq


#word_freq = gen_freq(dataset.text.str)
# print(word_freq)

# Visualisation using word cloud
# wc = WordCloud(width=400, height=330, max_words=100, background_color='white').generate_from_frequencies(word_freq)
#
# plt.figure(figsize=(12, 8))
# plt.imshow(wc, interpolation='bilinear')
# plt.axis('off')
# plt.show()


# Text cleaning to remove some noise and stop words
def clean_text(text):
    # Remove RT
    text = re.sub(r'RT', '', text)

    # Fix &
    text = re.sub(r'&amp;', '&', text)

    # Remove punctuations
    text = re.sub(r'[?!.;:,#@-]', '', text)

    # Convert to lowercase to maintain consistency
    text = text.lower()
    return text


# some english constructs which add to the noise of data
# print(STOPWORDS)

text = dataset.text.apply(lambda x: clean_text(x))
word_freq = gen_freq(text.str)*100
word_freq = word_freq.drop(labels=STOPWORDS, errors='ignore')


# Generate word cloud
wc = WordCloud(width=450, height=330, max_words=200, background_color='white').generate_from_frequencies(word_freq)

plt.figure(figsize=(12, 14))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
# plt.show()

"""
NLP, using NLTK
"""

# Tokenisation

from nltk.tokenize import sent_tokenize , word_tokenize
text = "HI folks! Lets learn and better our best. "
sent_tokenize(text)
word_tokenize(text)


# Stemming
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem("played"))
print(stemmer.stem("playing"))
print(stemmer.stem("increases"))


# Lemmatisation

from nltk.stem import WordNetLemmatizer

lemm = WordNetLemmatizer()
print(lemm.lemmatize("increases"))
print(lemm.lemmatize("running", pos="v"))

# parts of speech tag
from nltk import pos_tag
tokens = word_tokenize("Hi I'm Joey. How you doing? Friends Forever.")
print(pos_tag(tokens))

# dictionary association

from nltk.corpus import wordnet
print(wordnet.synsets('computer'))


#ngrams

from nltk import ngrams
sentence = " I love my country"
n= 2 #bigrams
for i in ngrams(word_tokenize(sentence), n):
    print(i)
