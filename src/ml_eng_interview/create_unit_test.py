
from abc import abstractmethod
from urllib.error import HTTPError
import pandas as pd
from io import StringIO


class FileDownloader:
    @abstractmethod
    def download_file(self, url: str) -> str:
        """Download a file from the given URL and return the file contents."""
        pass

def simple_process_function(file_downloader: FileDownloader) -> float|None:
    """Use the file downloader to download a file and return its contents."""
    url = "http://example.com/file.txt"
    try:
        csv_string = file_downloader.download_file(url)
    except HTTPError:
        return -1
    csv_data = StringIO(csv_string)
    try:
        df = pd.read_csv(csv_data)
    except pd.errors.EmptyDataError:
        raise ValueError("No data found in the file")
    # return the sum of the first column
    return df.iloc[:, 0].sum()
