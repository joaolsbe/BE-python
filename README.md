# Del 2 - poetry

Før vi setter i gang med å kjøre koden, så skal vi sette opp prosjektet ordentlig med poetry.

Det første vi må gjøre er å installere pakken: 

```
pip install poetry
```

Så skal vi initiere et poetry-prosjekt:

```
poetry init
```

Fyll inn informasjon som du bes om. Når du kommer til "Would you like to define your main dependencies interactively?" og "Would you like to define your development dependencies interactively?" så kan du skrive "no".

Du vil da få generert ei ny fil som heiter `pyproject.toml`, med ca dette innholdet:

```
[tool.poetry]
name = "be-python-jo"
version = "0.1.0"
description = "Dette er en pakke vi utvikler i forbindelse med best practice python kurs."
authors = ["Joakim Olsen"]
license = "Ingen"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
