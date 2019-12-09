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
size = int(sys.argv[2])

for root, dirs, files in os.walk(path):
    for file in files:
        print(f"Analyzing book: {file}")
        sentiments_polarity = []
        sentiments_subjectivity = []
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            text = f.read()
            tb = TextBlob(text)
        f.close()

        sentences = tb.sentences

        i = 0
        counter = 0
        temp_sentence = ""
        for sentence in sentences:
            if i < size:
                temp_sentence += sentence.__str__()
                i += 1
            else:
                s = TextBlob(temp_sentence)
                sentiments_polarity.append(analyzer.polarity_scores(temp_sentence))
                sentiments_subjectivity.append(s.sentiment.subjectivity)
                temp_sentence = ""
                i = 0
                counter += 1

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
        fig.suptitle(f"VaderSentiment Analysis of {file}")
        plt.ylabel('polarity')
        plt.xlabel('Average polarity (compound): {}'
                      '        '
                      'Average subjectivity: {}'.format(round(average_pol, 5), round(average_sub, 5)))
        x = range(len(sentiments_polarity))
        b1 = plt.bar(x, neg, width=1)
        b2 = plt.bar(x, neu, width=1, bottom=neg)
        b3 = plt.bar(x, pos, width=1, bottom=neu)
        plt.legend((b1[0], b2[0], b3[0]), ('neg', 'neu', 'pos'))
        if not os.path.exists("sentiment_vader_outputs/{}".format(str(size))):
            os.mkdir("sentiment_vader_outputs/{}".format(str(size)))
        fig.savefig("./sentiment_vader_outputs/{}/{}.png".format(str(size), file.split('.')[0]))
