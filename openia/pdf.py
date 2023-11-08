import pdfx


def text_from_pdf(file_location:str):
    text = pdfx.PDFx(file_location).get_text()
    # Modify the text as needed
    text = text.replace('\n\n', ',').strip()  # Remove newlines and strip spaces
    text = text.replace('\n\n\n', '').strip()
    text = text.replace('\n\n\n\n ', '').strip()
    return text