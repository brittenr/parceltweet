import yaml

with open(r"C:\Users\Rolf\Documents\git\parceltweet\config\secret.yaml") as f:
    secret = yaml.safe_load(f)

TW_BEARER = secret['twitter']['bearer']
TW_OAUTH1_CLIENT = secret['twitter']['oauth1_client_id']
TW_OAUTH1_SECRET = secret['twitter']['oauth1_client_secret']

OPENAI_BEARER = secret['openai']['bearer']

TW_REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
TW_BASE_AUTHORIZATION_URL = "https://api.twitter.com/oauth/authorize"
TW_ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"