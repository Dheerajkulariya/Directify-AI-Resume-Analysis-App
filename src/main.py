# Import pandas for data manipulation and analysis
import pandas as pd

# Import streamlit for creating and sharing web apps for machine learning and data science projects
import streamlit as st
# Import st_tags from streamlit_tags for adding tagging functionality to Streamlit apps
from streamlit_tags import st_tags

# Import Image from PIL for image processing capabilities
from PIL import Image



def main():
    
    """
    Main function to run the Directify AI Resume App.
    
    This function sets up the Streamlit page configuration, displays the app logo,
    title, and sidebar menu. It then handles different user choices (User or Admin)
    and displays appropriate content based on the selection.
    """
    # Set up the Streamlit page configuration
    st.set_page_config(page_title="Directify AI Resume App", page_icon="../images/Directify_Logo_01.png", layout="wide")

    # Load and display the app logo
    img = Image.open('../images/Directify_Logo_01.png')
    # Uncomment the following line to resize the image if needed
    # img = img.resize((250,250))
    st.image(img)

    # Display the app title
    st.title("Directify AI Resume App")

    # Set up the sidebar menu
    st.sidebar.markdown("# Choose User")
    menu = ['User', 'Admin']
    choice = st.sidebar.selectbox('Menu', menu)

    # Handle user choice
    if choice == 'User':
        # Display user-side content
        st.markdown('''<h5 style='text-align: left; color: #021659;'>Upload your resume, and get smart recommendations</h5>''', unsafe_allow_html=True)

    elif choice == 'Admin':
        # Display admin-side content
        st.success("Welcome to Admin Side")

    else:
        # Display error message for incorrect credentials
        # Note: This else block might not be necessary as the selectbox limits choices to 'User' and 'Admin'
        st.error("ID & Password is Incorrect")

if __name__ == '__main__':
    main()