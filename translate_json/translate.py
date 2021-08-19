import logging
import requests
import json
import os

from typing import Any, Callable, Dict, List
from .utils import TranslationError, open_json, save_json, translation_path

TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"


def translate(value: str, source: str, target: str) -> str:
    r = requests.get(
        TRANSLATE_URL,
        {
            "q": value,
            "source": source,
            "target": target,
            "key": os.getenv("GOOGLE_TRANSLATE_TOKEN"),
        },
    )
    translation = json.loads(r.content)

    if not translation.get("data") or not translation["data"].get("translations"):
        raise TranslationError(
            "Error getting the data from google translate API, make sure you are using a valid API key"
        )

    return translation["data"]["translations"][0].get("translatedText")


def translate_value(
    value: Any,
    source: str,
    target: str,
    translate_object: Callable[[Dict[str, Any], str, str], Dict[str, Any]],
):
    if isinstance(value, str):
        return translate(value, source, target)
    if isinstance(value, dict):
        return translate_object(value, source, target)
    elif isinstance(value, list):
        return [
            translate_value(translation, source, target, translate_object)
            for translation in value
        ]

    else:
        return value


def translate_object(o: Dict[str, Any], source: str, target: str) -> Dict[str, Any]:
    translation = {}

    for key, value in o.items():
        translation[key] = translate_value(value, source, target, translate_object)

    return translation


def translate_all(
    input_path: str, source_language: str, target_languages: List[str], output_dir: str
):
    source_object = open_json(input_path)

    for language in target_languages:
        logging.debug(f"Translating file from [{source_language}] to [{language}]")
        translated_object = translate_object(source_object, source_language, language)
        save_json(
            translated_object,
            os.path.join(output_dir, translation_path(input_path, language)),
        )
