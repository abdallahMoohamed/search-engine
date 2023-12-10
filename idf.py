# from turtle import pd
# from Phase_1 import document_of_terms as documents
# import pandas as pd
# import numpy as np
# import math 

# ########### idf ###########
# def compute_idf(tf_matrix):
#   idf_matrix = pd.DataFrame(columns=['df','idf'])
#   for i in range(len(tf_matrix)):
#     frequency = tf_matrix.iloc[i].values.sum() # iloc[3] ==> to get elements in raw 3
#     idf_matrix.loc[i,'df'] = frequency # loc[2, 'df'] ==> to put in raw 2 and column 'df' 
#     idf_matrix.loc[i,'idf'] = math.log10(10/float(frequency))
#   idf_matrix.index = tf_matrix.index
#   return idf_matrix



# ########### tf.idf ###########
# def copmute_tf_multiply_idf(tf_matrix, idf_matrix):
#   tf_mult_idf = tf_matrix.multiply(idf_matrix['idf'],axis=0)
#   return tf_mult_idf



# ########### documents length ###########
# def compute_documents_length(tf_mult_idf_matrix):
#   # to get document length for only document
#   def get_document_length(col):
#     # sqrt( (d1.0)**2 + (d1.1)**2 + (d1.2)**2 + ...) 
#     return np.sqrt(tf_mult_idf_matrix[col].apply(lambda x:x**2).sum())
  
#   documents_length = pd.DataFrame()
#   index = pd.Index([column+' length' for column in tf_mult_idf_matrix.columns],dtype='object')
#   documents_length.index = index
  
#   for column in tf_mult_idf_matrix.columns: # columns ==> d1,d2,d3 ...
#     # d1 length : 1.32342
#     documents_length.loc[column+' length','']= get_document_length(column)
#   return documents_length




# ########### normalize TF.IDF  ###########
# def compute_normalize_tf_idf(tf_mult_idf_matrix,documents_length):  
#   def get_normalized(position, x):
#     try:
#       # to get item from raw 0 or 1 or 2... and column 0, becuase we have only column
#       return x / documents_length.iloc[position].values[0] 
#     except:
#       return 0

#   noramlized_tf_idf= pd.DataFrame()
#   for position,column in enumerate(tf_mult_idf_matrix.columns):
#     noramlized_tf_idf[column] = tf_mult_idf_matrix[column].apply(lambda x: get_normalized(position,x))
#     # print(documents_length.iloc[position])
#   return noramlized_tf_idf


