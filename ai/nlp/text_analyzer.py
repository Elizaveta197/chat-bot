import numpy as np

class TextAnalyzer:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.sentiment_analyzer = SentimentAnalyzer()

    def analyze(self, text):
        tokens = self.tokenizer.tokenize(text)
        sentiment = self.sentiment_analyzer.analyze(tokens)
        return {
            'tokens': tokens,
            'sentiment': sentiment,
            'complexity': self._calculate_complexity(tokens)
        }

    def _calculate_complexity(self, tokens):
        return np.log(len(tokens) + 1) * np.sqrt(sum(len(token) for token in tokens) / len(tokens))
