import pandas as pd
import requests as re
import json
import os
import sys
# curl 'https://bootstrap.pypa.io/get-pip.py' > get-pip.py && sudo python3 get-pip.py
# Article search API page: https://developer.nytimes.com/docs/articlesearch-product/1/routes/articlesearch.json/get

class ConsolidateAPIResponse:
    '''
    A function that makes a 'test' call to the NYT API. If this fails, then quit the program, as there
    is no need to continue.
    '''
    def test_api_conn(API_KEY): 
        test_call = re.get("https://api.nytimes.com/svc/topstories/v2/home.json?api-key={}".format(API_KEY))
        print(test_call.status_code)

        # We only want to proceed IF we get a successful api call
        if test_call.status_code == 200:
            status = 0
            get_articles = ConsolidateAPIResponse.grab_articles(API_KEY)

        # Quit if there are issues connecting, this may be key-related
        else:
            status = 1
            print("Status code of ", test_call.status_code, "\nQuiting...")
            sys.exit()
        
        return status

    '''
    A function that calls the Article Search API and grabs the 10 most recent results for the month of 
    April 2023
    '''
    def grab_articles(API_KEY):

        # Call theb api with our specified parameters
        get_data = re.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=facet=true&begin_date=20230401&end_date=20230430&sort=newest&api-key={}".format(API_KEY))
        
        # Convert api response to json format
        api_response_json = get_data.json()

        # Format the json to be visually pleasing 
        json_response_formatted = json.dumps(api_response_json, indent=2)
        print(json_response_formatted)

