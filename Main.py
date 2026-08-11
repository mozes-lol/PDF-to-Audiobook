import PyPDF2
import pyttsx3
speaker = pyttsx3.init()
book = open('Kanibalismo.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print("There is/are " + str(pages) + " page/s in this document.")
for num in range(pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

