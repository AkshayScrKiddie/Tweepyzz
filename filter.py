import re
import json
import pandas as pd 
import numpy as np
import string
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

tweet_files = ['results.json']
tweets = []

for file in tweet_files:
    with open(file, 'r') as f:
        for line in f.readlines():
            tweets.append(json.loads(line))

def populate_tweet_df(tweets):
        df = pd.DataFrame()
        df['text'] = list(map(lambda tweet: tweet['text'], tweets))
        df['tidy_tweet'] = np.vectorize(remove_pattern)(df['text'], "@[\w]*")
        df['tidy_tweet'] = np.vectorize(remove_pattern)(df['text'], "http:*")
        df['tidy_tweet'] = df['tidy_tweet'].str.replace("[^a-zA-Z#]| ([http[s]?://(?:[a-z]+)) | ([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ")
       # df['polarity'] = df['tidy_tweet'].apply(lambda x: TextBlob(x['tidy_tweet']).sentiment.polarity)
        print (df.head(60))
       
        df['tidy_tweet'].to_excel("results_1.xlsx")
        df['tidy_tweet'].to_csv(r'results_1.csv', header=True, index=True, sep=' ', mode='a')
       # np.savetxt(r'np.txt', df.values, fmt='%d')

        all_words = ' '.join([text for text in df['tidy_tweet']])
        wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)

        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        plt.show()
    

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt

#df['tidy_tweet'] = np.vectorize(remove_pattern)(df['tweet'], "@[\w]*")
populate_tweet_df(tweets)
