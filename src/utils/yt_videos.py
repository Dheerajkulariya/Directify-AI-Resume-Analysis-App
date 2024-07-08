# Import necessary modules
import os

# Import pafy for interacting with YouTube content, such as fetching metadata and downloading videos
import pafy

# Set the PAFY_BACKEND environment variable to use yt-dlp as the backend
# This is done to ensure compatibility and better performance
os.environ["PAFY_BACKEND"] = "yt-dlp"

def fetch_yt_video(link):
    """
    Fetch the title of a YouTube video given its URL.

    This function uses the pafy library to retrieve metadata about a YouTube video.
    It attempts to create a new pafy object from the provided link and returns the video's title.
    If an error occurs during the process, it returns an error message instead.

    Args:
        link (str): The URL of the YouTube video.

    Returns:
        str: The title of the YouTube video if successful, or an error message if an exception occurs.

    Raises:
        No exceptions are raised directly by this function, but exceptions from pafy are caught and converted to error messages.
    """

    try:
        # Attempt to create a new pafy object from the provided link
        video = pafy.new(link)
        # If successful, return the video's title
        return video.title
    except Exception as e:
        # If an exception occurs, return an error message with the exception details
        return f"Error fetching video: {str(e)}"