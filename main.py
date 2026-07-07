from app.core.startup import StartupManager
from app.core.assistant import Assistant


def main():

    startup = StartupManager()

    container = startup.initialize()

    ai_engine = container.get("ai_engine")

    assistant = Assistant(ai_engine)

    assistant.run()


if __name__ == "__main__":

    main()