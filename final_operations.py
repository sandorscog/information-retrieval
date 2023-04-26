import pickle
import pandas as pd
import os
from collections import Counter


def merge_index():

    for file in os.listdir('indexes/'):
        with open('indexes/' + file, 'rb') as f:
            partial_index = pickle.load(f)

            for key in partial_index.keys():
                #print(partial_index[key])
                try:
                    with open('term_lists/' + key, 'ab') as file:
                        for doc in partial_index[key]:
                            pass
                            #print(doc)
                except:
                    print(key)



# testes
merge_index()

