from flask import Flask, render_template, request
from oauth import CasdoorSDK
app = Flask(__name__)


# These global variables are here only for demo purpose, please
# use a safer method to keep them in production environment.

# e.g. http://localhost:7001
FRONTEND_ENDPOINT = "PLACEHOLDER"

# e.g. http://localhost:8000
BACKEND_ENDPOINT = "PLACEHOLDER"

# Your client_id for the app
CLIENT_ID = "PLACEHOLDER"

# Your client_secret for the app
CLIENT_SECRET = "PLACEHOLDER"

# This is the default secret, leave it unchanged.
JWT_SECRET = "CasdoorSecret"

# This is the organization name, will only be used during users operation, leave it
# unchanged if you don't have to do users operation
ORG_NAME = "PLACEHOLDER"

# Initialize the SDK instance
ExampleSDK = CasdoorSDK(endpoint=BACKEND_ENDPOINT,
                        client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        jwt_secret=JWT_SECRET,
                        org_name=ORG_NAME)


@app.route("/")
def main():
    # redirect_uri is usually set to a callback function, leave it unchanged to
    # use default demo callback()
    redirect_uri = "http://localhost:5000/callback"

    # Please go to Applications tab in Casdoor and put your Application's name into state.
    state = "app-built-in"

    authorization_link = ExampleSDK.get_auth_link(redirect_uri, state)

    return render_template("main.html", auth_link=authorization_link)


@app.route("/callback", methods=["GET"])
def callback():
    code = request.values["code"]
    state = request.values["state"]

    auth_token = ExampleSDK.get_oauth_token(code)
    result = ExampleSDK.parse_jwt_token(auth_token)

    return render_template("success.html", result=result)
