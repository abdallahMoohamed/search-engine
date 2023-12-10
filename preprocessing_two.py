from turtle import pd
from Phase_1 import document_of_terms as documents
import pandas as pd
import numpy as np
import math 
from Phase_1 import all_words


########### term frequenecy(tf) ###########
def get_term_freq(doc): # for one docmuent
  """ 
    to create dictionary contain all words with value=0
    {'antony': 0, 'brutus': 0, 'caeser': 0, ....}
  """
  term_freq = dict.fromkeys(all_words,0) 
  for word in doc: # get every word from doc
    term_freq[word] +=1 # get it from term_freq dictionary and add 1 to this value
  return term_freq

def compute_term_frequency(): 
  # to initialize matrix and put index
  tf_matrix = pd.DataFrame(index = get_term_freq(documents[0]).keys()) 
  # to add the documnets to dataFrame
  for i in range(0, len(documents)):
    tf_matrix[i] = get_term_freq(documents[i]).values()
  tf_matrix.columns = ['d'+str(i) for i in range(1,11)] # to rename the columns with d1,d2,...
  return tf_matrix


########### w.tf ###########
def compute_w_tf(tf_matrix):
  wtf_matrix = tf_matrix
  for i in range(1, len(documents)+1):
    wtf_matrix['d'+str(i)] = wtf_matrix['d'+str(i)].apply(lambda x: math.log10(x)+1 if x>0 else 0)
  return wtf_matrix
  """ 
    1-
    list = []
    for i in range (1,11):
      list.append('d'+str(i))
    return list
    
    2- 
    ['d'+str(i) for i in range(1,11)]
  """

########### idf ###########
def compute_idf(tf_matrix):
  idf_matrix = pd.DataFrame(columns=['df','idf'])
  for i in range(len(tf_matrix)):
    frequency = tf_matrix.iloc[i].values.sum() # iloc[3] ==> to get elements in raw 3
    idf_matrix.loc[i,'df'] = frequency # loc[2, 'df'] ==> to put in raw 2 and column 'df' 
    idf_matrix.loc[i,'idf'] = math.log10(10/float(frequency))
  idf_matrix.index = tf_matrix.index
  return idf_matrix



########### tf.idf ###########
def copmute_tf_multiply_idf(tf_matrix, idf_matrix):
  tf_mult_idf = tf_matrix.multiply(idf_matrix['idf'],axis=0)
  return tf_mult_idf



########### documents length ###########
def compute_documents_length(tf_mult_idf_matrix):
  # to get document length for only document
  def get_document_length(col):
    # sqrt( (d1.0)**2 + (d1.1)**2 + (d1.2)**2 + ...) 
    return np.sqrt(tf_mult_idf_matrix[col].apply(lambda x:x**2).sum())
  
  documents_length = pd.DataFrame()
  index = pd.Index([column+' length' for column in tf_mult_idf_matrix.columns],dtype='object')
  documents_length.index = index
  
  for column in tf_mult_idf_matrix.columns: # columns ==> d1,d2,d3 ...
    # d1 length : 1.32342
    documents_length.loc[column+' length','']= get_document_length(column)
  return documents_length



########### normalize TF.IDF  ###########
def compute_normalize_tf_idf(tf_mult_idf_matrix,documents_length):  
  def get_normalized(position, x):
    try:
      # to get column='' and raw = position, we have only column is name:''

      return x / documents_length[''].iloc[position] 
    except:
      return 0

  noramlized_tf_idf= pd.DataFrame()
  for position,column in enumerate(tf_mult_idf_matrix.columns):
    noramlized_tf_idf[column] = tf_mult_idf_matrix[column].apply(lambda x: get_normalized(position,x))
    # print(documents_length.iloc[position])
  return noramlized_tf_idf


############## main ##############
if __name__ == "__main__":
  tf_matrix = compute_term_frequency()
  print('\n######################### term frequency #########################')
  print(tf_matrix)
  
  wtf_matrix = compute_w_tf(tf_matrix)
  print('\n######################### weighted term frequency #########################')
  print(wtf_matrix)
  
  idf_matrix = compute_idf(tf_matrix)
  print('\n######################### df idf #########################')
  print(idf_matrix)
  
  tf_mult_idf_matrix = copmute_tf_multiply_idf(tf_matrix,idf_matrix)
  print('\n######################### tf_multiply_idf #########################')
  print(tf_mult_idf_matrix)
  
  documents_length = compute_documents_length(tf_mult_idf_matrix)
  print('\n######################### documents_length #########################')
  print(documents_length)

  noramlized_tf_idf = compute_normalize_tf_idf(tf_mult_idf_matrix,documents_length)
  print('\n######################### normalized tf.idf #########################')
  print(noramlized_tf_idf)





# documents_length[column].iloc[row] 