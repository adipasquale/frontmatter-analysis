# FrontMatter Analysis

Collects FrontMatter data from a list of files and analyze it for useful insights

Usecases:

- count the tags occurences in a static blog
- identify outliers like poorly spelled attributes or values

## Usage

```sh
poetry install
poetry run python -m fma.analyze /home/pwd/some-dir-with-md-files
```

## Development

```sh
poetry run jupyter notebook
```