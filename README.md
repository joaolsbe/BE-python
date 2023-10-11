# Del 3 - typing

Type hints er din venn!

Argumenter kan gis typer ved å legge til `: type` etter argumentet, mens return-typen til ein funksjon gis ved å skrive ` -> type`:

```
def func(arg1: str, arg2: list[str], arg3: dict[str, int], arg4: pl.DataFrame) -> pl.DataFrame:
    ....
```

Bruk det, **alltid**!

Man kan også gi typer ved variabeldefinisjon (self om dette ofte er unødvendig):

```
number: int = 60
```
