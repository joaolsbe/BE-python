from zipfile import ZipFile

import polars as pl

from be_python import COL

with ZipFile("database/most_played_songs.zip", "r") as zip:
    filename = zip.filelist[0].filename
    f = zip.read(filename)
    df = pl.read_csv(f, separator=",", encoding="ISO-8859-1")

print("Sample stream data")
print(df)
print(df.columns)


def analysis1_getMostStreamedSongs(df: pl.DataFrame) -> None:
    df = (
        df.select(COL.track_name, COL.artist_name, COL.streams)
        .sort(COL.streams, descending=True)
        .limit(5)
    )
    print(df)


def analysis2_getMostPopularByBPM(df: pl.DataFrame):
    df_Binned = df.filter(pl.col(COL.bpm).is_not_nan()).with_columns(
        pl.col(COL.bpm).qcut(20).alias(COL.bpm_bin)
    )
    df_Binned = df_Binned.group_by(COL.bpm_bin).agg(
        pl.mean(COL.streams).alias(COL.agg_streams)
    )
    df_Binned = df_Binned.sort(COL.agg_streams, descending=True).limit(5)
    print(df_Binned)


def analysis3_getDanceability_ByBin(df: pl.DataFrame) -> None:
    df_Binned = df.filter(pl.col(COL.bpm).is_not_nan()).with_columns(
        pl.col(COL.bpm).qcut(20).alias(COL.bpm_bin)
    )
    df_Binned = df_Binned.group_by(COL.bpm_bin).agg(
        pl.mean(COL.danceability).alias(COL.agg_danceability)
    )
    df_Binned = df_Binned.sort(COL.agg_danceability, descending=True).limit(5)
    print(df_Binned)


def analysis4_getTop30SongsBy(df: pl.DataFrame) -> None:
    df_Binned = df.filter(pl.col(COL.bpm).is_not_nan()).with_columns(
        pl.col(COL.bpm).qcut(20).alias(COL.bpm_bin)
    )
    df_best_bpm = df_Binned.filter(pl.col(COL.bpm_bin) == "(104, 108]")
    df_most_popular = (
        df_best_bpm.select(COL.track_name, COL.artist_name, COL.streams)
        .sort(COL.streams, descending=True)
        .limit(30)
    )
    print(df_most_popular)


print("\n\n\n5 most streamed songs:")
analysis1_getMostStreamedSongs(df)

print("\n\n\nMost popular BPMs")
analysis2_getMostPopularByBPM(df)

print("\n\n\nMost danceable BPMs")
analysis3_getDanceability_ByBin(df)

print("\n\n\nMost popular songs within most danceable BPM")
analysis4_getTop30SongsBy(df)


with ZipFile("database/users.zip", "r") as zip:
    filename = zip.filelist[0].filename
    f = zip.read(filename)
    df = pl.read_csv(f, separator=",", encoding="ISO-8859-1")


print("\n\n\nSample user data")
print(df)
print(df.columns)


def analysis5_GetUserAgesCount(df: pl.DataFrame) -> None:
    df_Binned = df.filter(pl.col(COL.age).is_not_nan()).with_columns(
        pl.col(COL.age).cut([20, 30, 40, 50, 60]).alias(COL.age_bin)
    )
    df_Grouped = df_Binned.group_by(COL.age_bin).agg(
        pl.col(COL.user_id).count().alias(COL.agg_user_id)
    )
    df_Binned = df_Grouped.sort(COL.agg_user_id, descending=True).limit(5)
    df = df_Binned
    print(df_Binned)


print("\n\n\nMost popular age bins")
analysis5_GetUserAgesCount(df)
