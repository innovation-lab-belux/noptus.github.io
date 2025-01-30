import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

TYPE = "service_account"
PROJECT_ID = "eusummit2025"
PRIVATE_KEY_ID = "b9534ea18e65f8363e168153d92fd1de22c22868"
PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPZTTJFShDkofu
oRflh+TVp9+cdkaVget6tfC10NSvmr1qlwj5rbYasXOBoRsHJCPGp1xWkbgsbeTf
VCuqi9x2R0f87cC9hRZ4Zs2WZYYv4t2ivckcMw4W/7eQ/SgSrmggsXetcpwsmTPn
pvSLGjxrvFX0Ly+uwuj9igs/bOITNnpgnspOQxT5f/iWAWANw0JBby/ULpFhkJXU
UqC4Z7oa9Dp4umrMtRignqDgmeWO7ZaBoSdTyW0OSG8dL4iDU3lL8DDDMtYf6h5M
0tRLD7dGnMMGNwygbtSia3gYs/8Lec2QufYrC+GnuHsX058pug5WAJ+cymo1bV2g
8iKi/BITAgMBAAECggEARpKc1LQjYGMTaGte81c70kxuthI1UJjGJZqVz3jBdwQD
4qqEflnTNuAdewX0aYitt+KpdDff4RaAJFLDDSTMn18AKxxIUvVfwRbSbJQdhlv/
qWpFbhgdekwIDglnQnwgqMda/yWZ6T80v2Y7nr4Nw2dyJEaORjzDBcucqjeF8p0h
U1ZD7/qlusgyNYmu68K/LahBR1KXtUNxahWGzHEMd1H0oD/TvVmrlmBVTdR37k0T
u8oJumfgsFcakhSFIfoBqaqZcyzmbLBCfyS1zYJ4FCPm1ciGYIa8PzboIwM3vWI+
r866K86o1lqGxxihHE7EcUVMq9gYYp/GZvHxFXcd2QKBgQDoD6gZZaJwbTVToelS
6OZozIKbd/Ue5TLiXA2phqe4pLw4HOw1Jl3eiYFKQJ/2uBZNt3P1/tC1+P8hafEo
btrFIKQlGV1UTFXxwnUjTo9Ky1g4Z8e9qtuFkN0ZJ0g7taOUD88DZtVTwN4wDVgy
7ViZvmXQpSvmgkMZcwuF7AY3NQKBgQDkyiq2TRlirMGDPeg5KXsvKBaSUmBrSjkB
YqGvcAP5yhTt174L/UTQmE26Mczv1D8dQBJWL9cr6sIFWwBN5BuKuJqzT03fS7Ou
u/FWu8c4qx0cP7zlLUiANknEOdQOLGh+PbaRh9V6V0PviEGWciySuZYgJbMm0ALB
Fr49NrMlJwKBgBz4x23USIFswPmd/zlApnNzBONQCKRAzSeBgpslmo7s0irXQY4p
KhL8a83PX6k3tmEhhDK0C26MlZ2gUmFP5bQyrQuMrSA3H4u9UU6FIlKeLHduTXua
dymnulLHmrcJqFB14Mx17DA2pgatw9Mn2qXnJWL1HBP9M09cE5Y2r1f5AoGBAKMK
SvvU36VI9TJAuK+blvRY/hTR7XIn143cKtqp2bt1Pgrsdrt2hkaccq+gc6npN/zx
Pt/6gb0DM7a7TfE0AEiQG3ZyqkzZVrfLqUWk1WjV0A3kgglThtoPVewnRa3ACcsE
0YjOItxnObuF/y9mN8trw8cu9odPLtdJDNL0mx97AoGAeqgG8AzVM8P0+YZGoT/c
ZC/yot1YbfPRvmWNaJLxdXRphoXWELXUdt+MuUFEw63wwrBC48yJcGbr2fDytqG+
q3Bwq/LPV4+7l5y5+y1D+NCplBusqo5Sh0+MSHkWdxg38EuwUam216uvydnxRGLt
/fV8hnIbsJLFjVT4vqo2kdQ=
-----END PRIVATE KEY-----
"""

CLIENT_EMAIL = "firebase-adminsdk-igpbe@eusummit2025.iam.gserviceaccount.com"
CLIENT_ID = "109555817440430494954"
AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"
AUTH_PROVIDER_CERT_URL = "https://www.googleapis.com/oauth2/v1/certs"
CLIENT_CERT_URL = "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-igpbe%40eusummit2025.iam.gserviceaccount.com"
UNIVERSE_DOMAIN = "googleapis.com"

config = {
    "type": TYPE,
    "project_id": PROJECT_ID,
    "private_key_id": PRIVATE_KEY_ID,
    "private_key": PRIVATE_KEY,
    "client_email": CLIENT_EMAIL,
    "client_id": CLIENT_ID,
    "auth_uri": AUTH_URI,
    "token_uri": TOKEN_URI,
    "auth_provider_x509_cert_url": AUTH_PROVIDER_CERT_URL,
    "client_x509_cert_url": CLIENT_CERT_URL,
    "universe_domain": UNIVERSE_DOMAIN,
}

cred = credentials.Certificate(config)
app1 = firebase_admin.initialize_app(cred, {'databaseURL': 'https://eusummit2025-default-rtdb.europe-west1.firebasedatabase.app/'})

db = firestore.client()

def get_emails():
    emails = []
    sales_ref = db.collection("emails")
    docs = sales_ref.get()
    for doc in docs:
        data = doc.to_dict()
        if 'mail' in data:  # Ensure 'email' key exists
            emails.append(data['mail'])
    
    return emails

if __name__ == "__main__":
    emails = get_emails()
    print(emails)