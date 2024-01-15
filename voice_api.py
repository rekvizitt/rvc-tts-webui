import sys
from gradio_client import Client

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

args = sys.argv

client_link = args[1]
model_name = args[2]
user_input = args[3]


client = Client(f"{client_link}")
result = client.predict(
	model_name,
	20,
	user_input,
	"ru-RU-DmitryNeural-Male",
	2,
	"rmvpe",
	1,
	0.33,
	fn_index=0
)

print(result[2])