import json
import pathlib

from typing import Any, Callable, Dict, List


def open_json(path: str) -> Dict:
    with open(path, "r") as f:
        return json.loads(f.read())


def save_json(o: Dict[str, Any], path: str) -> None:
    with open(path, "w") as f:
        f.write(json.dumps(o, ensure_ascii=False))


def translation_path(original_path: str, language: str) -> str:
    name = pathlib.Path(original_path).stem
    return f"{name}.{language}.json"


class TranslationError(Exception):
    pass


class BadArgumentException(Exception):
    pass
