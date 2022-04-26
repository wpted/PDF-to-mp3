from PyPDF2 import PdfFileReader
from gtts import tts
from playsound import playsound


def pdf_to_text(input_path):
    """

    :param input_path: raw string
    :return: read text
    """

    pdf_path = input_path
    pdf_file_object = open(pdf_path, 'rb')
    pdf_reader = PdfFileReader(pdf_file_object)

    text = ""

    for i in range(0, pdf_reader.numPages):
        page_object = pdf_reader.getPage(i)
        text += page_object.extractText()

    return text


def play_input_text(output, text):
    """
    Takes pure text as input and save the output_name as file name in the output_path.
    :param output: Dict{
                        "name": as you like, default as default.mp3,
                        "path":as you like, default as the main code directory
                        }
    :param speed: String
    :param lang: String
    :param text: String
    """
    play_target = tts.gTTS(text)
    output_name = output["name"]
    play_target.save(output_name)
    playsound(output["path"])


def main():
    sample_pdf = r"../pdf_to_audio/sample.pdf"
    output_params = {"name": "sample.mp3", "path": f"../pdf_to_audio/sample.mp3"}
    parsed_text = pdf_to_text(sample_pdf)
    play_input_text(output_params, parsed_text)


if __name__ == "__main__":
    main()
