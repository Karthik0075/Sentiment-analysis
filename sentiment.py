from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import numpy as np


def percentage(x, y):
    return 100 * float(x) / float(y)


x1 = "dTcNCWsm5rAdOIuLxe9wFqTHP"  # consumer key
x2 = "fUUV2vsDYkgC2YS1JloQpWwCFTRQS4IY0e7iyhX34BvnZX6Jxm"  # consumer secret
x3 = "1108353266973171712-k7g4IOHyVHMRBALL1m43VrFpJmmh2O"  # access token
x4 = "EB8ZmAOXBoO6ydnaDDsor3YQSibAQo6H8b24FKfOSHlAR"  # access token secret


auth = tweepy.OAuthHandler(consumer_key=x1, consumer_secret=x2)
auth.set_access_token(x3, x4)
api = tweepy.API(auth)

searchterm = input("Enter Keyword//hashtag to search about~~")
noofsearchterm = int(input("Enter the number of tweets to analyze from twitter: "))

tweets = tweepy.Cursor(api.search, q=searchterm,).items(noofsearchterm)

positive = 0
negative = 0
neutral = 0
polarity = 0


for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)


    polarity = analysis.sentiment.polarity
    print(polarity)


    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noofsearchterm)
negative = percentage(negative, noofsearchterm)
neutral = percentage(neutral, noofsearchterm)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchterm + " by analyzing " + str(noofsearchterm) + " Tweets.")

if(polarity == 0):
    print("Neutal")
elif (polarity < 0):
    print("Negative")
elif (polarity > 0):
    print("positive")

choice = 1
while (choice != 0):
    print("0->Exit")
    print("1->Pie chart")
    print("2->percentage bar/Bar graph")
    print("Enter the choice")
    choice = int(input())
    if choice== 1:
        """if (polarity == 0):
            print("Neutal")
        elif (polarity < 0):
            print("Negative")
        elif (polarity > 0):
            print("positive")"""

        labels = ['Positive[' + str(positive) + '%]', 'Neutral[' + str(neutral) + '%]',
                  'Negative[' + str(negative) + '%]']
        sizes = [positive, neutral, negative]
        colors = ['yellow', 'orange', 'black']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + searchterm + ' by analysing ' + str(noofsearchterm) + ' Tweets. ')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    if choice== 2:

        x = [positive,negative,neutral]
        y = [positive,negative,neutral]
        plt.bar(x, y, label='polarities')

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('How people are reacting on ' + searchterm + ' by analysing ' + str(noofsearchterm) + ' Tweets. ')
        plt.legend()
        plt.show()



    if choice== 0:
        print("EXIT")
print()