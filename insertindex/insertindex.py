import glob
import json
from opensearchpy import OpenSearch
import sys

jsonl_files = glob.glob("jawiki.json/**/wiki_*")

index_name = 'tokenize-memory-test'


host = 'localhost'
port = 9200

client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True,
    use_ssl = False,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False
)

id=1

for jsonl_file in jsonl_files:
    with open(jsonl_file, 'r') as file:
        for line in file:
            try:
                wikiObj = json.loads(line)
                document = {
                    'title': wikiObj['title'],
                    'text': wikiObj['text'],
                }
                response = client.index(
                    index = index_name,
                    body = document,
                    id = id,
                    refresh = False
                )
                print(wikiObj['title'])
                id += 1
                if id > 21:
                    sys.exit()
            except json.JSONDecodeError:
                print("invalid json")