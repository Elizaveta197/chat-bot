import random

class SpeechToTextConverter:
    def __init__(self, model_path):
        self.model_path = model_path
        self.load_model()

    def load_model(self):
        pass

    def convert(self, audio_data):
        return " ".join([self.random_word() for _ in range(15)])

    def random_word(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        return ''.join(random.choice(letters) for i in range(random.randint(4, 8)))

