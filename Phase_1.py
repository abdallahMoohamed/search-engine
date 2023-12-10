import os
import tokenize
import nltk
from nltk import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from natsort import natsorted

stop_words = stopwords.words('english')
stop_words.remove('in')
stop_words.remove('to')
stop_words.remove('where')

files_name = natsorted(os.listdir('files'))

document_of_terms = []
all_words = []
for files in files_name:
    with open(f'files/{files}','r') as f:
        document = f.read()
    tokenized_document = word_tokenize(document)
    terms = []
    for word in tokenized_document:
        if word not in stop_words:
            all_words.append(word)
            terms.append(word)
    document_of_terms.append(terms)

