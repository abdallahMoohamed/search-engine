# from turtle import pd
# from Phase_1 import document_of_terms as documents
# from Phase_1 import all_words
# import pandas as pd
# import numpy as np
# import math 


# ########### term frequenecy(tf) ###########
# def get_term_freq(doc): # for one docmuent
#   """ 
#     to create dictionary contain all words with value=0
#     {'antony': 0, 'brutus': 0, 'caeser': 0, ....}
#   """
#   term_freq = dict.fromkeys(all_words,0) 
#   for word in doc: # get every word from doc
#     term_freq[word] +=1 # get it from term_freq dictionary and add 1 to this value
#   return term_freq

# def compute_term_frequency(): 
#   # to initialize matrix and put index
#   tf_matrix = pd.DataFrame(index = get_term_freq(documents[0]).keys()) 
#   # to add the documnets to dataFrame
#   for i in range(0, len(documents)):
#     tf_matrix[i] = get_term_freq(documents[i]).values()
#   tf_matrix.columns = ['d'+str(i) for i in range(1,11)] # to rename the columns with d1,d2,...
#   return tf_matrix


# ########### w.tf ###########
# def compute_w_tf(tf_matrix):
#   wtf_matrix = tf_matrix
#   for i in range(1, len(documents)+1):
#     wtf_matrix['d'+str(i)] = wtf_matrix['d'+str(i)].apply(lambda x: math.log(x)+1 if x>0 else 0)
#   return wtf_matrix


# """ 
#   1-
#   list = []
#   for i in range (1,11):
#     list.append('d'+str(i))
#   return list
  
#   2- 
#   ['d'+str(i) for i in range(1,11)]
# """