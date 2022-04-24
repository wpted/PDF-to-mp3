from gtts import gTTS
from playsound import playsound

my_text = "Hello World"

language = "en"

my_obj = gTTS(text=my_text, lang=language, slow=False)
my_obj.save("hello_world.mp3")

playsound("../pdf_to_audio/hello_world.mp3")
