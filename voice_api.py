import sys
from gradio_client import Client
import codecs
import os

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

args = sys.argv

client_link = args[1]
model_name = args[2]
user_input = args[3]
file_name = args[4]

client = Client(f"{client_link}")
result = client.predict(
	model_name,
	10,
	user_input,
	"ru-RU-DmitryNeural-Male",
	2,
	"rmvpe",
	1,
	0.33,
	fn_index=0
)

with open(os.path.join("C:\\Users\\Vladislav\\AppData\\Roaming\\Godot\\app_userdata\\streamers_ai", file_name), "w") as file:
    file.write(result[2])

sys.exit(0)