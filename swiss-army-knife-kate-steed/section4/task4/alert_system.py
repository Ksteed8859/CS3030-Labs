import os
import requests
from dotenv import load_dotenv

load_dotenv()
webhook_url = os.environ.get("WEBHOOK_URL")

message = {"content": "Hello World!"}

requests.post(webhook_url, json=message)