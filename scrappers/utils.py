import requests

session = requests.Session()


def send_http_request(method, url, params=None, data=None, headers=None):
    response = session.request(method=method, url=url, params=params, data=data, headers=headers)

    if response.status_code == 401:
        # TODO: Send request to home page
        pass

    return response
