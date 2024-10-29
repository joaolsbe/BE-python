# Del 3 - typing

Type hints er din venn!

Argumenter kan gis typer ved å legge til `: type` etter argumentet, mens return-typen til ein funksjon gis ved å skrive ` -> type`:

```
def func(arg1: str, arg2: list[str], arg3: dict[str, int], arg4: pl.DataFrame) -> pl.DataFrame:
    ....
```

Bruk det, **alltid**! Legg merke til at når du legger til riktig typer i funksjoner så får du med deg autocompletion og andre nyttige eigenskaper.

Man kan også gi typer ved variabeldefinisjon (self om dette generelt er unødvendig):

```
number: int = 60
```

### Oppgave:

- Implementer typing i alle funksjoner.

Et annet triks her kan være å introdusere variabler for kolonnenavn. Det kan kanskje oppleves overkill for mange, men fordelene er at man får auto-completion her også, du slipper å huske hvordan man skriver de ulike navnene, og kanskje viktigst av alt, aldri meir skrivefeil på kolonnenavn. 

Et annet tips: Tenk gjenbruk i alt. Dersom du begynner å utvikle logikk som kan være nyttig for andre, så er det på tide å modularisere det og gjøre det gjenbrukbart. Se neste steg for et eksempel på hvordan det kan se ut.
