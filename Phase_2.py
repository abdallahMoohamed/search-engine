from Phase_1 import document_of_terms

document_number = 0 
positional_index = {}

for document in document_of_terms:
    for positional, term in enumerate(document):
        if term in positional_index:
            positional_index[term][0] = positional_index[term][0] +1
            if document_number in positional_index[term][1]:
                positional_index[term][1][document_number].append(positional)
            else:
                positional_index[term][1][document_number]=[positional]
        else:
            positional_index[term]=[]
            positional_index[term].append(1)
            positional_index[term].append({})
            positional_index[term][1][document_number] = [positional]
    document_number += 1

