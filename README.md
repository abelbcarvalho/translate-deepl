# Translate Deepl API
Implement the [deepl](https://deepl.com) API to make text translation. I'm making a project to use third API to make this software intent.

## SUMMARY
1. [Description](#description)
2. [Dependencies](#dependencies)
3. [Structure](#structure)
4. [Models](#models)
5. [Languages Codes](#languages-codes)
6. [Translate Model](#translate-model)
7. [Response](#response)

## Description
This software is being built to access the [DeepL API](https://developers.deepl.com/docs/) and make languages translates.

It's my intention to build some useful applications to grown up my skills about programming.

We provide the service for:
* only one word (single);
* phrases (one word or more);
* texts (something large until 5000 characters).

## Dependencies
Here is the list of installed dependencies. First, this project is built using [Python3](https://docs.python.org/3) as programming languages and some libraries listed below.

* [Flask](https://flask.palletsprojects.com/en/3.0.x/);
* [Pydantic](https://docs.pydantic.dev/latest/);
* [PyTestAsyncio](https://docs.pytest.org/en/stable/);
* [DeepL Lib](https://github.com/DeepLcom/deepl-python);
* [PythonDotEnv](https://github.com/theskumar/python-dotenv);

As well, we provide a file named [requirements.txt](./requirements.txt) with all the dependencies, since the packages listed here to their requirements dependencies.

You can install all these dependencies just typing the following command at your device.

```commandline
pip install -r requirements.txt
```

## Structure
The package structure of the project [root](/).

```text
src/
├──controller/
├──core/
├──enums/
├──models/
├──routes/
├──use_cases/
├──utilities/
tests/
.env.example
.gitignore
app.py
LICENSE
README.md
requirements.txt
```

## Models
Here is the build of our models. Note: *attributes with '?' are optionals.*

* WordModel

```json
{
  "word": "",
  "target_lang": "",
  "source_lang?": "string or null",
}
```

* PhraseModel

```json
{
  "phrase": "",
  "target_lang": "",
  "source_lang?": "string or null",
}
```

* TextModel

```json
{
  "text": "",
  "target_lang": "",
  "source_lang?": "string or null",
}
```

## Languages Codes
Here I present to you a link to another documentation file where you'll can see the languages valid. It's what you find at enumerate for backend level.
* Doc: [LANGUAGES.md](./LANGUAGES.md);

If you want to see the documentation on [deepl.com](https://deepl.com) website, you can access:
* [DeepL doc target language](https://developers.deepl.com/docs/resources/supported-languages#target-languages);

## Translate Model
This model get data from another base model and it's used to send data to *DeepL API*.

| Field                  | Type                     | Description                                   |
|------------------------|--------------------------|-----------------------------------------------|
| text                   | `str`                    | Text to be translated                         |
| target_lang            | `EnumLang`              | Target language                               |
| source_lang            | `Optional[EnumLang]`    | Source language (optional)                    |
| context                | `Optional[str]`         | Additional context (optional)                 |
| split_sentences        | `Optional[str]`         | Indicates if sentences should be split (optional)|
| preserve_formatting     | `Optional[bool]`        | Indicates if formatting should be preserved (optional)|
| formality              | `Optional[str]`         | Desired level of formality (optional)        |
| glossary_id            | `Optional[str]`         | Glossary ID (optional)                        |
| show_billed_characters | `Optional[bool]`        | Indicates if billed characters should be shown (optional)|
| tag_handling           | `Optional[str]`         | How to handle tags (optional)                |
| outline_detection      | `Optional[bool]`        | Indicates if outline structures should be detected (optional)|
| non_splitting_tags     | `Optional[List[str]]`    | Tags that should not be split (optional)     |
| splitting_tags         | `Optional[List[str]]`    | Tags that should be split (optional)         |
| ignore_tags            | `Optional[List[str]]`    | Tags to be ignored (optional)                |


## Response

---
That's all folks!
[Go Ahead](#translate-deepl-api).
