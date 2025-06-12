import azure.functions as func
import datetime
import json
import logging
import os
from azure.data.tables import TableServiceClient, TableClient, UpdateMode

app = func.FunctionApp()

@app.route(route="counterfunction", auth_level=func.AuthLevel.ANONYMOUS)
def counterfunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    connection_string = os.environ["CUSTOMCONNSTR_tableconnect"]
    my_filter = "PartitionKey eq 'counter' and RowKey eq 'counter'"
    table_client = TableClient.from_connection_string(conn_str=connection_string, table_name="countertable")
    entity = table_client.get_entity(row_key="counter", partition_key="counter")
    updated_num = entity['hits'] + 1
    updated_table = {
        "PartitionKey": "counter",
        "RowKey": "counter",
        "hits": updated_num
    }
    table_client.upsert_entity(mode=UpdateMode.REPLACE, entity=updated_table)
    return func.HttpResponse(f"Current number of visitors: {updated_num}")