import polars as pl

from be_python import COL
from be_python.transform import agg_by_bins, bin, get_top_n
from be_python.zipdb import ZipDb

db = ZipDb()
df = db.read("most_played_songs")

print("Sample stream data")
print(df)
print(df.columns)


def analysis1_getMostStreamedSongs(df: pl.DataFrame) -> pl.DataFrame:
    df = get_top_n(df, COL.streams, 5)
    df = df.select(COL.track_name, COL.artist_name, COL.streams)
    print(df)


def analysis2_getMostPopularByBPM(df: pl.DataFrame):
    df = agg_by_bins(df, by=COL.bpm, col=COL.streams, agg=pl.mean, n_bins=20)
    df = get_top_n(df, COL.agg_streams, 5)
    print(df)


def analysis3_getDanceability_ByBin(df: pl.DataFrame):
    df = agg_by_bins(df, by=COL.bpm, col=COL.danceability, agg=pl.mean, n_bins=20)
    df = get_top_n(df, COL.agg_danceability, 5)
    print(df)


def analysis4_getTop30SongsBy(df: pl.DataFrame):
    df = bin(df, by=COL.bpm, n_bins=20)
    df = df.filter(pl.col(COL.bpm_bin) == "(104, 108]")
    df = get_top_n(df, COL.streams, 30)
    df = df.select(COL.track_name, COL.artist_name, COL.streams)
    print(df)


print("\n\n\n5 most streamed songs:")
analysis1_getMostStreamedSongs(df)

print("\n\n\nMost popular BPMs")
analysis2_getMostPopularByBPM(df)

print("\n\n\nMost danceable BPMs")
analysis3_getDanceability_ByBin(df)

print("\n\n\nMost popular songs within most danceable BPM")
analysis4_getTop30SongsBy(df)

df = db.read("users")

print("\n\n\nSample user data")
print(df)
print(df.columns)


def analysis5_GetUserAgesCount(df: pl.DataFrame):
    df = agg_by_bins(
        df,
        by=COL.age,
        col=COL.user_id,
        agg=pl.count,
        bins=[20, 30, 40, 50, 60],
    )
    df = get_top_n(df, COL.agg_user_id, 5)
    print(df)


print("\n\n\nMost popular age bins")
analysis5_GetUserAgesCount(df)
