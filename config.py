import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', '[YOUR ENDPOINT]'),
    'master_key': os.environ.get('ACCOUNT_KEY', '[YOUR KEY]'),
    'database_id': os.environ.get('COSMOS_DATABASE', '[YOUR DATABASE]'),
    'container_id': os.environ.get('COSMOS_CONTAINER', '[YOUR CONTAINER]'),
    'MONGOURL': os.environ.get('MONGOURL', '[YOUR ENDPOINT]'),
    'MONGO_USERNAME': os.environ.get('MONGO_USERNAME', '[YOUR USER NAME]'),
    'MONGO_PASSWORD': os.environ.get('MONGO_PASSWORD', '[YOUR PASSWORD]')
}
