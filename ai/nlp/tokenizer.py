class Tokenizer:
    def __init__(self):
        self.delimiters = " .,;:!?"

    def tokenize(self, text):
        tokens = []
        current_token = ""
        for char in text:
            if char in self.delimiters:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char
        if current_token:
            tokens.append(current_token)
        return tokens
