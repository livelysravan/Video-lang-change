import PyPDF2
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdf_path = '/Users/sravansnair/Downloads/storyofdog.pdf' 

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

english_text = extract_text_from_pdf(pdf_path)
def translate_to_malayalam(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ml')
    return translated_text.text

malayalam_text = translate_to_malayalam(english_text)
buffer = BytesIO()
doc = SimpleDocTemplate(buffer, pagesize=letter)

story = []
pdfmetrics.registerFont(TTFont('NotoSansMalayalam', '/Users//Downloads/Noto_Sans_Malayalam/NotoSansMalayalam-VariableFont_wdth,wght.ttf'))  # Replace with the actual path on your Mac
malayalam_style = ParagraphStyle(
    name='MalayalamStyle',
    fontName='NotoSansMalayalam',
    fontSize=12,
    leading=14,
    textColor=colors.black,
)

story.append(Paragraph(malayalam_text, malayalam_style))

doc.build(story)

malayalam_pdf_path = 'malayalam_text.pdf'
with open(malayalam_pdf_path, 'wb') as f:
    f.write(buffer.getvalue())

print(f"Malayalam PDF saved to {malayalam_pdf_path}")

