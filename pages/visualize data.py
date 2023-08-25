import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title('Visualize Data')

 # Add a dropdown for visualization selection
visualization_option = st.selectbox("Select Visualization", ["Bar Plot", "Scatter Plot", "Histogram", "Pie Chart", "Heat Map", "Line Chart", "Area Chart"])

if "dataframe" in st.session_state:
        
        df = st.session_state['dataframe']

        # Add columns for x and y axes
        col1, col2 = st.columns(2)
        with col1:
            x_column = st.selectbox("Select X-axis Column", df.columns)
        with col2:
            y_column = st.selectbox("Select Y-axis Column", df.columns)

        if visualization_option == "Bar Plot":
            fig = px.bar(df, x=x_column, y=y_column, title=f"Bar Plot: {x_column} vs {y_column}")
            st.components.v1.html(fig.to_html(config={'displayModeBar': False}), width=700, height=500)

        elif visualization_option == "Scatter Plot":
            fig = px.scatter(df, x=x_column, y=y_column, title=f"Scatter Plot: {x_column} vs {y_column}")
            st.components.v1.html(fig.to_html(config={'displayModeBar': False}), width=700, height=500)

        elif visualization_option == "Histogram":
            fig = px.histogram(df, x=x_column, title=f"Histogram for {x_column}")
            st.components.v1.html(fig.to_html(config={'displayModeBar': False}), width=700, height=500)

        elif visualization_option == "Pie Chart":
            fig = px.pie(df, names=x_column, title=f"Pie Chart for {x_column}")
            st.components.v1.html(fig.to_html(config={'displayModeBar': False}), width=700, height=500)

        elif visualization_option == "Heat Map":
            fig = px.imshow(df.corr(), title="Heat Map")
            st.components.v1.html(fig.to_html(config={'displayModeBar': False}), width=700, height=500)

        elif visualization_option == "Line Chart":
            fig = px.line(df, x=x_column, y=y_column, title=f"Line Chart: {x_column} vs {y_column}")
            st.components.v1.html(fig.to_html(config={'displayModeBar': False}), width=700, height=500)

        elif visualization_option == "Area Chart":
            fig = px.area(df, x=x_column, y=y_column, title=f"Area Chart: {x_column} vs {y_column}")
            st.components.v1.html(fig.to_html(config={'displayModeBar': False}), width=700, height=500)

else:
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://i.ibb.co/dKdhtMH/crying.png")
    with col2:
        st.warning("The App Runner can't find any data, please upload a valid file first!")
        st.warning("Please note that if the file is too big, the App Runner might take some time to come up with the results")
        st.warning("This is just a file for you, but it is his raison d'etre")