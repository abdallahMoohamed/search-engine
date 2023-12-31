
from turtle import pd
from Phase_1 import document_of_terms as documents
import pandas as pd
import numpy as np
import math 

all_words = []
for doc in documents:
  for word in doc:
    all_words.append(word)
  
def get_term_freq(doc):
  term_freq = dict.fromkeys(all_words,0)
  for word in doc:
    term_freq[word] +=1 
  return term_freq


term_freq = pd.DataFrame(get_term_freq(documents[0]).values() , index = get_term_freq(documents[0]).keys())
for i in range(1, len(documents)):
  term_freq[i] = get_term_freq(documents[i]).values()
term_freq.columns = ['doc'+str(i) for i in range(1,11)]

def get_weighted_term_freq(x):
  if x>0:
    return math.log(x) + 1
  else:
    return 0
for i in range(1, len(documents)+1):
  term_freq['doc'+str(i)]= term_freq['doc'+str(i)].apply(get_weighted_term_freq)
  
# print(term_freq)



######################### IDF and TF IDF ##########################
tfd = pd.DataFrame(columns=['freq','idf'])
for i in range(len(term_freq)):
  frequency = term_freq.iloc[i].values.sum() # type: ignore
  tfd.loc[i, 'freq'] = frequency
  tfd.loc[i,'idf'] = math.log(10/ (float(frequency)))
tfd.index = term_freq.index  
# print(tfd)

term_freq_mult_tfd = term_freq.multiply(tfd['idf'],axis=0)
# print(term_freq_mult_tfd)



# document length
document_length = pd.DataFrame()

def get_docs_length(col):
  return np.sqrt(term_freq_mult_tfd[col].apply(lambda x:x**2).sum())

for column in term_freq_mult_tfd.columns:
  document_length.loc[0,column+"_len"] = get_docs_length(column)

# print(document_length)

######################### normalize TF.IDF  #####################
normalized_term_freq_idf = pd.DataFrame()

def get_normalized(col, x):
  try:
    return x / document_length[col+'_len'].values[0]
  except:
    return 0

for column in term_freq_mult_tfd.columns:
  normalized_term_freq_idf[column] = term_freq_mult_tfd[column].apply(lambda x: get_normalized(column,x))

################################### query details ###################################
def get_w_tf(x):
  try:
    return math.log10(x)+1
  except:
    return 0
  
q = 'antony brutus'
query = pd.DataFrame(index=term_freq.index)
array = [] #[1 if x in q.split() else 0 for x in list(term_freq.index)]
for x in list(term_freq.index):
  if x in q.split():
    array.append(1)
  else:
    array.append(0)

query['tf'] = array 
query['w_tf'] = query['tf'].apply(lambda x:get_w_tf(x))
# print(query)   ########## DONE

# multiply every column in normalized tf.idf with query['w_tf] that's column also
product = normalized_term_freq_idf.multiply(query['w_tf'],axis=0)
# print(f'\n{normalized_term_freq_idf}\n')
# print(query['w_tf'])
# print(f'\n{product}') 
 
query['idf'] = tfd['idf'] * query['w_tf']
# print('\n',tfd)
# print('\n',query)

query['tf_idf'] = query['w_tf'] * query['idf']
query['norm'] = 0
# print('\n',(query)) 

idf_values = np.array(query['idf'].values)
normalization_factor = math.sqrt(np.sum(idf_values**2))
# query_length = math.sqrt()
for i in range(len(query)):
  query['norm'].iloc[i] = float(query['idf'].iloc[i]) / normalization_factor  
print(query) ##### DONE

product2 = normalized_term_freq_idf.multiply(query['w_tf'],axis=0).multiply(query['norm'],axis=0)
print(product2)

scores = {}
for col in product2.columns: 
  print(q.split())
  print('product2[col].loc[q.split()].values :',product2[col].loc[q.split()].values)
  if 0 in product2[col].loc[q.split()].values: # q.split = ['antony','brutus']
    pass
  else:
    scores[col] = product2[col].sum()
print(scores) # cosine similarity 

products_result = product2[list(scores.keys())].loc[q.split()]
print(products_result)
# print(products_result.sum())
print(scores)
scores_sort = sorted(scores.items(), key = lambda x:x[1], reverse=True)
print(scores_sort)

for doc in scores_sort:
  print(doc[0] , end=' ')
