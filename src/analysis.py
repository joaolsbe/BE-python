import polars as pl
from zipfile import ZipFile


with ZipFile("database/most_played_songs.zip", 'r') as zip:
    filename = zip.filelist[0].filename
    f = zip.read(filename)
    df = pl.read_csv(f, separator=",", encoding='ISO-8859-1')

print("Sample stream data") 
print(df)
print(df.columns)



def analysis1_getMostStreamedSongs(df):
    df = df.select("track_name", "artist(s)_name", "streams").sort("streams", descending=True).limit(5)
    print(df)


def analysis2_getMostPopularByBPM(df):
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(pl.col("bpm").qcut(20).alias("bpm_binned"))
    df_Binned = df_Binned.group_by("bpm_binned").agg(pl.mean("streams").alias("agg_streams"))
    df_Binned = df_Binned.sort("agg_streams", descending=True).limit(5)
    print(df_Binned)


def analysis3_getDanceability_ByBin(df):
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(pl.col("bpm").qcut(20).alias("bpm_binned"))
    df_Binned = df_Binned.group_by("bpm_binned").agg(pl.mean("danceability_%").alias("agg_danceability_%"))
    df_Binned = df_Binned.sort("agg_danceability_%", descending=True).limit(5)
    print(df_Binned)

def analysis4_getTop30SongsBy(df):
    df_Binned = df.filter(pl.col("bpm").is_not_nan()).with_columns(pl.col("bpm").qcut(20).alias("bpm_binned"))
    df_best_bpm = df_Binned.filter(pl.col("bpm_binned") == "(104, 108]")
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


with ZipFile("database/users.zip", 'r') as zip:
    filename = zip.filelist[0].filename
    f = zip.read(filename)
    df = pl.read_csv(f, separator=",", encoding='ISO-8859-1')


print("\n\n\nSample user data")
print(df)
print(df.columns)

def analysis5_GetUserAgesCount(df):
    df_Binned = df.filter(pl.col("Age").is_not_nan()).with_columns(pl.col("Age").cut([20, 30, 40, 50, 60]).alias("Age_binned"))
    df_Grouped = df_Binned.group_by("Age_binned").agg(pl.col("User ID").count().alias("agg_User ID"))
    df_Binned = df_Grouped.sort("agg_User ID", descending=True).limit(5)
    df = df_Binned
    print(df_Binned)


print("\n\n\nMost popular age bins")
analysis5_GetUserAgesCount(df)