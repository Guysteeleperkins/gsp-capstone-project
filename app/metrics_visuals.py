import streamlit as st
import plotly.express as px
from app.data_processing import weekly_activities


def display_metrics(df):
    """Display key metrics in Streamlit"""
    total_distance = calculate_total_distance(df)
    total_calories = calculate_total_calories(df)
    total_elevation = calculate_total_elevation(df)
    total_steps = calculate_total_steps(df)

    # Display Metics in Columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Distance (km)", value=total_distance)
    with col2:
        st.metric(label="Calories Burnt", value=total_calories)
    with col3:
        st.metric(label="Elevation (M)", value=total_elevation)
    with col4:
        st.metric(label="Steps Taken", value=total_steps)


def calculate_total_distance(df):
    """Calculate total distance run within time frame
    of dataset"""
    distance = df["Distance"].sum().round(2)
    return distance.round(2)


def calculate_total_calories(df):
    """Calculate total calories burnt within
    time frame of data set"""
    return df["Calories"].sum()


def calculate_total_elevation(df):
    """Calculate total elevation gained within time
    frame of dataset"""
    return df["Total Ascent"].sum()


def calculate_total_steps(df):
    """Calculate total steps within time frame of
    dataset"""
    return df["Steps"].sum()


def create_weekly_activities_chart(df):
    """Create a chart for number of activities per week"""
    weekly_df = weekly_activities(df)

    fig = px.bar(
        weekly_df,
        x="Week",
        y="Number of Activities",
        title="Number of Activities per Week"
    )

    return fig


def display_visualizations(df):
    """Display visualizations in Streamlit."""
    fig1 = create_weekly_activities_chart(df)
    st.plotly_chart(fig1)
