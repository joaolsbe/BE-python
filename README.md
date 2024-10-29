# Del 1 - package management

Velkommen til koden. Her finnes det bare ei py-fil, `analysis.py`.

Denne kan kjøres ved å skrive `uv run analysis.py` i terminal. Men hvis vi kjører denne uten videre så vil du få følgende feilmelding: 

```
Traceback (most recent call last):
  File "C:\Users\joakim.olsen\Documents\git\BE-python\BE-python\analysis.py", line 1, in <module>
    import polars as pl
ModuleNotFoundError: No module named 'polars'
```

Dette kan du også sjå dersom du opnar fila `analysis.py`, ved at det er gule strekar under pakken `polars`. 

Vi må altså installere pakken polars. Men, dette **skal** vi alltid gjere i eit virtuelt python-miljø, og det er sterkt anbefalt å bruke eit meir sofistikert verktøy enn pip til å gjøre dette. "Poetry" er i dag det mest utbredte verktøyet, men her skal vi bruke "uv", som er ein ganske ny package manager som fungerer ganske likt, men er raskere og smartere. Vi initierer først prosjektet, som et "library":

```
uv init --lib
```

Det opprettes no ein del greier:
- **`.python-version`**: Fil som kun inneheld kva python-versjon vi skal bruke i prosjektet.
- **`pyproject.toml`**: Spesifikasjon av prosjektet.
- **`src/be_python/__init__.py`**: Eksempel-kode for prosjektet.
- **`src/be_python/py.typed`**: Denne fila er ein markør for "type checkers" som forteller at koden vår bruker typer. Vi kommer meir tilbake til dette seinere i kurset.

Prosjekt-strukturen som settes opp her er typisk for kodeprosjekter, og kan være ein fin struktur å ta utgangspunkt i. Vi kan fjerne eksempel-koden i `src/be_python/__init__.py`, og flytte `analysis.py` inn i mappen `src`.

No kan vi installere pakken som manglar: 

```
uv add polars
```

Fleire filer blir oppretta:
- **`.venv/`**: Mappe for det virtuelle miljøet som høyrer til prosjektet.
- **`uv.lock`**: Avhengigheiter for prosjektet. Tilsvarer ei `requirements.txt`-fil, men manages av `uv`. Denne er det meningen at skal inn i versjonskontroll, slik at alle som jobbar på same prosjekt brukar same versjonar. 

Når vi køyrer denne kommandoen skjer fleire ting:
- Pakken, med ein presis spesifikasjon av sine avhengigheiter, legges til i `uv.lock`.
- Pakken legges til under dependencies i `pyproject.toml`. Her vil den nyeste versjon bli valgt "by default", men vi kunne spesifisert versjon ved å skrive for eksempel `uv add polars==1.12.0`. Her er det også mogleg å modifisere versjoner rett i `pyproject.toml`, men då må du køyre `uv lock` for at lock-fila skal oppdatere seg (det vil også skje automatisk dersom du køyrer f. eks. `uv run ...`).
- Selve python-pakken `polars` installeres inn i det virtuelle miljøet under `.venv`- mappen.

Sørg for å sette VSCode til å bruke det nye miljøet. Dette burde dukke opp som ein boks nede i høgre hjørne, men dersom det ikkje gjer det så kan du klikke `CTRL+Shift+P`/`CMD+Shift+P`, søkje opp "Python: Select interpreter". Velg det nye virtuelle miljøet `(.venv)`. 

Dersom du no opnar ein ny terminal, så skal det nye miljøet automatisk bli valgt. Du vil sjå at det fungerer ved at det står `(be-python)` i terminalen:

<img width="400" alt="image" src="https://github.com/joaolsbe/BE-python/assets/104839676/a165f2e3-107c-496f-a279-9e725263ddcc">

Pakken er no installert, som vil bli synlig ved å gå inn i `analysis.py` og sjå at den gule streken under `polars` no er borte, og referansen til `polars` no har blitt riktig fargelagt. Vi kan også endelig køyre koden vår med suksess: 

```
uv run src/analysis.py
```

Før vi gjer oss heilt ferdig med pakkehandtering, så skal vi også byggje prosjektet vårt. Kjør følgende kommando: 

```
uv build
```

Når denne kommandoen kjøres så bygges prosjektet vårt under `/dist`-mappen, og vi kunne delt koden vår med andre (typisk som `.whl`-fil).


Gå til neste steg (branch): Part-2-tools
