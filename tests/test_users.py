from bepythonjo.analysis import analysis5_GetUserAgesCount
from zipfile import ZipFile
import polars as pl


def test_user_ages():
    with ZipFile("database/users.zip", "r") as zip:
        filename = zip.filelist[0].filename
        f = zip.read(filename)
        df = pl.read_csv(f, separator=",", encoding="ISO-8859-1")

    df = analysis5_GetUserAgesCount(df)
    print(df)
    d = df.to_dicts()

    assert d[0]["AgeBin"] == "(30, 40]"
    assert d[0]["NumUsers"] == 1007

    assert d[1]["AgeBin"] == "(40, 50]"
    assert d[1]["NumUsers"] == 977

    assert d[2]["AgeBin"] == "(20, 30]"
    assert d[2]["NumUsers"] == 423

    assert d[3]["AgeBin"] == "(50, 60]"
    assert d[3]["NumUsers"] == 93
