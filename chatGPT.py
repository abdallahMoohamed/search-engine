import os
import re
import math
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Assuming you have NLTK installed, if not, you can install it using: pip install nltk
# Also, download the punkt package by running: nltk.download('punkt')

# Step 1: Read 10 files (.txt)
def read_files(folder_path):
    files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                files.append((filename, file.read()))
    return files

# Step 2: Apply tokenization
def tokenize(text):
    return word_tokenize(text)

# Step 3: Apply stemming
def stem(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

# Step 4: Build positional index
def build_positional_index(files):
    positional_index = defaultdict(lambda: defaultdict(list))

    for file_id, (filename, content) in enumerate(files):
        tokens = stem(tokenize(content))
        for position, term in enumerate(tokens):
            positional_index[term][file_id].append(position)

    return positional_index

# Step 5: Compute term frequency
def compute_term_frequency(positional_index):
    tf_matrix = defaultdict(lambda: defaultdict(int))

    for term, positions in positional_index.items():
        for file_id, positions_list in positions.items():
            tf_matrix[term][file_id] = len(positions_list)

    return tf_matrix

# Step 6: Compute IDF
def compute_idf(positional_index, num_documents):
    idf_matrix = {}
    
    for term, positions in positional_index.items():
        idf_matrix[term] = math.log(num_documents / len(positions))

    return idf_matrix

# Step 7: Compute TF.IDF matrix
def compute_tfidf(tf_matrix, idf_matrix):
    tfidf_matrix = defaultdict(lambda: defaultdict(float))

    for term, files in tf_matrix.items():
        for file_id, tf in files.items():
            tfidf_matrix[term][file_id] = tf * idf_matrix[term]

    return tfidf_matrix

# Step 8: Allow users to write a phrase query
def phrase_query(positional_index, query):
    query_terms = stem(tokenize(query))
    result = set(range(len(files)))

    for term in query_terms:
        if term in positional_index:
            result &= set(positional_index[term].keys())
        else:
            # Handle the case when a term is not in the index
            result = set()

    return result

# Step 9: Compute similarity between the query and matched documents
def compute_similarity(tfidf_matrix, query_vector):
    similarities = {}

    for file_id, document_vector in tfidf_matrix.items():
        dot_product = sum(query_vector[term] * document_vector[term] for term in query_vector)
        query_norm = math.sqrt(sum(value ** 2 for value in query_vector.values()))
        doc_norm = math.sqrt(sum(value ** 2 for value in document_vector.values()))

        if query_norm == 0 or doc_norm == 0:
            similarities[file_id] = 0
        else:
            similarities[file_id] = dot_product / (query_norm * doc_norm)

    return similarities

# Step 10: Rank documents based on similarity score
def rank_documents(similarities):
    return sorted(similarities.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    folder_path = "e:/computer science/study matrials/Level 4/1'st term/IR/project/search-engine/files"
    files = read_files(folder_path)

    positional_index = build_positional_index(files)
    tf_matrix = compute_term_frequency(positional_index)
    print(tf_matrix)
    
    num_documents = len(files)
    idf_matrix = compute_idf(positional_index, num_documents)
    tfidf_matrix = compute_tfidf(tf_matrix, idf_matrix)

    query = "antony brutus"
    matched_documents = phrase_query(positional_index, query)

    # Create a query vector for similarity calculation
    query_vector = defaultdict(int)
    for term in stem(tokenize(query)):
        query_vector[term] = 1  # Assuming binary representation for the query terms

    similarities = compute_similarity(tfidf_matrix, query_vector)
    ranked_documents = rank_documents(similarities)

    print("Matched Documents:", matched_documents)
    print("Ranked Documents:", ranked_documents)
