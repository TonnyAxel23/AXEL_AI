from app.config.settings import settings
from app.core.logger import logger


def main():
    logger.info("AXEL AI started")

    print("=" * 50)
    print(settings.APP_NAME)
    print(f"Version: {settings.APP_VERSION}")
    print("=" * 50)

    print("AXEL AI is running...")


if __name__ == "__main__":
    main()