import urllib
import pandas as pd
import numpy as np
import re, nltk # nltk.download() Run this if you do not have nltk in your machine
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

nltk.data.path.append('./nltk_data/')

### TRAINING AND TESTING DATA ###
def test_data_df(df):
    test_data_initial = df
    test_data_initial.columns = ["Keyword"]
    return test_data_initial


def train_data_df():
    train_data = 'data_kw/train_data.csv'
    train_data_initial = pd.read_csv(train_data, header=None)
    train_data_initial.columns = ["Sentiment","Keyword"]
    return train_data_initial


### WRITE TO FILE ###
def write_to_csv_kw(kw_pred):
    kw_pred.to_csv("data_kw/kw_pred.csv", encoding='utf-8', index=False)


### INTENT FINDER ###
def kw_intent_finder(test_data):
    test_data_final = test_data
    train_data_final = train_data_df()    
    stemmer = PorterStemmer()

    def stem_tokens(tokens, stemmer):
        stemmed = []
        for item in tokens:
            stemmed.append(stemmer.stem(item))
        return stemmed

    def tokenize(text):
        # remove non letters
        text = re.sub("[^a-zA-Z]", " ", text)
        # tokenize
        tokens = nltk.word_tokenize(text)
        # stem
        stems = stem_tokens(tokens, stemmer)
        return stems

    vectorizer = CountVectorizer(
        analyzer = 'word',
        tokenizer = tokenize,
        lowercase = True,
        stop_words = 'english',
        max_features = 85
    )

    corpus_data_features = vectorizer.fit_transform(train_data_final.Keyword.tolist() + test_data_final.Keyword.tolist())
    corpus_data_features_nd = corpus_data_features.toarray()
    vocab = vectorizer.get_feature_names()

    ### SUM UP THE COUNTS OF EACH VOCABULARY WORD ###
    dist = np.sum(corpus_data_features_nd, axis=0)

    X_train, X_test, y_train, y_test  = train_test_split(
            corpus_data_features_nd[0:len(train_data_final)],
            train_data_final.Sentiment,
            train_size=0.85,
            random_state=1234
            )
    log_model = LogisticRegression()
    log_model = log_model.fit(X=X_train, y=y_train)
    y_pred = log_model.predict(X_test)

    ### TRAIN CLASSIFIER ###
    log_model = LogisticRegression()
    log_model = log_model.fit(X=corpus_data_features_nd[0:len(train_data_final)], y=train_data_final.Sentiment)

    ### PREDICT ###
    test_pred = log_model.predict(corpus_data_features_nd[len(train_data_final):])
    test_pred_final = pd.DataFrame(test_pred, columns = ['Intent'])
    test_data_pred = pd.concat([test_data_final, test_pred_final], axis=1)

    ### DROP DUPLICATES ###
    test_data_pred = test_data_pred.drop_duplicates(['Keyword'], keep='last')
    # test_data_pred_buy = test_data_pred[test_data_pred['Intent'] == 1]

    ### CONVERT 0 AND 1 TO TRAN AND INFO
    test_data_pred.Intent.replace([1, 0],['Transaction', 'Information'], inplace=True)

    ### CONVERT TO JSON
    # test_data_pred_JSON = test_data_pred.to_json(path_or_buf = None, orient = 'records', date_format = 'epoch', double_precision = 10, force_ascii = True, date_unit = 'ms', default_handler = None)

    ## WRITE ###
    # write_to_csv_kw(test_data_pred)
    # with open('data_kw/data_kw.json', 'w') as f:
    #     json.dump(test_data_pred_JSON, f)

    ### RETURN RAW DATA ###
    return test_data_pred
