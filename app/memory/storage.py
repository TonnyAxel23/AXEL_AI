import json
from pathlib import Path


class MemoryStorage:

    def __init__(self) -> None:

        # Directory containing storage.py
        memory_dir = Path(__file__).resolve().parent

        self.file = memory_dir / "memory.json"

        # Ensure the directory exists
        self.file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # Create the file if it doesn't exist
        if not self.file.exists():

            self.file.write_text(
                "{}",
                encoding="utf-8"
            )

    def load(self) -> dict:

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def save(self, data: dict) -> None:

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )