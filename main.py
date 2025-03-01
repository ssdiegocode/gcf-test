import functions_framework
import requests
from requests.structures import CaseInsensitiveDict

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using make_response
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    print("This script is running")
    url = "https://hooks.slack.com/services/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"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = '{"text":"Github code commited - From the second function"}'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
