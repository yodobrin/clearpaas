import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', '[COSMOS ENDPOINT'),
    'master_key': os.environ.get('ACCOUNT_KEY', '[COSMOS WRITE KEY]'),
    'database_id': os.environ.get('COSMOS_DATABASE', '[DB NAME]'),
    'container_id': os.environ.get('COSMOS_CONTAINER', '[CONTAINER NAME]]'),
    'kv_name': os.environ.get('KV_NAME', '[YOUR KEYVAULT NAME ]'),
    'secret_name': os.environ.get('SECRET_NAME', '[YOUR SECRET]')
}
