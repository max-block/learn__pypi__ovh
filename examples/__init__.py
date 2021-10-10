import os

from dotenv import load_dotenv
from ovh import Client

load_dotenv()

APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")


def get_client() -> Client:
    return Client(
        endpoint="ovh-eu",
        application_key=APP_KEY,
        application_secret=APP_SECRET,
        consumer_key=CONSUMER_KEY,
    )
