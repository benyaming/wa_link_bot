import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from wa_link_bot.bot import _load_environment


class BotConfigTest(unittest.TestCase):
    def test_load_environment_reads_dotenv_from_current_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, ".env").write_text(
                "BOT_TOKEN=token-from-dotenv\n"
                "DEFAULT_COUNTRY_CODE=44\n",
                encoding="utf-8",
            )

            current_directory = os.getcwd()
            try:
                os.chdir(directory)
                with patch.dict(os.environ, {}, clear=True):
                    _load_environment()

                    self.assertEqual(os.getenv("BOT_TOKEN"), "token-from-dotenv")
                    self.assertEqual(os.getenv("DEFAULT_COUNTRY_CODE"), "44")
            finally:
                os.chdir(current_directory)


if __name__ == "__main__":
    unittest.main()
