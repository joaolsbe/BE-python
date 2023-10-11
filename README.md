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

Vi ønsker også å strukturere mappen bedre. Poetry har ein foreslått struktur for pakker. Denne strukturen kan man se i dokumentasjonen her: 
https://python-poetry.org/docs/basic-usage/

Lag nå en lik struktur på prosjektet som er foreslått her. Prosjektet vårt inneholder også noen data-filer, som gjerne kan legges i en egen mappe. Prosjektet vil da bli seende slik ut: 

<img width="600" alt="image" src="https://github.com/joaolsbe/BE-python/assets/104839676/7684d53a-0d1d-4e49-b784-5086530c27fb">

La oss nå kikke på analysis.py. Gule streker på pakkene polars og dotenv betyr at dette er pakker vi ikkje har installert. Vi installerer disse gjennom poetry:

```
poetry add polars
```

Legg merke til at `pyproject.toml` oppdateres med nye dependencies, og at det genereres ei fil som heiter `poetry.lock`. Denne inneholder pakkeversjoner, og hjelper oss å sørge for at alle som jobber på et prosjekt bruker samme versjoner. Denne skal derfor inn i versjonskontroll. 

Vi skal nå kunne kjøre koden i analysis.py.

Til slutt skal vi prøve å bygge prosjektet vårt. Dette kan gjøres ved å kjøre

```
poetry build
```

Da vil prosjektet bli bygd, og en wheel-fil vil dukke opp under mappen `./dist/`. Dette er en fullverdig python-modul, og hvis du ønsker å pakketere og gjenbruke din egen kode så kan denne installeres via 

```
pip install ".../bepythonjo-0.1.0-py3-none-any.whl"
```

Les meir om poetry her: 

https://python-poetry.org/

Før vi går videre skal vi også legge til linting og auto-formattering. Gå til extensions i vscode og installer "flake8". Hvis du nå går til analysis.py så skal det dukke opp gule/røde linjer der flake8 meiner koden har strukturelle feil. Hold over streker for å sjå kva den klager på. 

Installer så extension "Black Formatter". Opprett så en mappe som heter `.vscode`, og ei fil som heiter `settings.json`. Her putter du følgende:

```
{
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
}
```

Den første linja gjør at vi bruker "black" som formatterer, og at vi automatisk formatterer når vi lagrer. Hvis du nå går til `analysis.py` og lagrer fila, så vil du sjå at den automatisk formatteres av "black". 

Gå nå videre til Part-3-typing
