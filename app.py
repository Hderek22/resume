### Main page for streamlit resume
import streamlit as st
import intro.about
import intro.skills
import intro.projects
import intro.edu
import intro.recommendations

import resources.ast as ast

PAGES = {
    "About": intro.about,
    "Education" : intro.edu,
    "Skills": intro.skills,
    "Projects": intro.projects,
    "Recommendations": intro.recommendations
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me")
    st.sidebar.info(
        """
        If you are looking to hire a Data Scientist, 
        [email me](mailto:abhishek.2.gupta@uconn.edu) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/abhishek-gupta-/)
""")
    st.sidebar.title("Additional Info")
    st.sidebar.info(
        "This an interactive streamlit app completely created with Python's latest library **streamlit** "
        "Do reach out to me on [LinkedIn](https://www.linkedin.com/in/abhishek-gupta-/) or "
        "at [Mail me](mailto:abhishek.2.gupta@uconn.edu) to know more. "
        "Also check the [source code](https://github.com/alphadatagamma/Streamlit-Resume-App) here. "  

)

if __name__ == "__main__":
    main()
