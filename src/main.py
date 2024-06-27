# Import pandas for data manipulation and analysis
import pandas as pd

# Import nltk for natural language processing tasks
import nltk
# Ensure that the stopwords corpus is available, downloading it if necessary
nltk.download('stopwords')

# Import base64 for encoding/decoding data in base64 format
import base64
# Import random for generating random numbers and selecting random elements
import random

# Import time for time-related functions
import time
# Import datetime for handling date and time information
import datetime

# Import streamlit for creating and sharing web apps for machine learning and data science projects
import streamlit as st
# Import st_tags from streamlit_tags for adding tagging functionality to Streamlit apps
from streamlit_tags import st_tags

# Import pymysql for interacting with MySQL databases
import pymysql

# Import plotly.express for creating interactive charts and visualizations
import plotly.express as px

# Import pafy for interacting with YouTube content, such as fetching metadata and downloading videos
import pafy

# Import io for handling I/O operations on various types of streams
import io
# Import random for generating random numbers and selecting random elements (redundant import, already included above)
import random

# Import Image from PIL for image processing capabilities
from PIL import Image

# Import specific course data from a local module named Courses
#from Courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos

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