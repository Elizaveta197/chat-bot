import asyncio
import unittest


# test_bot.py
class BotTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_start_command(self):
        response = await bot_test_client.send_command("/start")
        self.assertIn("Добро пожаловать", response)

    async def test_help_command(self):
        response = await bot_test_client.send_command("/help")
        self.assertIn("Список команд", response)

    async def test_text_message_handling(self):
        response = await bot_test_client.send_message("Какой сегодня день?")
        self.assertIn("Сегодня", response)
