from zipfile import ZipFile

import polars as pl


class ZipDb:
    def __init__(self, encoding: str = "ISO-8859-1") -> None:
        # Attributt
        self.encoding = encoding

    # Metode
    def read(self, table: str) -> pl.DataFrame:
        with ZipFile(f"database/{table}.zip", "r") as zip:
            filename = zip.filelist[0].filename
            f = zip.read(filename)
            return pl.read_csv(f, separator=",", encoding=self.encoding)

    def write(self, df: pl.DataFrame, table: str) -> None:
        pass
