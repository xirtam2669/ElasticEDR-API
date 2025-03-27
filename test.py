#!/bin/python3
from client import ElasticEDRClient
client = ElasticEDRClient()

desired_output = ["description", "query"]

print(client.list_all_rules(desired_output)

