from docx import Document


def create_word_document():

    document = Document()

    document.add_heading("TECHNICAL OFFER", level=1)

    document.add_paragraph("This document was generated automatically.")

    document.save("output/technical_offer.docx")