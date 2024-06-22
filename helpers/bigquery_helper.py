from google.cloud import bigquery


class BigQueryHelper:
    D_WRITE_DISP = bigquery.WriteDisposition.WRITE_TRUNCATE
    D_CREATE_DISP = bigquery.CreateDisposition.CREATE_IF_NEEDED

    def __init__(self, project_id: str) -> None:
        self._project_id = project_id
        self._client = bigquery.Client(project=self._project_id)

    def _execute_query(self, query: str):
        self._client.query(query).result()

    def _build_table(self, table_id, schema, expire=None):
        table = bigquery.Table(table_id, schema=schema)
        if expire is not None:
            table.expires = expire
        self._client.create_table(table)

    def write_table(self, df, table_id, wdisp=None, cdisp=None):
        job_config = bigquery.LoadJobConfig(
            # schema=schema,
            write_disposition=self.D_WRITE_DISP if wdisp is None else wdisp,
            create_disposition=self.D_CREATE_DISP if cdisp is None else cdisp
        )

        job = self._client.load_table_from_dataframe(df,
                                                     destination=f"{self._project_id}.{table_id}",
                                                     job_config=job_config)
        job.result()

    def _get_table(self, table_id):
        return self._client.get_table(table_id)

    def _delete_table(self, table_id: str):
        self._client.delete_table(table_id, not_found_ok=True)
