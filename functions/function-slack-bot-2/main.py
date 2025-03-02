import functions_framework
import requests
from requests.structures import CaseInsensitiveDict
import os

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    print("This script is running - function 2")
    url = os.getenv('SLACK_URL')
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = '{"text":"Github code commited - for function two"}'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    #update test - git version
    #update test - git version 2 - 2
