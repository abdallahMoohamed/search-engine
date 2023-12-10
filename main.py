from itertools import product
import math
from Phase_1 import document_of_terms as documents

from preprocessing_two import compute_term_frequency,compute_normalize_tf_idf, copmute_tf_multiply_idf,compute_idf, compute_w_tf,compute_documents_length
import pandas as pd
import numpy as np

def get_query_details(q,tf_matrix,idf_matrix):
  tf_array= []
  query = pd.DataFrame(index=tf_matrix.index)
  for term in list(tf_matrix.index):
    if term in q.split():
      tf_array.append(1)
    else:
      tf_array.append(0)
  query['tf'] = tf_array
  query['w_tf'] = query['tf'].apply(lambda x: math.log10(x)+1 if x>0 else 0)  
  query['idf'] = idf_matrix['idf'] * query['w_tf']
  query['tf_idf'] = query['w_tf'] * query['idf'] 
  query['norm'] = 0
  idf_values = np.array(query['idf'].values)
  normalization_factor = math.sqrt(np.sum(idf_values**2))
  for i in range(len(query)):
    query['norm'].iloc[i] = float(query['idf'].iloc[i]) / normalization_factor 
  
  return query

def get_product (q, noramlized_tf_idf, tf_matrix, idf_matrix):
  query = get_query_details(q, tf_matrix, idf_matrix)
  temp = noramlized_tf_idf.multiply(query['w_tf'],axis=0)
  product = temp.multiply(query['norm'],axis=0)
  
  similarity  = {}
  for col in product.columns: 
    if 0 not in product[col].loc[q.split()].values:
      similarity [col] = product[col].sum()
      
  products_result = product[list(similarity .keys())].loc[q.split()]
  similarity_sort = sorted(similarity.items(), key = lambda x:x[1], reverse=True)
  docs_sort = [doc[0] for doc in similarity_sort]

  return products_result, similarity, docs_sort


if __name__ == '__main__':
  q = 'antony brutus'
  tf_matrix = compute_term_frequency()
  idf_matrix = compute_idf(tf_matrix)
  tf_mult_idf_matrix = copmute_tf_multiply_idf(tf_matrix,idf_matrix)
  documents_length = compute_documents_length(tf_mult_idf_matrix)
  noramlized_tf_idf = compute_normalize_tf_idf(tf_mult_idf_matrix,documents_length)
  
  query_details = get_query_details(q, tf_matrix, idf_matrix )
  # print(query_details)

  products_result, similarity,docs_sort = get_product(q, noramlized_tf_idf, tf_matrix, idf_matrix)
  print('\n################ products_result ###################')
  print(products_result)
  print('\n################ similarity ###################')
  print(similarity)
  print('\n################ docs_sort ###################')
  print(docs_sort)
  