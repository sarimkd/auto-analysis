import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px


def identify_columns(dataframe):
    """
    Identifies the data type of each column in a given dataframe.
    """
    date_cols = []
    numeric_cols = []
    categorical_cols = []

    for col in dataframe.columns:
        if pd.api.types.is_datetime64_dtype(dataframe[col]):
            date_cols.append(col)
        elif pd.api.types.is_numeric_dtype(dataframe[col]):
            numeric_cols.append(col)
        elif pd.api.types.is_string_dtype(dataframe[col]):
            try:
                pd.to_datetime(dataframe[col])
                date_cols.append(col)
            except ValueError:
                categorical_cols.append(col)
        else:
            categorical_cols.append(col)

    return date_cols, numeric_cols, categorical_cols


def convert_to_datetime(dataframe, date_cols):
    """
    Converts date columns in a given dataframe to datetime64 data type and format them as YEAR-MONTH-DAY.
    """
    for col in date_cols:
        dataframe[col] = pd.to_datetime(dataframe[col], infer_datetime_format=True).dt.strftime('%Y-%m-%d')
        dataframe[col] = pd.to_datetime(dataframe[col], infer_datetime_format=True)
        
    return dataframe

st.title('Time Series Analysis')

if 'dataframe' in st.session_state:
    df = st.session_state['dataframe']
    # Identify columns
    date_cols, numeric_cols, categorical_cols = identify_columns(df)

    # Convert date columns to datetime64 data type
    df = convert_to_datetime(df, date_cols)

    st.write('Choose columns that you want to analyse:')

    try:
        date_column = st.selectbox('Choose the Date column', date_cols)
        numerical_column = st.selectbox('Choose the Values column', numeric_cols)

        df_new = df[[date_column, numerical_column]]
        st.dataframe(df_new)
        df_new.rename(columns={date_column: 'ds', numerical_column: 'y'}, inplace=True)

        # Train Model
        m = Prophet(interval_width=0.95, daily_seasonality=True)
        model = m.fit(df_new)

        # Set Parameters
        col1, col2 = st.columns(2)
        periods = col1.number_input('Select Number of Periods for Forecasting', step=1, value=100)
        frequency = col2.radio('Select the frequency of the periods:', ['Day', 'Week', 'Month', 'Quarter', 'Year'])
        frequency = frequency[0]

        # Forecast
        future = m.make_future_dataframe(periods=periods, freq=frequency)
        forecast = m.predict(future)
        forecast = forecast[['ds', 'yhat']]

        # Graphs
        col = st.color_picker('Select a color for the charts')

        # Line Chart
        line_plot = px.line(forecast, x=forecast['ds'], y=forecast['yhat'])
        line_plot.update_traces(marker=dict(color=col))
        st.plotly_chart(line_plot)

    except KeyError:
        st.warning("No Valid Column Detected, to run the time series analysis, please upload a file with at least one:\n 1) Date column \n2) Numerical Column")
        # You can also clear the session_state or take other appropriate actions here.
else:
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://i.ibb.co/vjKcnJF/begging.png")
    with col2:
        st.warning("The App Runner can't find valid data, please upload a valid file first!")
        st.warning("In order to run the time series analysis, please upload a file with at least one:\n 1) Date column \n2) Numerical Column")
        st.warning("This is just a file for you, but it is his raison d'etre")