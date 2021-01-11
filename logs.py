import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

# TODO: replace the all-zero GUID with your instrumentation key.
inst_key = config.settings['logs_ins_key']
conn_string = 'InstrumentationKey='+inst_key
logger.addHandler(AzureLogHandler(
    connection_string=conn_string)
)

def valuePrompt():
    line = input("Enter a value: ")
    logger.warning(line)

def main():
    while True:
        valuePrompt()

if __name__ == "__main__":
    main()
