from textblob import TextBlob
import matplotlib.pyplot as plt
import os
import sys


def get_average(l):
    s = sum(l)
    length = len(l)
    return s/length

size = int(sys.argv[3])

for root, dir, files in os.walk(sys.argv[1]):
    fig, axs = plt.subplots(len(files)//2+1, 2, sharex=True, sharey=True)
    fig.suptitle("Sentiment analysis of {} Novels".format(sys.argv[2]))
    index = 0
    for file in files:
        print(f"Analyzing book: {file}")
        sentiments_polarity = []
        sentiments_subjectivity = []
        filepath = os.path.join(root, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            t = TextBlob(f.read())
            f.close()

        i = 0
        counter = 0
        temp_sentence = ""
        for sentence in t.sentences:
            if i < size:
                temp_sentence += sentence.__str__()
                i += 1
            else:
                s = TextBlob(temp_sentence)
                sentiments_polarity.append(s.sentiment.polarity)
                sentiments_subjectivity.append(s.sentiment.subjectivity)
                temp_sentence = ""
                i = 0
                counter += 1

        average_pol = get_average(sentiments_polarity)
        average_sub = get_average(sentiments_subjectivity)
        ax = axs[index//2][index%2]
        ax.plot(sentiments_polarity)
        ax.set_title(file)
        ax.set_ylabel('polarity')
        ax.set_xlabel('Average polarity (compound): {}'
                      '        '
                      'Average subjectivity: {}'.format(round(average_pol, 5), round(average_sub, 5)))
        index += 1

    plt.show()
    if not os.path.exists("sentiment_tb"):
        os.mkdir("sentiment_tb")
    fig.tight_layout()
    fig.savefig("./sentiment_tb/{}_bulk{}.png".format(sys.argv[2], size), bbox_inches='tight', dpi=100)
