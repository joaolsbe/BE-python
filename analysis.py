import polars as pl
from zipfile import ZipFile
import os
from dotenv import load_dotenv



with ZipFile("most_played_songs.zip", 'r') as zip:
    load_dotenv()
    password = os.getenv("ZIP_PASSWORD")
    f = zip.read(zip.filelist[0].filename, pwd=bytes(password, encoding="utf8"))
    df = pl.read_csv(f, separator=",", encoding='ISO-8859-1')

print("Sample stream data") 
print(df)
print(df.columns)



def analysis1_getMostStreamedSongs(df):
    df = df.select("track_name", "artist(s)_name", "streams").sort("streams", descending=True).limit(5)
    print(df)


def analysis2_getMostPopularByBPM(df):
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(pl.col("bpm").qcut(20).alias("BPMBin"))
    df_Binned = df_Binned.group_by("BPMBin").agg(pl.mean("streams").alias("AverageStreams"))
    df_Binned = df_Binned.sort("AverageStreams", descending=True).limit(5)
    print(df_Binned)


def analysis3_getDanceability_ByBin(df):
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(pl.col("bpm").qcut(20).alias("BPMBin"))
    df_Binned = df_Binned.group_by("BPMBin").agg(pl.mean("danceability_%").alias("AverageDanceability"))
    df_Binned = df_Binned.sort("AverageDanceability", descending=True).limit(5)
    print(df_Binned)

def analysis4_getTop30SongsBy(df):
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(pl.col("bpm").qcut(20).alias("BPMBin"))
    df_best_bpm = df_Binned.filter(pl.col("BPMBin") == "(104, 108]")
    df_most_popular = df_best_bpm.select("track_name", "artist(s)_name", "streams").sort("streams", descending=True).limit(30)
    print(df_most_popular)


print("\n\n\n5 most streamed songs:")
analysis1_getMostStreamedSongs(df)

print("\n\n\nMost popular BPMs")
analysis2_getMostPopularByBPM(df)

print("\n\n\nMost danceable BPMs")
analysis3_getDanceability_ByBin(df)

print("\n\n\nMost popular songs within most danceable BPM")
analysis4_getTop30SongsBy(df)


with ZipFile("users.zip", 'r') as zip:
    load_dotenv()
    password = os.getenv("ZIP_PASSWORD")
    f = zip.read(zip.filelist[0].filename, pwd=bytes(password, encoding="utf8"))
    df = pl.read_csv(f, separator=",", encoding='ISO-8859-1')


print("\n\n\nSample user data")
print(df)
print(df.columns)

def analysis5_GetUserAgesCount(df):
    df_Binned = df.filter(pl.col("Age").is_not_nan()).with_columns(pl.col("Age").qcut(10).alias("AgeBin"))
    df_Grouped = df_Binned.group_by("AgeBin").agg(pl.col("User ID").count().alias("NumUsers"))
    df_Binned = df_Grouped.sort("NumUsers", descending=True).limit(5)
    df = df_Binned
    print(df_Binned)

analysis5_GetUserAgesCount(df)