import streamlit as st
import pandas as pd
import streamlit_pandas as sp
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title('Exploratory Data Analysis')

if "dataframe" in st.session_state:
    data_dict = st.session_state['dataframe']

    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame.from_dict(data_dict)

    # Generate a profile report
    profile_report = ProfileReport(df, title='Pandas Profiling Report', explorative=True)

    # Display the profile report in Streamlit
    st_profile_report(profile_report)
        
else:
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://i.ibb.co/dKdhtMH/crying.png")
    with col2:
        st.warning("The App Runner can't find any data, please upload a valid file first!")
        st.warning("Please note that if the file is too big, the App Runner might take some time to come up with the results")
        st.warning("This is just a file for you, but it is his raison d'etre")