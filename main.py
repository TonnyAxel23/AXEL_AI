# main.py

from app.config.settings import settings

from app.lifecycle.startup import start
from app.lifecycle.shutdown import stop
from app.lifecycle.runtime import Runtime


def main() -> None:
    """
    AXEL application entry point.
    """

    app, container = start()

    runtime = Runtime(container)

    try:

        match settings.RUNTIME_MODE:

            case "cli":
                runtime.cli()

            case "voice":
                runtime.voice()

            case "gui":
                runtime.gui()

            case "api":
                runtime.api()

            case _:
                raise ValueError(
                    f"Unknown runtime mode: {settings.RUNTIME_MODE}"
                )

    finally:

        stop(app)


if __name__ == "__main__":
    main()
