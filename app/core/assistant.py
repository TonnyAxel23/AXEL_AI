from app.brain.command_processor import CommandProcessor


class Assistant:

    def __init__(self):

        self.processor = CommandProcessor()

    def run(self):

        print("=" * 50)
        print("AXEL AI")
        print("=" * 50)

        while True:

            command = input("\nYou: ")

            if command.lower() == "exit":

                print("AXEL: Goodbye!")

                break

            response = self.processor.process(command)

            print(f"AXEL: {response}")