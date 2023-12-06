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
print(files_name)

documentOfTerms = []
for files in files_name:
    with open(f'files/{files}','r') as f:
        document = f.read()
    tokenizedDocument = word_tokenize(document)
    terms = []
    for word in tokenizedDocument:
        if word not in stop_words:
            terms.append(word)
    documentOfTerms.append(terms)

    