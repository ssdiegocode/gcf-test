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
    print("___ This script is running - function 3")
    url = os.getenv('SLACK_URL')
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = '{"text":"___ Github code commited - for function three"}'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    # first test 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11 - 12 - 13 - 14 - 15 - 16 - 17 - 18 - 19 - 20 - 21 - 22
