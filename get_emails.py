import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
    "type": "service_account",
    "project_id": "eusummit2025",
    "private_key_id": "b9534ea18e65f8363e168153d92fd1de22c22868",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPZTTJFShDkofu\noRflh+TVp9+cdkaVget6tfC10NSvmr1qlwj5rbYasXOBoRsHJCPGp1xWkbgsbeTf\nVCuqi9x2R0f87cC9hRZ4Zs2WZYYv4t2ivckcMw4W/7eQ/SgSrmggsXetcpwsmTPn\npvSLGjxrvFX0Ly+uwuj9igs/bOITNnpgnspOQxT5f/iWAWANw0JBby/ULpFhkJXU\nUqC4Z7oa9Dp4umrMtRignqDgmeWO7ZaBoSdTyW0OSG8dL4iDU3lL8DDDMtYf6h5M\n0tRLD7dGnMMGNwygbtSia3gYs/8Lec2QufYrC+GnuHsX058pug5WAJ+cymo1bV2g\n8iKi/BITAgMBAAECggEARpKc1LQjYGMTaGte81c70kxuthI1UJjGJZqVz3jBdwQD\n4qqEflnTNuAdewX0aYitt+KpdDff4RaAJFLDDSTMn18AKxxIUvVfwRbSbJQdhlv/\nqWpFbhgdekwIDglnQnwgqMda/yWZ6T80v2Y7nr4Nw2dyJEaORjzDBcucqjeF8p0h\nU1ZD7/qlusgyNYmu68K/LahBR1KXtUNxahWGzHEMd1H0oD/TvVmrlmBVTdR37k0T\nu8oJumfgsFcakhSFIfoBqaqZcyzmbLBCfyS1zYJ4FCPm1ciGYIa8PzboIwM3vWI+\nr866K86o1lqGxxihHE7EcUVMq9gYYp/GZvHxFXcd2QKBgQDoD6gZZaJwbTVToelS\n6OZozIKbd/Ue5TLiXA2phqe4pLw4HOw1Jl3eiYFKQJ/2uBZNt3P1/tC1+P8hafEo\nbtrFIKQlGV1UTFXxwnUjTo9Ky1g4Z8e9qtuFkN0ZJ0g7taOUD88DZtVTwN4wDVgy\n7ViZvmXQpSvmgkMZcwuF7AY3NQKBgQDkyiq2TRlirMGDPeg5KXsvKBaSUmBrSjkB\nYqGvcAP5yhTt174L/UTQmE26Mczv1D8dQBJWL9cr6sIFWwBN5BuKuJqzT03fS7Ou\nu/FWu8c4qx0cP7zlLUiANknEOdQOLGh+PbaRh9V6V0PviEGWciySuZYgJbMm0ALB\nFr49NrMlJwKBgBz4x23USIFswPmd/zlApnNzBONQCKRAzSeBgpslmo7s0irXQY4p\nKhL8a83PX6k3tmEhhDK0C26MlZ2gUmFP5bQyrQuMrSA3H4u9UU6FIlKeLHduTXua\ndymnulLHmrcJqFB14Mx17DA2pgatw9Mn2qXnJWL1HBP9M09cE5Y2r1f5AoGBAKMK\nSvvU36VI9TJAuK+blvRY/hTR7XIn143cKtqp2bt1Pgrsdrt2hkaccq+gc6npN/zx\nPt/6gb0DM7a7TfE0AEiQG3ZyqkzZVrfLqUWk1WjV0A3kgglThtoPVewnRa3ACcsE\n0YjOItxnObuF/y9mN8trw8cu9odPLtdJDNL0mx97AoGAeqgG8AzVM8P0+YZGoT/c\nZC/yot1YbfPRvmWNaJLxdXRphoXWELXUdt+MuUFEw63wwrBC48yJcGbr2fDytqG+\nq3Bwq/LPV4+7l5y5+y1D+NCplBusqo5Sh0+MSHkWdxg38EuwUam216uvydnxRGLt\n/fV8hnIbsJLFjVT4vqo2kdQ=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-igpbe@eusummit2025.iam.gserviceaccount.com",
    "client_id": "109555817440430494954",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-igpbe%40eusummit2025.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
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