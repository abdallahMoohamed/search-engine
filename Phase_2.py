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
            positional_index[term]=[] # 'antony': []
            positional_index[term].append(1) # 'antony':[1]
            positional_index[term].append({}) # 'antony':[1, { }]
            positional_index[term][1][document_number] = [positional] # 'antony':[1, { 0: [0] }]
    document_number += 1

print(positional_index)


