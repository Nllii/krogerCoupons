import base64

CLIENT_ID = ""
CLIENT_SECRET = ""

# Get these 3 values from registering your developer account/application with https://developer.kroger.com/
redirect_uri = "https://localhost/8080/ "

# Authentication requires base64 encoded id:secret, which is precalculated here
encoded_client_token = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('ascii')).decode('ascii')
customer_username = ""
customer_password = ""
