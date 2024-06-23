import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'url'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'password'),
    'database_id': os.environ.get('COSMOS_DATABASE', 'People'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Item')
}