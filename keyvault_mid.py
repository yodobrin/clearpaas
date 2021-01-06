import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import config

keyVaultName = config.settings['kv_name']
MASTER_KEY = config.settings['master_key']

KVUri = 'https://'+keyVaultName+'.vault.azure.net'

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = config.settings['secret_name']

retrieved_secret = client.get_secret(secretName)
print(retrieved_secret)