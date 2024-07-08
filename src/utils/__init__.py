"""
This module provides functionality for parsing PDFs and fetching YouTube videos.

It exports two submodules: pdf_parser and yt_videos.
"""

# Specify which symbols should be exported when using "from module import *"
__all__ = ["pdf_parser", "yt_videos"]

# Import specific functions from the pdf_parser submodule
from .pdf_parser import pdf_reader, show_pdf

# Import the fetch_yt_video function from the yt_videos submodule
from .yt_videos import fetch_yt_video

# Note: The above imports make the following functions available in this module's namespace:
# - pdf_reader: Likely a function to read and parse PDF files
# - show_pdf: Probably a function to display PDF content
# - fetch_yt_video: Presumably a function to retrieve YouTube video information or content