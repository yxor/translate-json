from .console import ConsoleManager
import logging
import dotenv


def main():
    dotenv.load_dotenv()
    logging.getLogger().setLevel(logging.INFO)
    try:
        ConsoleManager.translate_file()
    except Exception as e:
        logging.error(e)
