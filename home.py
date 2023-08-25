import streamlit as st
import pandas as pd

linkedin = "https://www.linkedin.com/in/sarimkhanskd"

# set page title
st.set_page_config(page_title="home")

# define a function to read uploaded csv file and store it in session state
#@st.cache_data
def read_file(file):
    file_extension = file.name.split('.')[-1]
    if file_extension == 'csv':
        df = pd.read_csv(file)
    elif file_extension in ['xls', 'xlsx']:
        df = pd.read_excel(file, engine='openpyxl')
    else:
        st.error("Unsupported file format!")
        df = None
    return df

# main function
def main():
    # set page title
    st.title("Auto Analysis")
    st.write('Auto Analysis offers exploratory data analysis, data visualization, time series analysis, and sentiment analysis – all in one place.')
    # create a file uploader
    file = st.file_uploader("Upload a CSV file")
    
    # check if file is uploaded
    if file is not None:
         # check file extension
        file_ext = file.name.split(".")[-1]
        if file_ext in ["xlsx", "xls", "csv"]:
            # read file and store it in session state
            st.session_state['dataframe'] = read_file(file)
        else:
            st.error("Unsupported file format!")

    # check if dataframe is available in session state
    if "dataframe" in st.session_state:
        # create two columns
        col1, col2 = st.columns(2)
        
        # show dataframe in expander of column 1
        with col1.expander("Dataframe", expanded=False):
            st.write(st.session_state['dataframe'])
        
        # show column names in expander of column 2
        with col2.expander("Column Names", expanded=False):
            st.write(list(st.session_state['dataframe'].columns))
        
    st.write("Developed by [Sarim Khan](%s)" % linkedin)

# run main function
if __name__ == "__main__":
    main()
