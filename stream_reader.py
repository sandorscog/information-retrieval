import pandas as pd
from multiprocessing.pool import ThreadPool
import multiprocessing as mp
from pre_processor import pre_process
import os
from sys import getsizeof
from collections import Counter

# /home/vboxuser/TP1/information-retrieval/corpus.jsonl
# /home/vboxuser/TP1/information-retrieval/tests


def chunk_handler(chunk):
    # print(chunk)

    documents_info = pd.DataFrame({
        'docid': [],
        'text_size': [],
        'token_count': []
    }).astype(int)

    print('mariana')
    for index, row in chunk.iterrows():
        # print(index)
        # print(row)

        tokens = pre_process(row['text'])
        # title
        # keywords

        term_frequency = Counter(tokens)

        new_doc = pd.DataFrame({
            'docid': [row['id']],
            'text_size': [getsizeof(row['text'])],
            'token_count': [len(tokens)]
        })
        documents_info = pd.concat([documents_info, new_doc], ignore_index=True)


    print(len(documents_info))

    # indexing: count of lexicons

    documents_info.to_csv('doc_infos/doc_info_' + str(chunk.iloc[0].id) + '.csv', index=False)
    chunk.to_csv('tests/' + str(chunk.iloc[0].id) + '.csv', index=False)
    print(documents_info.info)
    print('Fim')


def load_data(path: str):

    with pd.read_json(path, lines=True, chunksize=10_000) as reader:

        with mp.Pool(4) as pool:
            # pool.imap(chunk_handler, reader, chunksize=1)
            pool.imap(chunk_handler, reader)
            pool.close()
            pool.join()


