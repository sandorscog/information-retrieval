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

