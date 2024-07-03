import streamlit as st
import random

def course_recommender(course_list):
    """
    Recommends a random selection of courses from a given list.

    Args:
        course_list (list): A list of tuples, where each tuple contains a course name and its link. 
                            Example: [("Python for Beginners", "https://www.example.com/python-beginners"), ...]

    Returns:
        list: A list of course names that were recommended.
    """
        
    st.subheader("**Courses & Certificates Recommendations 🎓**")
    c = 0  # Counter for the number of courses recommended
    rec_course = []  # List to store the recommended course names
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 5)  # User input for the number of recommendations
    random.shuffle(course_list)  # Shuffle the course list to randomize recommendations
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}] ({c_link})")  # Display the course name and link
        rec_course.append(c_name)  # Add the course name to the recommendations list
        if c == no_of_reco:  # Stop recommending when the desired number of recommendations is reached
            break
    return rec_course