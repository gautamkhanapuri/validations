import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import config
import uuid
import json


HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']


def create_items(container, partition):
    print('\nCreating Items\n')
    with open("relations.json") as f:
        txt = f.read()
        data = json.loads(txt)
    if data:
        for obj in data:
            obj["id"] = str(uuid.uuid1())
            # obj['partitionKey'] = partition
            container.create_item(body=obj)


def read_items(container):
    dataids = []
    print('\nReading all items in a container\n')
    item_list = list(container.read_all_items())
    print(f'Found {len(item_list)} items')
    for doc in item_list:
        dataids.append(doc.get("id"))
        print(f'Item Id: {doc.get("id")}')
        print(doc)
    return dataids


def query_by_name(container, name):
    print('\nQuerying for a Person by name\n')
    if name:
        items = list(container.query_items(
            query="SELECT * FROM r WHERE r.name=@name",
            parameters=[
                { "name":"@name", "value": name }
            ]
        ))
        print(f'Item queried by name {json.dumps(items, indent=2)}')


def delete_item(container, doc_id, partition):
    print(f'\nDeleting Item by Id: {doc_id}\n')
    response = container.delete_item(doc_id,'')
    print(f'Deleted item\'s Id is {doc_id}')


def upsert_item(container, doc_id):
    print('\nUpserting an item\n')
    rd_item = container.read_item(item=doc_id)
    rd_item['name'] = "xyz"
    response = container.upsert_item(body=rd_item)
    print(f'Upserted Item\'s Id is {response["id"]}, new subtotal={response["name"]}')


def main():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
    try:
        db = client.get_database_client(database=DATABASE_ID)
        print('Database with id \'{0}\' created'.format(DATABASE_ID))

        container = db.get_container_client(CONTAINER_ID)
        print('Container with id \'{0}\' created'.format(CONTAINER_ID))

        create_items(container, "name")
        # read_item(container, 'name')
        data_ids = read_items(container)
        query_by_name(container, 'sl shetty')
        # replace_item(container, 'SalesOrder1', 'Account1')
        # upsert_item(container, 'SalesOrder1', 'Account1')
        try:
            delete_item(container, data_ids[-1], "name")
        except:
            print("Error in delete")
    except exceptions.CosmosHttpResponseError as e:
        print('\nrun_sample has caught an error. {0}'.format(e.message))

    finally:
            print("\nrun_sample done")


if __name__ == '__main__':
    main()