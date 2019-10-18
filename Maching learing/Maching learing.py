import numpy as np
import pandas as pd
import random



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


urls_data = pd.read_csv('urldata.csv')
#print(urls_data.head)

def maketokones(f):
    tkns_byslash = str(f.encode('utf-8')).split('/')
    total_Tokens = []
    for i in tkns_byslash:
        tokens = str(i).split('-')
        tkns_bydot = []
        for j in range(0,len(tokens)):
            temp_tokens = str(tokens[j]).split('.')
            tkns_bydot = total_Tokens + temp_tokens
        total_Tokens = total_Tokens + tokens + tkns_bydot
    total_Tokens = list(set(total_Tokens))

    if 'com' in total_Tokens:
        total_Tokens.remove('com')
    return total_Tokens


y = urls_data['label']

url_list = urls_data['url']



vectorizer = TfidfVectorizer(tokenizer=maketokones)

x = vectorizer.fit_transform(url_list)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

logit = LogisticRegression()
logit.fit(x_train,y_train)

x_predict = ['google.com/search=jcharistech','google.com/search=faizanahmad']

x_predict = vectorizer.transform(x_predict)
New_predict = logit.predict(x_predict)
print(New_predict)

















#89448bc76cce47fe18240e3743bf397a65f455c3c7d4a57a4fb73cfb60a8d71e my api