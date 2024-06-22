import pandas as pd
from google.cloud import storage
from google.api_core.exceptions import Conflict

class BucketHelper:
    def __init__(self, project_id: str) -> None:
        self._project_id = project_id
        self._client = storage.Client(project=self._project_id)

    def _get_blob(self, bucket_name: str, file_name: str):
        bucket = self._client.bucket(bucket_name)
        return bucket, bucket.blob(file_name)

    def create_bucket(self, bucket_name: str):
        try:
            self._client.create_bucket(bucket_name)
        except Conflict:
            print("Bucket already exists")

    def read_file(self, file_name: str, bucket_name: str):
        _, blob = self._get_blob(bucket_name, file_name)
        return blob.download_as_bytes()

    def write_file(self, data: pd.DataFrame, file_name: str, bucket_name: str):
        _, blob = self._get_blob(bucket_name, file_name)
        blob.upload_from_string(data.to_csv(), 'text/csv')
