from helpers.bigquery_helper import BigQueryHelper
from helpers.bucket_helper import BucketHelper
from helpers.config_helper import ConfigFileHelper
from helpers.utils import get_download_ids, get_data
from core.etl_data import process_data


def main():
    # object instances
    confighelper = ConfigFileHelper()
    params = confighelper.get_config("prod")
    bqhelper = BigQueryHelper(project_id=params.get("project_id"))
    buckethelper = BucketHelper(project_id=params.get("project_id"))

    # data ingestion
    ids = get_download_ids()
    data = get_data(ids)

    # writing data to bucket
    buckethelper.create_bucket(params.get("bucket_name"))
    for df in data:
        buckethelper.write_file(data=df.get("data"),
                                file_name=f"{df.get('id')}.csv",
                                bucket_name=params.get("bucket_name"))

    df_clean = process_data(data)

    bqhelper.write_table(df=df_clean,
                         table_id=f"{params.get('dataset_name')}.{params.get('table_name')}")


if __name__ == '__main__':
    main()
