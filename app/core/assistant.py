class Assistant:
    """
    Handles the interaction between
    the user and the AI Engine.
    """

    def __init__(self, ai_engine) -> None:
        self.ai_engine = ai_engine

    def run(self) -> None:

        print("=" * 60)
        print("           AXEL AI ASSISTANT")
        print("=" * 60)
        print("Type 'exit' to quit.\n")

        while True:

            command = input("You: ").strip()

            if not command:
                continue

            if command.lower() == "exit":
                print("AXEL: Goodbye!")
                break

            response = self.ai_engine.process(command)

            print(f"AXEL: {response}")