import subprocess

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "pycharm": r"C:\Program Files\JetBrains\PyCharm 2025.1.1.1\bin\pycharm64.exe"
}


class AppLauncher:

    @staticmethod
    def open_app(app_name: str) -> bool:
        app = APPS.get(app_name.lower())

        if app:
            subprocess.Popen(app)
            return True

        return False
