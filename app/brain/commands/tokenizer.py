import re


class Tokenizer:

    @staticmethod
    def tokenize(text: str) -> list[str]:

        text = re.sub(r"[^\w\s]", "", text)

        text = text.lower()

        return text.split()