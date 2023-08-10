import pandas as pd 
from libraries.consolidate_api_response import ConsolidateAPIResponse
import os

'''
3. Write the code (Python preferred, but any language is acceptable) to access the API
and return the last 10 articles with a pub_date of April 2023

4. Populate a CSV with the following columns from that data set: _id, pub_date,
headline, section_name, word_count, and snippet. Feel free to use a package that
handles csv transformation such as pandas for Python.

5. Clean the CSV by limiting the column containing `snippet` to only contain 50
characters. Simply truncate this data, do not make these values null.

6. Download the CSV. Bonus points for uploading it somewhere like Google Docs!

7. Return an email containing the link to your code on Github and a copy of the cleaned
CSV you generated.
'''


key = os.getenv('NYT_API_KEY')
test_api = ConsolidateAPIResponse.test_api_conn(key)
print(test_api)