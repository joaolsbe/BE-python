import polars as pl

from be_python.transform import agg_by_bins, get_top_n


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


def test_agg_by_bins():
    df = pl.DataFrame(
        {
            "bpm": [119, 120, 121, 99, 100, 101, 79, 80, 81],
            "age": [10, 20, 30, 40, 50, 60, 70, 80, 90],
        }
    )
    df = agg_by_bins(df, by="age", col="bpm", agg=pl.mean, bins=[35, 65])
    d = df.to_dicts()

    assert d[0]["age_binned"] == "(-inf, 35]"
    assert d[0]["agg_bpm"] == 120.0
    assert d[1]["age_binned"] == "(35, 65]"
    assert d[1]["agg_bpm"] == 100.0
    assert d[2]["age_binned"] == "(65, inf]"
    assert d[2]["agg_bpm"] == 80.0
