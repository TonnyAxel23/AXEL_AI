class CommandParser:

    def extract_app(self, command):

        command = command.lower()

        words = [

            "open",

            "launch",

            "run",

            "start",

            "please",

            "could",

            "you",

            "can"

        ]

        for word in words:

            command = command.replace(word, "")

        return command.strip()