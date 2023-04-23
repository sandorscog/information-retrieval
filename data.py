import pandas as pd
import json as js
from pre_processor import pre_process

# /home/vboxuser/TP1/information-retrieval/corpus.jsonl


def chunk_handler(chunk):
    print(type(chunk['text']))
    texts = chunk['text']

    for i in texts:
        text_tokens = pre_process(i)
        print(text_tokens, flush=True)


def load_data(path: str):

    total = 0
    div = 0

    with pd.read_json(path, lines=True, chunksize=100000) as reader:

        for chunk in reader:
            # print(chunk.memory_usage(deep=True).sum())
            total += chunk.memory_usage(deep=True).sum()
            div += 1
            chunk_handler(chunk)

    print(total/div)



