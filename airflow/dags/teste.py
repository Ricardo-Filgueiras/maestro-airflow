""" 
from minio import Minio
import os

# Minio connection details
# It's recommended to use environment variables for sensitive information
# or a secure configuration management system.
# For demonstration purposes, placeholders are used here.
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "3C5GQ6m9ltG3UDCz7qXz")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "JSoP9ezbLdtOF4gDB7gFjScywikFxRX04hRzqazZ")
MINIO_SECURE = os.getenv("MINIO_SECURE", "False").lower() == "true" # Use True for HTTPS

def test_minio_connection():
    """
    Tests the connection to the Minio server.
    """
    try:
        # Create a client with the Minio server playground endpoint,
        # access key and secret key.
        client = Minio(
            MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=MINIO_SECURE
        )

        # List buckets to check connection
        buckets = client.list_buckets()
        print(f"Successfully connected to Minio at {MINIO_ENDPOINT}.")
        print("Existing buckets:")
        for bucket in buckets:
            print(f"- {bucket.name}")

    except Exception as e:
        print(f"Error connecting to Minio: {e}")

if __name__ == "__main__":
    test_minio_connection()

"""