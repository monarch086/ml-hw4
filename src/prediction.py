import pandas as pd
import pickle
from source import clean_text, process_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

MODEL_NAME = "MOC_KNC"


with open("../data/input.txt", "rb") as f:
    input_text = f.read().decode("utf-8")


input_df = pd.DataFrame.from_dict({
    'raw_text': [input_text]
})


input_df['cleaned_text'] = input_df['raw_text'].apply(clean_text)
input_df['processed_text'] = input_df['cleaned_text'].apply(clean_text)
input_df = input_df.drop(columns=['raw_text', 'cleaned_text'])

# print(input_df)

with open('models/Vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer: TfidfVectorizer = pickle.load(f);


tfidf_matrix = tfidf_vectorizer.transform(input_df['processed_text'])

print(tfidf_matrix)

with open('models/SVD.pkl', 'rb') as f:
    svd_transformer: TruncatedSVD = pickle.load(f);

svd_dimensions = svd_transformer.transform(tfidf_matrix)

# print(svd_dimensions)

with open(f"models/{MODEL_NAME}.pkl", "rb") as f:
    model = pickle.load(f)
    

result = model.predict(svd_dimensions)
print(result)

result = dict(zip(['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'], result.flatten()))
print(result)