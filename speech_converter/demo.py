from gtts import gTTS
import os

text = "Hello Karthikeyaa! this is really funny"
output = gTTS(text,lang='en',slow=False)
output.save('output.mp3')
os.system("start output.mp3")