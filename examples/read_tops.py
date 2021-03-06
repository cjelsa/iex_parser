from iex_parser import Parser, TOPS_1_6
import logging
import os

logging.basicConfig(level=logging.INFO)

TOPS_SAMPLE_DATA_FILE = os.path.join(os.environ['DATA_FOLDER'], 'data_feeds_20180127_20180127_IEXTP1_TOPS1.6.pcap.gz')

with Parser(TOPS_SAMPLE_DATA_FILE, TOPS_1_6) as reader:
    for message in reader:
        print(message)

print('Done')
