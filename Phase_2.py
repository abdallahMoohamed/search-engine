documents = [['antony' , 'brutus' , 'caeser' , 'cleopatra' , 'mercy' , 'worser'],
['antony' , 'brutus' , 'caeser' , 'calpurnia'],
['mercy' , 'worser'],
['brutus' , 'caeser' , 'mercy' , 'worser'],
['caeser' , 'mercy' , 'worser'],
['antony' , 'caeser' , 'mercy'],
['angels' , 'fools' , 'fear' , 'in' , 'rush' , 'to' , 'tread' , 'where'],
['angels' , 'fools' , 'fear' , 'in' , 'rush' , 'to' , 'tread' , 'where'],
['angels' , 'fools' , 'in' , 'rush' , 'to' , 'tread' , 'where'],
['fools' , 'fear' , 'in' , 'rush' , 'to' , 'tread' , 'where']]

document_number = 0 
positional_index = {}

for document in documents:
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
print(positional_index)
