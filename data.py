import pandas as pd
import json as js


def load_data(path: str):

    with pd.read_json(path, lines=True, chunksize=2) as reader:

        for chunk in reader:
            print(chunk)
