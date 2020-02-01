import json
from pprint import pprint
from collections import Counter
from itertools import chain


def coint_in_json():
    with open('newsafr.json') as news_json:
        json_data = json.load(news_json)
    news = json_data['rss']['channel']['items']
    news_description = []
    for n_d in news:
        news_description.append(n_d['description'])
    words_news = str(news_description).replace("['", '').split()
    long_word = []
    for word in words_news:
        if len(word) > 6:
            long_word.append(word)
    words_news_count = Counter(chain.from_iterable(map(str.split, long_word)))
    pprint(words_news_count.most_common(10))

coint_in_json()