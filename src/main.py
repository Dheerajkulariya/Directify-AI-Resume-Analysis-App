# Import pandas for data manipulation and analysis
import pandas as pd

# Import nltk for natural language processing tasks
import nltk
# Ensure that the stopwords corpus is available, downloading it if necessary
nltk.download('stopwords')

# Import streamlit for creating and sharing web apps for machine learning and data science projects
import streamlit as st
# Import st_tags from streamlit_tags for adding tagging functionality to Streamlit apps
from streamlit_tags import st_tags

# Import Image from PIL for image processing capabilities
from PIL import Image

# Import create_database_and_table from mysql_db for create database and table if they not exists
from mysql_db import create_database_and_table

# Import ResumeParser from pyresparser for extracting information from resumes
from pyresparser import ResumeParser

#import warnings

# Import show_pdf from utils for show pdf
from utils import pdf_reader, show_pdf

# Import course_recommender from courses for recommend courses
from courses import course_recommender

# Import list of courses from courses_list
from courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos

# Import time for time-related functions
import time
# Import datetime for handling date and time information
import datetime

def main():

    """
    Main function to run the Directify AI Resume App.
    
    This function sets up the Streamlit page configuration, displays the app logo,
    title, and sidebar menu. It then handles different user choices (User or Admin)
    and displays appropriate content based on the selection.
    """
    # Set up the Streamlit page configuration
    st.set_page_config(page_title = "Directify AI Resume App", page_icon = "../images/Directify_Logo_01.png", layout = "wide")

    # Load and display the app logo
    img = Image.open('./images/Directify_Logo_01.png')
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
        st.markdown('''<h5 style='text-align: left; color: #38A1CE;'>Upload your resume, and get smart recommendations</h5>''', unsafe_allow_html=True)

        # Allow user to upload a PDF file
        pdf_file = st.file_uploader("Select your Resume", type = ["pdf"])
        if pdf_file is not None:
            # Show a spinner while uploading the resume
            with st.spinner("Uploading your Resume..."):
                time.sleep(5)
            
            # Save the uploaded resume to a local directory
            save_image_path = "./Uploading_Resumes/" + pdf_file.name
            with open(save_image_path, "wb") as fl:
                fl.write(pdf_file.getbuffer())

            #warnings.filterwarnings("ignore", category=UserWarning)

            # Display the uploaded PDF file
            show_pdf(save_image_path)
            # Parse the resume to extract data
            resume_data = ResumeParser(save_image_path).get_extracted_data()

            if resume_data:
                # Get the whole resume data
                resume_text = pdf_reader(save_image_path)

                # Display resume analysis header
                st.header("**Resume Analysis**")
                st.success("Hello " + resume_data["name"])
                st.subheader("**Your Basic info**")
                try:
                    st.text("Name :" + resume_data["name"])
                    st.text("Email :" + resume_data["email"])
                    st.text("Contact :" + resume_data["phone_number"])
                    st.text("Resume pages :" + str(resume_data["no_of_pages"]))
                except:
                    pass

                # Determine candidate level based on the number of resume pages
                candidate_level = ""
                if resume_data["no_of_pages"] == 1:
                    candidate_level = "Fresher"
                    st.markdown("""<h4 style = 'text-align: left; color: #38A1CE;'>You are at Fresher level!</h4>""",unsafe_allow_html=True)
                elif resume_data["no_of_pages"] == 2:
                    candidate_level = "Intermediate"
                    st.markdown("""<h4 style = 'text-align: left; color: #38A1CE;'>You are at Intermediatelevel!</h4>""",unsafe_allow_html=True)
                elif resume_data["no_of_pages"] >= 3:
                    candidate_level = "Experienced"
                    st.markdown("""<h4 style = 'text-align: left; color: #38A1CE;'>You are at Experienced!</h4>""",unsafe_allow_html=True)
                
                # st.subheader("**Skills Recommendation 💡**")
                # Display current skills
                keywords = st_tags(label = "### Your Current Skills",
                                    text = "See our skills recommendation below",
                                    value = resume_data["skills"],key = "1 ")
                
                # Define skill keywords for different fields
                ds_keyword = ['tensorflow','keras','pytorch','machine learning','deep Learning','flask','streamlit']
                web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                               'javascript', 'angular js', 'c#', 'flask']
                android_keyword = ['android','android development','flutter','kotlin','xml','kivy']
                ios_keyword = ['ios','ios development','swift','cocoa','cocoa touch','xcode']
                uiux_keyword = ['ux','adobe xd','figma','zeplin','balsamiq','ui','prototyping','wireframes','storyframes',
                                'adobe photoshop','photoshop','editing','adobe illustrator','illustrator','adobe after effects',
                                'after effects','adobe premier pro','premier pro','adobe indesign','indesign','wireframe','solid',
                                'grasp','user research','user experience']
                
                # Initialize lists for recommended skills and fields
                recommended_skills = []
                reco_field = ''
                rec_course = ''

                # Courses Recommendation
                for i in resume_data["skills"]:
                    # Data science recommendation
                    if i.lower() in ds_keyword:
                        # Print the skill for debugging
                        print(i.lower())
                        # Set the recommended field to Data Science
                        reco_field = "Data Science"
                        # Display a success message to the user
                        st.success("** Our analysis says you are looking for Data Science Jobs.**")
                        # Define a list of recommended skills for Data Science
                        recommended_skills = ['Data Visualization','Predictive Analysis','Statistical Modeling','Data Mining',
                                              'Clustering & Classification','Data Analytics','Quantitative Analysis','Web Scraping',
                                              'ML Algorithms','Keras','Pytorch','Probability','Scikit-learn','Tensorflow',"Flask",'Streamlit']
                        # Display the recommended skills using the st_tags function
                        recommended_keywords = st_tags(label = "### Recommended skills for you.",
                                                       text = "Recommended skills generated from System", value = recommended_skills, key = "2")
                        # Display a message encouraging the user to add the recommended skills to their resume
                        st.markdown("""<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job</h4>""",unsafe_allow_html=True)
                        # Recommend courses based on the Data Science field
                        rec_course = course_recommender(ds_course)
                        # Break the loop after finding a match
                        break

                    # Web development recommendation
                    elif i.lower() in web_keyword:
                        # Print the skill for debugging
                        print(i.lower())
                        # Set the recommended field to Web Development
                        reco_field = "Web Development"
                        # Display a success message to the user
                        st.success("** Our analysis says you are looking for Web Development Jobs.**")
                        # Define a list of recommended skills for Web Development
                        recommended_skills = ['React','Django','Node JS','React JS','php','laravel','Magento','wordpress','Javascript','Angular JS','c#','Flask','SDK']
                         # Display the recommended skills using the st_tags function
                        recommended_keywords = st_tags(label = "### Recommended skills for you.",
                                                       text = "Recommended skills generated from system", value = recommended_skills, key = "3")
                        # Display a message encouraging the user to add the recommended skills to their resume
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        # Recommend courses based on the Web Development field
                        rec_course = course_recommender(web_course)
                        # Break the loop after finding a match
                        break

                    # Android Development
                    elif i.lower() in android_keyword:
                        # Print the skill for debugging
                        print(i.lower())
                        # Set the recommended field to Android Development
                        reco_field = "Android Development"
                        # Display a success message to the user
                        st.success("** Our analysis says you are looking for web Development Jobs.**")
                        # Define a list of recommended skills for Android Development
                        recommended_skills = ['Android','Android development','Flutter','Kotlin','XML','Java','Kivy','GIT','SDK','SQLite']
                         # Display the recommended skills using the st_tags function
                        recommended_keywords = st_tags(label = "### Recommended skills for you.",
                                                       text = "Recommended skills generated from System", value = recommended_skills, key = "4")
                        # Display a message encouraging the user to add the recommended skills to their resume
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        # Recommend courses based on the Android Development field
                        rec_course = course_recommender(android_course)
                        # Break the loop after finding a match
                        break

                    ## IOS App Development
                    elif i.lower() in ios_keyword:
                        # Print the skill for debugging
                        print(i.lower())
                        # Set the recommended field to IOS App Development
                        reco_field = 'IOS Development'
                        # Display a success message to the user
                        st.success("** Our analysis says you are looking for IOS App Development Jobs **")
                        # Define a list of recommended skills for App Development
                        recommended_skills = ['IOS','IOS Development','Swift','Cocoa','Cocoa Touch','Xcode','Objective-C','SQLite','Plist','StoreKit',"UI-Kit",'AV Foundation','Auto-Layout']
                         # Display the recommended skills using the st_tags function
                        recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                        text='Recommended skills generated from System',value=recommended_skills,key = '5')
                        # Display a message encouraging the user to add the recommended skills to their resume
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        # Recommend courses based on the IOS App Development field
                        rec_course = course_recommender(ios_course)
                        # Break the loop after finding a match
                        break

                    ## Ui-UX Recommendation
                    elif i.lower() in uiux_keyword:
                        # Print the skill for debugging
                        print(i.lower())
                        # Set the recommended field to Ui-UX
                        reco_field = 'UI-UX Development'
                        # Display a success message to the user
                        st.success("** Our analysis says you are looking for UI-UX Development Jobs **")
                        # Define a list of recommended skills for Ui-UX
                        recommended_skills = ['UI','User Experience','Adobe XD','Figma','Zeplin','Balsamiq','Prototyping','Wireframes','Storyframes','Adobe Photoshop','Editing','Illustrator','After Effects','Premier Pro','Indesign','Wireframe','Solid','Grasp','User Research']
                        # Display the recommended skills using the st_tags function
                        recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                        text='Recommended skills generated from System',value=recommended_skills,key = '6')
                        # Display a message encouraging the user to add the recommended skills to their resume
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        # Recommend courses based on the Ui-UX field
                        rec_course = course_recommender(uiux_course)
                        # Break the loop after finding a match
                        break




                
                

                

                
                 


                            


    elif choice == 'Admin':
        # Display admin-side content
        st.success("Welcome to Admin Side")

    else:
        # Display error message for incorrect credentials
        # Note: This else block might not be necessary as the selectbox limits choices to 'User' and 'Admin'
        st.error("ID & Password is Incorrect")



if __name__ == '__main__':
    main()