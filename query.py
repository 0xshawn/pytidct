from readmdict import MDX, MDD
from pyquery import PyQuery as pq

filename = '简明英汉字典增强版-去音标.mdx'
headwords = [*MDX(filename)]
items = [*MDX(filename).items()]
if len(headwords) == len(items):
    print(f'Load success, total {len(headwords)} words')
else:
    print('Failed to load')

query_words = 'admission'
word_index = headwords.index(query_words.encode())
word, html = items[word_index]
word, html = word.decode(), html.decode()

print(word)
print(html)