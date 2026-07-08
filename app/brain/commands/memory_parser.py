class MemoryParser:
    """
    Parses conversational memory commands.
    """

    @staticmethod
    def parse_remember(command: str):

        text = command.lower()

        if "remember that my " not in text:
            return None

        sentence = text.replace(
            "remember that my ",
            ""
        )

        if " is " not in sentence:
            return None

        key, value = sentence.split(
            " is ",
            1
        )

        return key.strip(), value.strip()

    @staticmethod
    def parse_recall(command: str):

        text = command.lower()

        if text.startswith("what is my "):

            return text.replace(
                "what is my ",
                ""
            ).strip()

        if text.startswith("who is my "):

            return text.replace(
                "who is my ",
                ""
            ).strip()

        return None

    @staticmethod
    def parse_forget(command: str):

        text = command.lower()

        if text.startswith("forget my "):

            return text.replace(
                "forget my ",
                ""
            ).strip()

        return None