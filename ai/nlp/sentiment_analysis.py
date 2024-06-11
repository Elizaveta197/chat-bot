import random

class SentimentAnalyzer:
    def __init__(self):
        self.sentiments = ['positive', 'neutral', 'negative']

    def analyze(self, tokens):
        return random.choice(self.sentiments)
