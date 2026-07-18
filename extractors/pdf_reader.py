from pypdf import PdfReader

def read_pdf(path):

    text = ""

    reader = PdfReader(path)

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text