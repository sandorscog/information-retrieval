import pickle
import pandas as pd
import os
from collections import Counter
from sys import getsizeof


def merge_index():

    '''
    # final_index = {}

    # num_of_keys = []
    os.makedirs('term_lists/')

    for file in os.listdir('indexes/'):
        with open('indexes/' + file, 'rb') as f:
            partial_index = pickle.load(f)
            # num_of_keys.extend(partial_index)

            for key in partial_index.keys():
                try:
                    with open('term_lists/' + key, 'ab') as term_file:
                        for doc in partial_index[key]:

                            docid_bytes = doc[0].to_bytes(4, 'big')
                            tf_bytes = doc[1].to_bytes(4, 'big')
                            term_file.write(docid_bytes)
                            term_file.write(tf_bytes)

                except Exception as e:
                    print(e)

            for key in partial_index.keys():
                if key in final_index:
                    final_index[key].extend(partial_index[key])
                else:
                    final_index[key] = partial_index[key]

            print(getsizeof(final_index))'''

    print('term indexes done')

    # Create term lexicon and merge all the partial indexes
    start_of_term = 0
    for file in os.listdir('term_lists/'):
        with open('term_lists/' + file, 'rb') as current_term:
            byte_sequence = current_term.read()

        df = int(len(byte_sequence) / 8)

        # (term, byte in index, df)
        lexic_tuple = (file, start_of_term, df)

        # Add reference to lexic
        with open('lexic.txt', 'a') as lexic:
            lexic.write(str(lexic_tuple) + '\n')

        # Add to index
        with open('index', 'ab') as index:
            index.write(byte_sequence)

        start_of_term += len(byte_sequence)

    # print(len(set(num_of_keys)))
    print('done')


# testes
def visualise():
    with open('term_lists/act', 'rb') as file:
        byte_sequence = file.read()

        num_registros = int(len(byte_sequence)/8)

        for i in range(num_registros):

            init = i*8
            x = int.from_bytes(byte_sequence[init:init+4], 'big')
            y = int.from_bytes(byte_sequence[init+4:init+8], 'big')
            print(x, y)

        print(len(byte_sequence))


merge_index()
# visualise()
# 18489784
