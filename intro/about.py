"""About page shown when the user enters the application"""
import streamlit as st

def write():
# Used to write the about page in the app.py file
    st.title("Derek Hall")
    st.image("resources/images/Derek.JPG",width = 250)
    st.markdown(
    """

"_Focus on the success of those around you and yours will come naturally, for all boats rise on a rising sea._"


Immersing myself completely into something that I enjoy has been my key to success. I am currently 100 percent focused on blockchain engineering/development and can't wait to see where it takes me!


## Experiences

**Business Development | Leadership | Team Building | Finance**

## Skills

**Python | Solidity | Machine Learning | API's | SQL | AWS**

[**LinkedIn**](https://www.linkedin.com/in/hderek22) | [**Email**](mailto:Hderek22@gmail.com)

## My Goals

**Join a team with like-minded 'can do' teammates and build a 4 star business!**

-----

*Built with [**Streamlit**](https://www.streamlit.io/)*

*Check out my [**GitHub**](https://github.com/Hderek22/resume.git) for the implementation details of this page.* 




""",
    unsafe_allow_html=True,
)
