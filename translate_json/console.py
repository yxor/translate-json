import os
import argparse
import pathlib
import logging

from .utils import BadArgumentException
from .translate import translate_all


def is_valid_json_file(path: str) -> bool:
    return (
        os.path.exists(path) and os.path.isfile(path) and path.lower().endswith(".json")
    )


class ConsoleManager:
    @staticmethod
    def translate_file():
        parser = argparse.ArgumentParser(
            description="Translate all string values in a JSON file to multiple languages using the google translate API"
        )

        parser.add_argument(
            "-f", "--file", type=str, required=True, help="The input file path"
        )

        parser.add_argument(
            "-s",
            "--source-language",
            type=str,
            required=True,
            help="The source language code",
        )

        parser.add_argument(
            "-o",
            "--out",
            type=str,
            default=None,
            required=False,
            help="The output directory path, will contain the created translation files",
        )

        parser.add_argument(
            "-l",
            "--langs",
            required=True,
            nargs="+",
            help="List of target languages you want to translate the file to",
        )

        parser.add_argument(
            "-k",
            "--key",
            type=str,
            help='Google translate API key, don\'t set this if you already have a key set as the environement variable "GOOGLE_TRANSLATE_TOKEN"',
        )

        args = parser.parse_args()
        if not args.langs:
            raise BadArgumentException(
                "You must provide a list of languages to translate to"
            )

        if not args.source_language or len(args.source_language) < 2:
            raise BadArgumentException(
                "You must provide the source language of the file"
            )

        if args.file is None or not is_valid_json_file(args.file):
            raise BadArgumentException("You must provide a valid input file")

        if args.out is not None:
            try:
                pathlib.Path(args.out).mkdir(parents=True, exist_ok=True)
            except OSError as e:
                raise BadArgumentException("You must provide a valid output directory")
        else:
            args.out = "."

        if args.key is not None:
            os.environ["GOOGLE_TRANSLATE_TOKEN"] = args.key

        logging.info(
            f'Translating file in path [{args.file}] to the languages [{", ".join(args.langs)}], output is set to [{args.out}]'
        )

        translate_all(args.file, args.source_language, args.langs, args.out)
