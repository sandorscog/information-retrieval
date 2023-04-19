import pandas as pd
from multiprocessing.pool import ThreadPool
import multiprocessing as mp
from pre_processor import pre_process
import os

# /home/vboxuser/TP1/information-retrieval/corpus.jsonl
# /home/vboxuser/TP1/information-retrieval/tests


def chunk_handler(chunk):

    texts = chunk['text']

    print('mariana')
    for i in texts:
        pre_process(i)

    chunk.to_csv('tests/' + str(chunk.iloc[0].id) + '.csv', index=False)
    print('Fim')


def load_data(path: str):

    res = []
    with pd.read_json(path, lines=True, chunksize=10_000) as reader:

        with mp.Pool(4) as pool:
            pool.imap(chunk_handler, reader, chunksize=1)
            pool.close()
            pool.join()
