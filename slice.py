import pandas as pd

#df = pd.DataFrame()

with pd.read_json('/home/vboxuser/TP1/information-retrieval/corpus.jsonl', lines=True, chunksize=100) as reader:
    for chunk in reader:
        df = chunk
        break

#print(df)
#df.to_json('/home/vboxuser/TP1/information-retrieval/sliced.json', lines=True, orient='records')
df = 0

print(pd.read_json('/home/vboxuser/TP1/information-retrieval/sliced.json', lines=True))
