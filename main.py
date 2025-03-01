import functions_framework
import requests
from requests.structures import CaseInsensitiveDict

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`.
    """
    print("This script is running")
    
    # Slack webhook URL
    url = "https://hooks.slack.com/services/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"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    # Data to send to Slack
    data = '{"text":"Github code committed"}'
    
    # Send the POST request to Slack
    resp = requests.post(url, headers=headers, data=data)
    
    # Debug: print the status code of the Slack request
    print("Slack response status:", resp.status_code)
    
    # Check if the request was successful
    if resp.status_code == 200:
        return "Message sent to Slack successfully!", 200
    else:
        return f"Failed to send message to Slack. Status code: {resp.status_code}", 500
