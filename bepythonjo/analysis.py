import polars as pl
from .zipdb import ZipDb


myclass = ZipDb(table_name="most_played_songs")
df = myclass.read()

print("Sample stream data")
print(df)
print(df.columns)


def get_most_streamed_songs(df: pl.DataFrame) -> None:
    df = (
        df.select("track_name", "artist(s)_name", "streams")
        .sort("streams", descending=True)
        .limit(5)
    )
    print(df)


def analysis2_getMostPopularByBPM(df: pl.DataFrame) -> None:
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(
        pl.col("bpm").qcut(20).alias("BPMBin")
    )
    df_Binned = df_Binned.group_by("BPMBin").agg(
        pl.mean("streams").alias("AverageStreams")
    )
    df_Binned = df_Binned.sort("AverageStreams", descending=True).limit(5)
    print(df_Binned)


def analysis3_getDanceability_ByBin(df: pl.DataFrame) -> None:
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(
        pl.col("bpm").qcut(20).alias("BPMBin")
    )
    df_Binned = df_Binned.group_by("BPMBin").agg(
        pl.mean("danceability_%").alias("AverageDanceability")
    )
    df_Binned = df_Binned.sort("AverageDanceability", descending=True).limit(5)
    print(df_Binned)


def analysis4_getTop30SongsBy(df: pl.DataFrame) -> None:
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(
        pl.col("bpm").qcut(20).alias("BPMBin")
    )
    df_best_bpm = df_Binned.filter(pl.col("BPMBin") == "(104, 108]")
    df_most_popular = (
        df_best_bpm.select("track_name", "artist(s)_name", "streams")
        .sort("streams", descending=True)
        .limit(30)
    )
    print(df_most_popular)


print("\n\n\n5 most streamed songs:")
get_most_streamed_songs(df)

print("\n\n\nMost popular BPMs")
analysis2_getMostPopularByBPM(df)

print("\n\n\nMost danceable BPMs")
analysis3_getDanceability_ByBin(df)

print("\n\n\nMost popular songs within most danceable BPM")
analysis4_getTop30SongsBy(df)


myclass = ZipDb(table_name="users")
df = myclass.read()


print("\n\n\nSample user data")
print(df)
print(df.columns)


def analysis5_GetUserAgesCount(df: pl.DataFrame) -> pl.DataFrame:
    df_Binned = df.filter(pl.col("Age").is_not_nan()).with_columns(
        pl.col("Age").cut([20, 30, 40, 50, 60]).alias("AgeBin")
    )
    df_Grouped = df_Binned.group_by("AgeBin").agg(
        pl.col("User ID").count().alias("NumUsers")
    )
    df_Binned = df_Grouped.sort("NumUsers", descending=True).limit(5)
    df = df_Binned
    print(df_Binned)
    return df


print("\n\n\nMost popular age bins")
analysis5_GetUserAgesCount(df)
