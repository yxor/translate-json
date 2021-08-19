[![Stars][stars-shield]][stars-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# Translate JSON

## About The Project

This is a command line tool to translate all string values in a JSON file to multiple languages using the Google Cloud Translate API.

## Getting Started

### Prerequisites

To run this program you need to have python 3.9 installed on your machine.

### Installation

1. To use this you need to have a [google translate API key](https://cloud.google.com/translate)
2. Install the package
   ```sh
   pip install translate-json
   ```

## Usage

You can use this program as a command line tool.

```
usage: translate-json [-h] -f FILE -s SOURCE_LANGUAGE [-o OUT] -l LANGS [LANGS ...] -k KEY

Translate all string values in a JSON file to multiple languages using the google translate API.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The input file path
  -s SOURCE_LANGUAGE, --source-language SOURCE_LANGUAGE
                        The source language code
  -o OUT, --out OUT     The output directory path, will contain the created translation files
  -l LANGS [LANGS ...], --langs LANGS [LANGS ...]
                        List of target languages you want to translate the file to
  -k KEY, --key KEY     Google translate API key, don't set this if you already have a key set as the environement
                        variable "GOOGLE_TRANSLATE_TOKEN"
```

### CLI Example

A file called `source.json` contains the following values

```JSON
{
   "title": "Hello World",
   "tags": {
      "lara": ["Video games", "swimming", "Interrupt routines"],
      "david": [
         {
            "value": "Baseball",
            "count": 5
         },
         "Climbing trees"
      ]
   },
   "example": {
      "title": "This will be translated",
      "ok": true
   }
}
```

To translate this file to dutch and french, you can run this command

```sh
translate-json -f source.json -s en -o ./translations/ -l nl fr -k YOUR_API_KEY
```

After running the command, the `translations` folder will contain two files: `source.nl.json` and `source.fr.json`.

```JSON
{
   "title": "Bonjour le monde",
   "tags": {
      "lara": [
         "Jeux vidéo",
         "la natation",
         "Routines d'interruption"
      ],
      "david": [
         {
               "value": "Base-ball",
               "count": 5
         },
         "Grimper aux arbres"
      ]
   },
   "example": {
      "title": "Cela sera traduit",
      "ok": true
   }
}
```

```JSON
{
    "title": "Hallo Wereld",
    "tags": {
        "lara": [
            "Computerspellen",
            "zwemmen",
            "Routines onderbreken"
        ],
        "david": [
            {
                "value": "Basketbal",
                "count": 5
            },
            "Bomen klimmen"
        ]
    },
    "example": {
        "title": "Dit wordt vertaald",
        "ok": true
    }
}
```

### Example

You can also import this library and use it in your code

```python
from translate_json.translate import translate_all


if __name__=="__main__":
   # you must set the google cloud translate API key as an environment variable before running this program
   translate_all('source.json', 'en', ['nl', 'de', 'fr'], './dist/')

```

## Contributing

Any contributions you make are **greatly appreciated**

## License

Distributed under the MIT License. See `LICENSE` for more information.

[forks-shield]: https://img.shields.io/github/forks/yxor/translate-json.svg?style=for-the-badge
[forks-url]: https://github.com/yxor/translate-json/network/members
[stars-shield]: https://img.shields.io/github/stars/yxor/translate-json.svg?style=for-the-badge
[stars-url]: https://github.com/yxor/translate-json/stargazers
[issues-shield]: https://img.shields.io/github/issues/yxor/translate-json.svg?style=for-the-badge
[issues-url]: https://github.com/yxor/translate-json/issues
[license-shield]: https://img.shields.io/github/license/yxor/translate-json.svg?style=for-the-badge
[license-url]: https://github.com/yxor/translate-json/blob/master/LICENSE
