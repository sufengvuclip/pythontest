import nltk
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# ps = PorterStemmer()
with io.open(u"E:\\workspace\\sufeng\\pythontest\\doc\\new_year_videos.txt",'r',-1,encoding="utf-8") as f:
    str = f.read()

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(str)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

# stemmed_sentence = []
# for w in filtered_sentence:
#     stemmed_sentence.append(ps.stem(w))
# print(stemmed_sentence)

