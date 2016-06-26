import http.client as httplib
import os

# Create your views here.
from django.http import HttpResponse


class ApiError(Exception):
    pass


def authenticate(request, *args, **kwargs):
    """
    The authentication step is a bit involved. First of all, this app will have
    a client_id and client_secret tied to it. This is to confirm that the
    requests are coming from the right location.

    The user name and passwords are then sent in the header to provided an
    authorization token for the user for this specific instance of the
    application. The token is then saved in the session to avoid this request
    from being made again
    :return: The json
    """
    conn = httplib.HttpConnection("https://webservices.io")

    headers = {"Content-type": "application/json", "Accept": "json"}
    headers["client_secret"] = os.environ.get("client_secret")
    headers["client_key"] = os.environ.get("client_key")
    headers['grant_type'] = "password"
    headers["email"] = request.body.get("email"),
    headers["password"] = request.body.get("password")

    conn.request("GET", "/users", headers=headers)

    response = conn.get_response()
    conn.close()

    if response.status >= 200:

        data = response.read()

        if response.status >= 200 and response.status < 300:
            request.session['auth_token'] = data['access_token']

        return HttpResponse(data, status=response.status)
    else:
        raise ApiError("There was an error ")

    # Assume that whatever come back from the API login is good enough
    return data


def get_details(request, *args, **kwargs):
    """
    This uses the API key that should be placed in the session in the /login
    url. The API key is used to determine what kind of information the user
    has access to. Both on here and on the microservice end.
    
    :param user_id: The id of hte user to search for. Own profile data will
    be returned instead.
    :return:
    """
    conn = httplib.HttpConnection("https://webservices.io")

    user_id = kwargs.get('user_id')
    headers = {"Content-type": "application/json", "Accept": "json"}
    headers['Authrization'] = 'Bearer {0}'.format(request.session[
                                                      'auth_token'])
    headers['grant_type'] = "token"

    if not user_id:
        conn.request("GET", "/users", headers=headers)
    else:
        conn.request("GET", "/users/" + user_id, headers=headers)

    response = conn.get_response()

    data = response.read()

    return data
