import whisper
import asyncio
import asyncio
import websockets
from datetime import datetime



model = whisper.load_model("tiny.en")
file_name = 'hpi-en-fast.mp3'
current_dateTime = datetime.now()
result = model.transcribe(file_name, language='English')
result = model.transcribe(file_name, language='English')
result = model.transcribe(file_name, language='English')
result = model.transcribe(file_name, language='English')
result = model.transcribe(file_name, language='English')
result = model.transcribe(file_name, language='English')
current_dateTime1 = datetime.now()
time_diff = current_dateTime1 - current_dateTime
print(time_diff)
print(result["text"])


