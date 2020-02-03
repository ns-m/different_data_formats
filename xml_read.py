import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter
from itertools import chain


def coint_in_xml():
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    items = root.findall('channel/item')
    news_description = []
    for n_d in items:
        news_description.append(n_d.find('description').text)
    words_news = str(news_description).lower().split()
    long_word = []
    for word in words_news:
        if len(word) > 6:
            long_word.append(word)
    words_news_count = Counter(chain.from_iterable(map(str.split, long_word)))
    pprint(words_news_count.most_common(10))

coint_in_xml()