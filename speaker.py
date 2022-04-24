from gtts import gTTS
from playsound import playsound


class Speaker(gTTS):
    def __init__(self, text, language, slow=False):
        self.text = text
        self.lang = language
        self.speed = slow

    def convert_to_mp3(self, filename="default.mp3"):
        self.save(filename)

    @staticmethod
    def play(output_path):
        playsound(output_path)


def main():
    my_text = "Hello World"
    language = "en"

    speaker = Speaker(my_text, language)
    speaker.save("default.mp3")
    Speaker.play("../pdf_to_audio/hello_world.mp3")


if __name__ == "__main__":
    main()
