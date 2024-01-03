import pyttsx3
import PyPDF2
from tkinter.filedialog import *

#read pdf file from the user
book = askopenfilename()
#initialise it with the pdf reader
pdfreader = PyPDF2.PdfFileReader(book)
#get the number of pages from the PDF file, return pages of pdf
pages = pdfreader.numPages
#read all of the data from each page in the pdf
for num in range(0, pages):
    page = pdfreader.getPage(num)
#extract text
    text = page.extract_text()
#define tts object
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
