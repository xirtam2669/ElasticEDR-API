#!/bin/python3
import requests
import textwrap

class ElasticEDRClient:
    def __init__(
        self,
    ):
        self.url: str = ""#insert URL
        self.API_key: str = ""#insert api key
        
        self.params: dict = {
        "per_page": 100,  
        "page": 1,
        }
        
        self.headers: dict = {
        "kbn-xsrf": "true",
        "Authorization": "ApiKey " + self.API_key
        }

        self.tags = {}
################################################### OUTPUT FORMATTING ###################################################
    def create_tag_dict(self, rule, key_list):
        #Takes in list of keys to customize output
        #Creats a dictionary of keys, that correspond to formatted values from the response
        self.tags = {"Name": f"Name: {rule['name']}"}
    
        for key in key_list:
            self.tags.update({key: self.wrap_text(rule, key)})
            
    def wrap_text(self, rule, key):
        #Formats output text

        wrapped_text = textwrap.fill(
        rule[key], #text
        width=70,              
        initial_indent=f"\t{key}: \n\t\t     ",
        subsequent_indent="\t\t     "
        )
        return wrapped_text
    
    def enumerate_rule_response(self, rule, keys_list):
        #Crafts output string per rule
        output_string = ""

        self.create_tag_dict(rule, keys_list)

        for key in self.tags:
            output_string += (str(self.tags[key]+'\n'))

        return output_string
###########################################################################################################################

    def list_all_rules(self, keys_list, filter_key=None,):
        request = "detection_engine/rules/_find"
        params = self.params.copy()

        if(not filter_key):
           pass
        else:
            params["filter"] = f"{filter_key}"

        try:
            response = requests.get(self.url + request, headers=self.headers, params=params)
        except Exception as e:
            print(f"ERROR: {e}")

        if response.status_code == 200:
            data = response.json()
            print(f"Rules Found: {data['total']}")
            for rule in data['data']:
                try:
                    print(self.enumerate_rule_response(rule, keys_list))
                except KeyError as e:
                        pass
        else:
            print("Error:", response.status_code)
            print(response.text)
