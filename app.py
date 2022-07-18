### Main page for streamlit resume
import streamlit as st
import intro.about
import intro.projects
import intro.edu
import intro.recommendations

import resources.ast as ast

PAGES = {
    "About": intro.about,
    "Tech Skills" : intro.edu,
    "Projects": intro.projects,
    "Career": intro.recommendations
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me.")
    st.sidebar.info(
        """
        Are you are looking for help developing and building your business? 
        [Email me](mailto:Hderek22@icloud.com) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/hderek22/)
""")
    st.sidebar.title(" ")
    st.sidebar.info(
        "This interactive app was built with **streamlit**. "
        "[source code](https://github.com/Hderek22/resume)"  

)

if __name__ == "__main__":
    main()
