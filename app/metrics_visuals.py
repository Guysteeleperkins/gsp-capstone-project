import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_processing import weekly_activities, weekly_avg_rhr

# Add the project root directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def display_metrics(df):
    """Display key metrics in Streamlit"""
    total_distance = calculate_total_distance(df)
    total_calories = calculate_total_calories(df)
    total_elevation = calculate_total_elevation(df)
    total_steps = calculate_total_steps(df)

    st.markdown('<hr style="border:3px solid gray">', unsafe_allow_html=True)

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

    st.markdown('<hr style="border:3px solid gray">', unsafe_allow_html=True)


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
        y="Activity Count",
        title="Weekly Activity Count"
    )

    return fig


def create_rhr_vs_weekly_activities(df):
    """Create a chart to show RHR against number of activities.
    I found this online, it is not my own code"""

    # Get weekly Activity count
    weekly_df = weekly_activities(df)

    # Get Average RHR per week
    weekly_rhr_df = weekly_avg_rhr(df)

    # Merge Dataframes
    combined_df = pd.merge(weekly_df, weekly_rhr_df, on='Week', how='inner')

    # Create a bar chart for Activity count
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=combined_df['Week'],
            y=combined_df['Activity Count'],
            name="Activity Count",
            marker_color='blue',
            yaxis='y1'  # link to primary y-axis
        )
    )

    # Add a line chart for average RHR
    fig.add_trace(
        go.Scatter(
            x=combined_df['Week'],
            y=combined_df['Resting Heart Rate'],
            name='Average Resting Heart Rate',
            mode='lines+markers',
            line=dict(color='black'),
            yaxis='y2'  # link to Secondary y-axis
        )
    )

    # Update Layout
    fig.update_layout(
        title="How Weekly Activity Count Affects Resting Heart Rate",
        xaxis=dict(title="Week"),
        yaxis=dict(
            title=dict(
                text="Activity Count",
                font=dict(color="blue")  # Set font color for the title
            ),
            tickfont=dict(color="blue")  # Set font color for the ticks
        ),
        yaxis2=dict(
            title=dict(
                text="Resting Heart Rate",
                font=dict(color="black")  # Set font color for the title
            ),
            tickfont=dict(color="black"),  # Set font color for the ticks
            overlaying="y",  # Overlay on the same x-axis
            side="right"  # Place on the right-hand side
        ),
        legend=dict(title="Metrics"),
        barmode='group'
    )
    return fig


def create_stress_over_time_chart(df):
    """Create a chart for stress over time"""
    fig = px.line(
        df,
        x='Date',
        y='stress',
        title="Stress Over Time"
    )

    return fig


def create_rhr_over_time_chart(df):
    """Create a chart for stress over time"""
    fig = px.line(
        df,
        y='Resting Heart Rate',
        x='Date',
        title="RHR Over Time"
    )

    return fig


def display_visualizations(df):
    """Display visualizations in Streamlit."""
    fig1 = create_weekly_activities_chart(df)
    st.plotly_chart(fig1)

    st.markdown('<hr style="border:3px solid gray">', unsafe_allow_html=True)

    fig2 = create_stress_over_time_chart(df)
    st.plotly_chart(fig2)

    st.markdown('<hr style="border:3px solid gray">', unsafe_allow_html=True)

    fig3 = create_rhr_over_time_chart(df)
    st.plotly_chart(fig3)

    st.markdown('<hr style="border:3px solid gray">', unsafe_allow_html=True)

    fig4 = create_rhr_vs_weekly_activities(df)
    st.plotly_chart(fig4)

    st.markdown('<hr style="border:3px solid gray">', unsafe_allow_html=True)


def display_dataframe(df):
    # Display Dataframe
    st.write("Cleaned DataFrame")
    st.dataframe(df)
