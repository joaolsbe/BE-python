# Del 4 - testing

Det er god praksis å skrive tester når man utvikler. Innenfor software-utvikling er det nærmest obligatorisk, mens innenfor data engineering og data science er det ganske få som gjør det. Her kan vi gå foran med et godt eksempel, særlig i python, hvor det er enkelt å drive med testing. 

Vi skal nå bruke pytest. Vi legger først pakken til i prosjektet som ein development dependency. Dette er fordi vi ikkje trenger denne pakken for å kjøre koden (i et eventuelt kjøremiljø), men ønsker å ha det under utvikling.

```
uv add --dev pytest
```

Når pytest skal kjøre tester så leiter den etter filer med navn `test_*.py`, og funksjoner som heiter `test_*`. Vi lager tester ved å importere og kjøre funksjonen vi ønsker å teste, og så "asserte" at resultatet er som vi forventer. 

Før vi kan begynne å teste, så må vi finne ut hva vi ønsker å teste. Måten vi har skrevet koden på per nå inviterer veldig lite til gjenbruk og testing. Et av målene med å jobbe test-drevet er også at vi skal ende opp med å skrive ryddigere og gjenbrukbar kode, og bare ved å spørre oss spørsmålet "hva trenger vi egentlig å teste her" så endrer det kanskje måten vi koder på. I koden vi har skrevet per nå så er det ein del transformasjoner som går igjen, som vi både har interesse av å kunne gjenbruke og å kunne teste. 

Vi refakturerer nå koden vår ved å implementere funksjonene `get_top_n(df, by, n)` og `bin(df, by, bins, n_bins)`:

```
def get_top_n(df: pl.DataFrame, by: str, n: int) -> pl.DataFrame:
    return df.sort(by, descending=True).limit(n)

def bin(
    df: pl.DataFrame, by: str, bins: list[int] | None = None, n_bins: int | None = None
) -> pl.DataFrame:
    if bins is not None:
        col = pl.col(by).cut(bins)
    elif n_bins is not None:
        col = pl.col(by).qcut(n_bins)
    else:
        raise Exception("Either bins or n_bins must be set")

    return df.filter(pl.col(by).is_not_nan()).with_columns(col.alias(f"{by}_binned"))
```

Dette er generelle transformasjoner som vi ser i koden vår at vi har en tendens til å gjenbruke. Det kan diskuteres om det er så verdifullt å generalisere disse, men ein annen fordel med å gjøre det er at vi lager kode som er mye enklere å teste. Vi implementerer vår første test, ved å lage fila `tests/test_transform.py`, og legger inn følgende kode: 

```
import polars as pl

from be_python.transform import get_top_n


def test_get_top_n():
    df = pl.DataFrame({"id": [1, 2, 3, 4, 5], "number": [27, 3, -1, 42, 111]})
    df = get_top_n(df, by="number", n=3)
    d = df.to_dicts()

    assert d[0]["id"] == 5
    assert d[0]["number"] == 111
    assert d[1]["id"] == 4
    assert d[1]["number"] == 42
    assert d[2]["id"] == 1
    assert d[2]["number"] == 27
```

Denne testen kan nå kjøres ved å kjøre 

```
pytest tests/
```

### Oppgave:

Det er ein transformasjon til som gjenbrukes fleire steder, og som derfor kan være nyttig å implementere og teste. Implementer funksjonen 

```
def agg_by_bins(
    df: pl.DataFrame,
    by: str,
    col: str,
    agg: Callable[[str], pl.Expr],
    bins: list[int] | None = None,
    n_bins: int | None = None,
) -> pl.DataFrame:
```

Skriv så en test for denne. 