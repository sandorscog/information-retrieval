import pandas as pd
from multiprocessing.pool import ThreadPool
import multiprocessing as mp
from pre_processor import pre_process
import os

# /home/vboxuser/TP1/information-retrieval/corpus.jsonl
# /home/vboxuser/TP1/information-retrieval/tests


def chunk_handler(chunk):
    print('pirula')
    texts = chunk['text']

    print('mariana')
    for i in texts:
        pre_process(i)

    print('sandor')
    chunk.to_csv('tests/' + len(os.listdir()) + '.csv', index=False)
    print('done')


def load_data(path: str):

    with pd.read_json(path, lines=True, chunksize=10000) as reader:
        pool = mp.Pool(4)

        ll_ = []
        for chunk in reader:
            res = pool.apply_async(chunk_handler, (chunk,))

            ll_.append(res)

        #res.close()
        #res.join()
        #with ThreadPool(processes=2) as pool:
            #pool.map(partial_indexer, reader)



