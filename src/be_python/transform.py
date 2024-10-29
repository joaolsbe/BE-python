from collections.abc import Callable

import polars as pl


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


def agg_by_bins(
    df: pl.DataFrame,
    by: str,
    col: str,
    agg: Callable[[str], pl.Expr],
    bins: list[int] | None = None,
    n_bins: int | None = None,
) -> pl.DataFrame:
    df = bin(df, by, bins, n_bins)
    return df.group_by(f"{by}_binned").agg(agg(col).alias(f"agg_{col}"))
