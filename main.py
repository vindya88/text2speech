import pyttsx3
import PyPDF2

book = open('ANN Instructions', 'rb')
pdfReader = PyPDF2.PdfReader(book)
num_pages = len(pdfReader.pages)

speaker = pyttsx3.init()
for page_number in range(200, num_pages):
    page = pdfReader.pages[page_number]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

book.close()
