import ssl
from requests_oauthlib import OAuth1Session

import params as par


def get_oauth1_token():
    oauth = OAuth1Session(par.TW_OAUTH1_CLIENT, client_secret=par.TW_OAUTH1_SECRET)

    try:
        fetch_response = oauth.fetch_request_token(par.TW_REQUEST_TOKEN_URL)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    authorization_url = oauth.authorization_url(par.TW_BASE_AUTHORIZATION_URL)
    print("Please go here and authorize: %s" % authorization_url)
    verifier = input("Paste the PIN here: ")    

    oauth = OAuth1Session(
        par.TW_OAUTH1_CLIENT,
        client_secret=par.TW_OAUTH1_SECRET,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(par.TW_ACCESS_TOKEN_URL)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    return access_token, access_token_secret


def create_oauth1_session(access_token, access_token_secret):
    oauth = OAuth1Session(
        par.TW_OAUTH1_CLIENT,
        client_secret=par.TW_OAUTH1_SECRET,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    return oauth


def main():
    access_token, access_token_secret = get_oauth1_token()

    oauth = create_oauth1_session(access_token, access_token_secret)

    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json={'text': 'Hello World!'},
    )

    print(response.json())


if __name__ == '__main__':
    main()