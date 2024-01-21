import sys
from gradio_client import Client
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

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