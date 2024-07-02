# Import io for handling I/O operations on various types of streams
import io
# Import base64 for encoding/decoding data in base64 format
import base64
# Import streamlit
import streamlit as st
# Import ResumeParser from pyresparser for extracting information from resumes
from pyresparser import ResumeParser
# Import LAParams, LTTextBox from pdfminer3 for configuring PDF parsing parameters and handling text boxes in PDFs
from pdfminer3.layout import LAParams, LTTextBox
# Import PDFPage from pdfminer3 for iterating over pages in a PDF document
from pdfminer3.pdfpage import PDFPage
# Import PDFResourceManager and PDFPageInterpreter from pdfminer3 for managing resources and interpreting PDF pages
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
# Import TextConverter from pdfminer3 for converting PDF documents to text
from pdfminer3.converter import TextConverter

def pdf_reader(file):
    """
    Reads a PDF file and extracts its text content.

    Args:
        file (str): The path to the PDF file.

    Returns:
        str: The extracted text content from the PDF file.
    """

    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams = LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching = True, check_extractable=True):
            # Process each page of the PDF
            page_interpreter.process_page(page)
            # Print the page object (optional for debugging)
            print(page)
        text = fake_file_handle.getvalue()
    # Close open handles to release resources
    converter.close()
    fake_file_handle.close()
    return text

def show_pdf(file_path):
    """
    Displays a PDF file in an iframe within the Streamlit app.

    Args:
        file_path (str): The path to the PDF file.
    """

    with open(file_path, 'rb') as fp:
        # Read the PDF file and encode it in base64
        base64_pdf = base64.b64encode(fp.read()).decode('utf-8')
    # Construct an iframe HTML string to display the PDF
    pdf_display = f'<iframe src = "data:application/pdf;base64,{base64_pdf} "width = "700" height = "1000" type = "application/pdf"></iframe>'
    # Display the PDF in the Streamlit app using markdown
    st.markdown(pdf_display, unsafe_allow_html=True)

            