# assistant.py

class Assistant:

    def __init__(self, ai_engine):

        self.ai_engine = ai_engine

    def run(self) -> None:

        print("=" * 60)
        print("AXEL AI")
        print("=" * 60)

        while True:

            command = input("\nYou: ")

            if command.lower() == "exit":

                print("AXEL: Goodbye!")

                break

            response = self.ai_engine.process(command)

            print(f"AXEL: {response}")