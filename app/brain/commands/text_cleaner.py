import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:

        text = text.lower()

        text = re.sub(r"[^\w\s]", "", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()