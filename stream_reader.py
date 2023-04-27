import pandas as pd
import multiprocessing as mp
from pre_processor import pre_process
from sys import getsizeof
from collections import Counter
import pickle
import os

# /home/vboxuser/TP1/information-retrieval/corpus.jsonl
# /home/vboxuser/TP1/information-retrieval/tests


def chunk_handler(chunk):

    index = {}

    documents_info = pd.DataFrame({
        'docid': [],
        'text_size': [],
        'token_count': [],
        'title': []
    }).astype(int)

    #print('m')
    for i, row in chunk.iterrows():

        tokens = pre_process(row['text'])
        tokens.extend(pre_process(row['title']))

        # determine TF
        term_frequency = Counter(tokens)

        # Store Document info
        new_doc = pd.DataFrame({
            'docid': [row['id']],
            'text_size': [getsizeof(row['text'])],
            'token_count': [len(tokens)],
            'title': [row['title']]
        })
        documents_info = pd.concat([documents_info, new_doc], ignore_index=True)

        # Index update
        for term in term_frequency.keys():
            if term in index:
                index[term].append((row['id'], term_frequency[term]))
            else:
                index[term] = [(row['id'], term_frequency[term])]

    # Persist data
    documents_info.to_csv('doc_infos/doc_info_' + str(chunk.iloc[0].id) + '.csv', index=False)
    with open('indexes/partial_index_' + str(chunk.iloc[0].id) + '.pkl', 'wb') as f:
        pickle.dump(index, f)

    #print('Fim')


def load_data(path: str):


    os.makedirs('doc_infos/')
    os.makedirs('indexes/')

    with pd.read_json(path, lines=True, chunksize=10_000) as reader:

        with mp.Pool(4) as pool:
            # pool.imap(chunk_handler, reader, chunksize=1)
            pool.imap(chunk_handler, reader)
            pool.close()
            pool.join()


