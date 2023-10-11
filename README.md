# Del 4 - testing

Det er god praksis å skrive tester når man utvikler. Innenfor software-utvikling er det nærmest obligatorisk, mens innenfor data engineering og data science er det svært få som gjør det. Her kan vi gå foran med et godt eksempel, særlig i python, hvor det er enkelt å drive med testing. 

Vi skal nå bruke pytest. Vi legger først pakken til i prosjektet som ein development dependency. Dette er fordi vi ikkje trenger denne pakken for å kjøre koden (i et eventuelt kjøremiljø), men ønsker å ha det under utvikling.

```
poetry add pytest -G dev
```

Når pytest skal kjøre tester så leiter den etter filer med navn `test_*.py`, og funksjoner som heiter `test_*`. Vi lager tester ved å importere og kjøre funksjonen vi ønsker å teste, og så "asserte" at resultatet er som vi forventer. Lag ei fil under tests som heiter `test_users.py`, og legg inn følgende test:

```
from bepythonjo.analysis import analysis5_GetUserAgesCount
from zipfile import ZipFile
import polars as pl


def test_user_ages():
    with ZipFile("database/users.zip", "r") as zip:
        filename = zip.filelist[0].filename
        f = zip.read(filename)
        df = pl.read_csv(f, separator=",", encoding="ISO-8859-1")

    df = analysis5_GetUserAgesCount(df)
    d = df.to_dicts()

    assert d[0]["AgeBin"] == "(30, 40]"
    assert d[0]["NumUsers"] == 1007

    assert d[1]["AgeBin"] == "(40, 50]"
    assert d[1]["NumUsers"] == 977

    assert d[2]["AgeBin"] == "(20, 30]"
    assert d[2]["NumUsers"] == 423

    assert d[3]["AgeBin"] == "(50, 60]"
    assert d[3]["NumUsers"] == 93
```

Denne testen kan nå kjøres ved å kjøre 

```
pytest tests/
```

Lag no ein test for "most danceable BPMs". 
