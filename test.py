#!/bin/python3
from client import ElasticEDRClient


#"alert.attributes.name:DLL" 

client = ElasticEDRClient()

desired_output = ["description", "query"]

print(client.list_all_rules(desired_output, "alert.attributes.name:DLL"))

