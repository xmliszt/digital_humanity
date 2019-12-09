from textblob import TextBlob
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import sys


def get_average(l):
    s = sum(l)
    length = len(l)
    return s/length


analyzer = SentimentIntensityAnalyzer()

path = sys.argv[1]
file_name = os.path.basename(path)

print(f"Analyzing book: {file_name}")
sentiments_polarity = []
sentiments_subjectivity = []
with open(path, 'r', encoding='utf-8') as f:
    t = TextBlob(f.read())
    for sentence in t.sentences:
        sentiments_polarity.append(analyzer.polarity_scores(sentence))
        sentiments_subjectivity.append(sentence.sentiment.subjectivity)
f.close()

pos = []
neu = []
neg = []
compound = []
for i in sentiments_polarity:
    pos.append(i['pos'])
    neu.append(i['neu'])
    neg.append(i['neg'])
    compound.append(i['compound'])

average_pol = get_average(compound)
average_sub = get_average(sentiments_subjectivity)

fig = plt.figure()
fig.suptitle(f"VaderSentiment Analysis of {file_name}")
plt.ylabel('polarity')
plt.xlabel('Average polarity (compound): {}'
              '        '
              'Average subjectivity: {}'.format(round(average_pol, 5), round(average_sub, 5)))
x = range(len(t.sentences))
b1 = plt.bar(x, neg, width=1)
b2 = plt.bar(x, neu, width=1, bottom=neg)
b3 = plt.bar(x, pos, width=1, bottom=neu)
plt.legend((b1[0], b2[0], b3[0]), ('neg', 'neu', 'pos'))

plt.show()
