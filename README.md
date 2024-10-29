# Del 2 - Tools og linting

Vi skal nå sette opp prosjektet vårt til å bruke "tools", av typen linting. Tools er ein generell samlebetegnelse på nyttige verktøy for oss som utviklere. I dette kurset skal vi kun jobbe med ett, nemlig "ruff". Dette er eit formateringsverktøy (linting) som hjelper oss å skrive ryddig kode.

For den beste opplevelsen her bør det installeres inn i kodevertøyet vi jobber i (VSCode). Gå til "extensions" og installer "ruff". 

Deretter må vi konfigurere prosjektet til å bruke verktøyet. Legg til følgende i pyproject.toml:

```
[tool.ruff.lint]
select = [
    # pycodestyle
    "E",
    # Pyflakes
    "F",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-simplify
    "SIM",
    # isort
    "I",
]
```

Dette er et sett med standard-innstillinger som ofte brukes i python, og kan være et godt utganspunkt. Men her er det mange flere ting som kan legges til dersom man ønsker "strengere" kodestandard. Gå nå til `analysis.py` så vil du se at ruff er på jobb og highlighter (i gult) ting som bryter med innstillingene over. 

Dersom vi no ynskjer å fikse problemene så er det fleire måtar å gjere det på. Ruff er tilgjengelig som verktøy blant anna gjennom `uv`, og kode kan formatteres ved å køyre

```
uvx ruff format
```

Du kan også kjøre det gjennom vscode ved å trykke `CTRL+Shift+P`, søke "ruff", og velge "Ruff: Fix all auto-fixable problems".

Men det beste alternativet er kanskje å legge til i innstillingene til vscode slik at ruff kjører auto-formattering hver gang man lagrer. Dette kan gjøres ved å opprette fila `.vscode/settings.json` og kopiere inn følgjende innhold: 

```
{
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "charliermarsh.ruff"
    }
}
```

Fra no av vil ruff sørge for at koden vår alltid følgjer vanlige konvensjonar. 

Tools kan også settes til å kjøre hver gang man committer code (gjennom pre-commit), og det er vanlig praksis å enforce kjøring av tools i pipeline før man deployer kode. Vi skal dog ikkje sette opp dette i dette kurset, ettersom det i større grad henger sammen med git/cicd (man kan også ha pre-commit i terraform-prosjekter for eksempel).

Gå no vidare til part-3-typing