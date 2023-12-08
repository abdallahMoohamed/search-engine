from Phase_2 import positional_index

query = input("Enter Word to search for : ")
# query = 'fools fear'
finalList = [[] for i in range (10)]

# for word in query.split():
#     for key in positional_index[word][1].keys():
      
#         if finalList[key-1] != []:
#           if finalList[key-1][-1] == positional_index[word][1][key][0] -1:
#               finalList[key-1].append(positional_index[word][1][key][0])
#         else:
#             finalList[key-1].append(positional_index[word][1][key][0])

for word in query.split():
    for key in positional_index[word][1].keys():
        if finalList[key-1] != positional_index[word][1][key][0] -1:
            finalList[key-1].append(positional_index[word][1][key][0])
        else:
            finalList[key-1].append(positional_index[word][1][key][0])



for position , list in enumerate(finalList , start = 1):
    if len(list) == len(query.split()):
        print(position)