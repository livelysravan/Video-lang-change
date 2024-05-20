import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Formula_One'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text_content = ' '.join([p.get_text() for p in soup.find_all('p')])

print(text_content)
import tkinter as tk
from googletrans import Translator

translator = Translator()

desired_language = 'ml' 
translated_text = translator.translate(text_content, dest=desired_language).text

root = tk.Tk()
root.title("Noto Sans Malayalam Text")
text_widget = tk.Text(root, font=("Noto Sans Malayalam", 12))
text_widget.pack()

text_widget.insert(tk.END, translated_text)

root.mainloop()

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from googletrans import Translator

translator = Translator()

desired_language = 'ml'  
translated_text = translator.translate(text_content, dest=desired_language).text

pdfmetrics.registerFont(TTFont('NotoSansMalayalam', r'C:\Users\sravansnair\Downloads\Noto_Sans_Malayalam\NotoSansMalayalam-VariableFont_wdth,wght.ttf'))  # Replace with the actual path


doc = SimpleDocTemplate("translated_document_web.pdf", pagesize=letter)
malayalam_style = getSampleStyleSheet()['Normal']
malayalam_style.fontName = 'NotoSansMalayalam'
malayalam_style.fontSize = 12
malayalam_style.leading = 14
malayalam_style.textColor = colors.black

translated_paragraph = Paragraph(translated_text, style=malayalam_style)
doc.build([translated_paragraph])

