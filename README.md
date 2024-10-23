# Translate Deepl API
Implement the [deepl](https://deepl.com) API to make text translation. I'm making a project to use third API to make this software intent.

## SUMMARY
1. [Description](#description)
2. [Dependencies](#dependencies)
3. [Structure](#structure)
4. [Models](#models)
5. [Response](#response)

## Description
This software was built to access the [DeepL API](https://developers.deepl.com/docs/) and make languages translates.

It's my intention to build some useful applications to grown up my skills about programming.

We provide the service for:
* only one word (single);
* phrases (one word or more);
* texts (something large until 2000 characters).

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

## Response

---
That's all folks!
[Go Ahead](#translate-deepl-api).
