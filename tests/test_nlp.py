# test_nlp.py
import asyncio
import unittest

class NLPTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_text_analysis(self):
        result = await analyze_text("Пример текста для анализа")
        self.assertIsNotNone(result)
        self.assertEqual(result['sentiment'], 'positive')

    async def test_tokenization(self):
        tokens = await tokenize_text("Тестовое предложение для токенизации")
        self.assertGreater(len(tokens), 0)
        self.assertIn('тестовое', tokens)

    async def test_sentiment_analysis(self):
        sentiment = await analyze_sentiment("Это предложение счастливое")
        self.assertIn(sentiment, ['positive', 'negative', 'neutral'])


