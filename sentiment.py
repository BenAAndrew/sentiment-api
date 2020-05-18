from collections import Counter
from os import getcwd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.data.path.append(getcwd())
sid = SentimentIntensityAnalyzer()


def cleanText(text):
    text = re.sub("[^a-zA-Z ]", "", text)
    words = text.split(" ")
    return [word.lower() for word in words if word]


def getSentiment(text, sentiment_threshold):
    words = cleanText(text)
    occurances = dict(Counter(words))
    sentiment = {}

    for word in set(words):
        score = sid.polarity_scores(word)["compound"]
        if abs(score) >= sentiment_threshold:
            sentiment[word] = {"occurances": occurances[word], "score": score}

    return sentiment
