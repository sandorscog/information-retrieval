import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import string

nltk.download('stopwords')
nltk.download('punkt')


def pre_process(text: str):
    snowball = SnowballStemmer(language='english')
    stop_words = set(stopwords.words('english'))
    text = text.lower()

    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [snowball.stem(token) for token in tokens]

    return tokens


