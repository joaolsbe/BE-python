# Del 1 - virtual environments

Velkommen til koden. Her finnes det bare ei py-fil, `analysis.py`.

Denne kan kjøres ved å skrive `python analysis.py` i terminal. Men hvis vi kjører denne uten videre så vil du få følgende feilmelding: 

```
Traceback (most recent call last):
  File "C:\Users\joakim.olsen\Documents\git\BE-python\BE-python\analysis.py", line 1, in <module>
    import polars as pl
ModuleNotFoundError: No module named 'polars'
```

Vi må altså installere pakken polars. Men, dette skal vi gjøre i et virtuelt python-miljø. Det finnes ulike måter å gjøre dette på, men her skal vi bruke python sin innebygde venv. Et nytt virtuelt miljø kan lages ved: 

```
python -m venv .venv
```

Vi må så velge å bruke det nye virtuelle miljøet. Velg CTRL+Shift+P, og søk opp "Python: Select interpreter". Velg det nye virtuelle miljøet (.venv). 

