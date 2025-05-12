import streamlit as st


def display_metrics(df):
    """Display key metrics in Streamlit"""
    total_distance = calculate_total_distance(df)
    total_calories = calculate_total_distance(df)
    total_elevation = calculate_total_elevation(df)
    total_steps = calculate_total_steps(df)