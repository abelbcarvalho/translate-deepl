# Translate Deepl API
Implement the [deepl](https://deepl.com) API to make text translation. I'm making a project to use third API to make this software intent.

## SUMMARY
1. [Description](#description)
2. [Dependencies](#dependencies)
3. [How To Run?](#how-to-run)
   1. [Running Tests](#running-tests)
4. [Structure](#structure)
5. [Models](#models)
6. [Languages Codes](#languages-codes)
7. [Translate Model](#translate-model)
8. [Routes](#routes)
9. [Response](#response)

## Description
This software is being built to access the [DeepL API](https://developers.deepl.com/docs/) and make languages translates.

It's my intention to build some useful applications to grown up my skills about programming.

We provide the service for:
* only one word (single);
* texts (something large until 5000 characters).

## Dependencies
Here is the list of installed dependencies. First, this project is built using [Python3](https://docs.python.org/3) as programming languages and some libraries listed below.

* [Flask](https://flask.palletsprojects.com/en/3.0.x/);
* [Flask Async](https://flask.palletsprojects.com/en/stable/async-await/);
* [PyTest](https://docs.pytest.org/en/stable/);
* [Pydantic](https://docs.pydantic.dev/latest/);
* [DeepL Lib](https://github.com/DeepLcom/deepl-python);
* [PythonDotEnv](https://github.com/theskumar/python-dotenv);

As well, we provide a file named [requirements.txt](./requirements.txt) with all the dependencies, since the packages listed here to their requirements dependencies.

You can install all these dependencies just typing the following command at your device.

```commandline
pip install -r requirements.txt
```

## How To Run?
For this topic, it's required you've been installed the all dependencies. So you can know run this project locally. *Remember to configure the `.env` file before with the required keys found at [.env.example](.env.example), renaming it to just **.env** or creating another file with this name.

**You need a DeepL account to have access to an API key and replace it to the `.env` file.**

To Run our application locally, just type:

```commandline
python app.py
```

Or access the file [app.py](app.py).

### Running Tests
To run our suite of Unitary Tests with PyTest, just type a command or use our IDE graphic user interface.

The command is:

```commandline
pytest
```

## Structure
The package structure of the project [root](/).

```text
src/
├──controllers/
├──core/
├──enums/
├──exceptions/
├──models/
├──routes/
├──services/
├──use_cases/
├──utilities/
├──├──adapters/
├──├──checkers/
├──├──language/
├──├──response/
tests/
├──controller/
├──mocks/
├──routes/
├──service/
├──use_case/
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
* Doc: [LANGUAGES.md](LANGUAGES.md);

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

## Routes

Base URL: `/api/v1/deepl`

Method: **POST**
#### route: /translate/word
#### route:  /translate/text

**NOTE:** See the models for Text and Word routes here. The body for each one.

## Response
Basically our responses can be errors or json success with data and status code 200.

For route [word](#route-translateword):

```json
{
  "word": "word translated"
}
```

For route [text](#route-translatetext):

```json
{
  "text": "text translated"
}
```

---
That's all folks!
[Go Ahead](#translate-deepl-api).
