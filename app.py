import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------
# Load & Prepare Data
# -------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/GlobalWeatherRepository.csv")
    
    # Convert last_updated to datetime
    if 'last_updated' in df.columns:
        df['last_updated'] = pd.to_datetime(df['last_updated'], errors='coerce')
        df = df.dropna(subset=['last_updated'])
    
    # Standardize column names
    if 'location_name' in df.columns:
        df.rename(columns={'location_name': 'city'}, inplace=True)
    
    return df

df = load_data()

# -------------------
# Sidebar Filters
# -------------------
st.sidebar.header("Filter Weather Data")

# Country filter
country_list = df['country'].dropna().unique()
selected_country = st.sidebar.selectbox("Select Country", options=["All"] + sorted(country_list.tolist()))

# City filter
if selected_country != "All":
    city_list = df[df['country'] == selected_country]['city'].dropna().unique()
else:
    city_list = df['city'].dropna().unique()
selected_city = st.sidebar.selectbox("Select City", options=["All"] + sorted(city_list.tolist()))

# Date filter
min_date, max_date = df['last_updated'].min(), df['last_updated'].max()
selected_date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

# -------------------
# Apply Filters
# -------------------
filtered_df = df.copy()
if selected_country != "All":
    filtered_df = filtered_df[filtered_df['country'] == selected_country]
if selected_city != "All":
    filtered_df = filtered_df[filtered_df['city'] == selected_city]
filtered_df = filtered_df[
    (filtered_df['last_updated'] >= pd.to_datetime(selected_date_range[0])) &
    (filtered_df['last_updated'] <= pd.to_datetime(selected_date_range[1]))
]

# -------------------
# Dashboard Layout
# -------------------
st.title("🌍 Global Weather Dashboard")
st.markdown("Interactive weather data visualization with filtering by country, city, and date range.")

# Line chart: Temperature trend
if not filtered_df.empty:
    fig_temp = px.line(filtered_df, x="last_updated", y="temperature_celsius",
                       color="city", title="Temperature Trends Over Time")
    st.plotly_chart(fig_temp, use_container_width=True)

    # Scatter: Humidity vs Temperature
    fig_scatter = px.scatter(filtered_df, x="humidity", y="temperature_celsius",
                             size="wind_kph", color="city",
                             title="Humidity vs Temperature (Bubble Size = Wind Speed)")
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Box plot: Temperature distribution by month
    filtered_df['month'] = filtered_df['last_updated'].dt.month_name()
    fig_box = px.box(filtered_df, x="month", y="temperature_celsius",
                     title="Monthly Temperature Distribution")
    st.plotly_chart(fig_box, use_container_width=True)
else:
    st.warning("No data available for the selected filters.")

# -------------------
# EDA Summary
# -------------------
st.header("📌 Key Findings & Next Steps")
st.markdown("""
- **Temperature patterns**: After removing extreme outliers, values are realistic.
- **Wind speed**: Outliers removed within 1st–99th percentile range.
- **Missing data**: Several columns have notable missing values.
- **Location insights**: Seasonal/local variations can be seen in the dashboard.
- **Model**: Linear regression with humidity & wind_kph had moderate R²; humidity more correlated than wind speed.
- **Improvements**:
    - Fill missing values (interpolation, merge with other datasets)
    - Add more weather variables (solar radiation, cloud cover)
    - Use time-series forecasting models for trend prediction
""")
