import polars as pl
from zipfile import ZipFile


class ZipDb:
    def __init__(self, table_name: str) -> None:
        # Attributt
        self.table_name = table_name

    # Metode
    def read(self) -> pl.DataFrame:
        with ZipFile(f"database/{self.table_name}.zip", "r") as zip:
            filename = zip.filelist[0].filename
            f = zip.read(filename)
            return pl.read_csv(f, separator=",", encoding="ISO-8859-1")


class MostPlayedSongs(ZipDb):
    def __init__(self):
        super().__init__(table_name="most_played_songs")

    def get_most_streamed_songs(self) -> pl.DataFrame:
        df = self.read()
        df = (
            df.select("track_name", "artist(s)_name", "streams")
            .sort("streams", descending=True)
            .limit(5)
        )
        return df

    def qbin(self, df: pl.DataFrame, colname: str, num_bins: int):
        return df.filter(pl.col(colname).is_not_nan()).with_columns(
            pl.col(colname).qcut(num_bins).alias(f"{colname}Bin")
        )

    def analysis2_getMostPopularByBPM(self) -> pl.DataFrame:
        df = self.read()
        df = self.qbin(df, "bpm", 20)
        df_Binned = df_Binned.group_by("BPMBin").agg(
            pl.mean("streams").alias("AverageStreams")
        )
        df_Binned = df_Binned.sort("AverageStreams", descending=True).limit(5)
        return df

    def analysis3_getDanceability_ByBin(self) -> pl.DataFrame:
        df = self.read()
        df = self.qbin(df, "bpm", 20)
        df_Binned = df_Binned.group_by("BPMBin").agg(
            pl.mean("danceability_%").alias("AverageDanceability")
        )
        df_Binned = df_Binned.sort("AverageDanceability", descending=True).limit(5)
        return df


myclass = MostPlayedSongs()
df = myclass.read()

print(df)
