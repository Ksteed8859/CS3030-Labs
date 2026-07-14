import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("SUPER_SECRET_KEY")

hidden_key = "*******" + key[-3:]

print(f"Accessing system with key: {hidden_key}")



