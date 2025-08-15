# 🌍 Global Weather Data Analysis & Interactive Dashboard

This project performs **Exploratory Data Analysis (EDA)** and builds an **interactive Streamlit dashboard** to explore global weather patterns.  
It uses weather observations such as **temperature, humidity, wind speed, precipitation, and air quality** to uncover insights and trends.

---

## 📂 Project Structure

```
GlobalWeatherRepository_EDA/
│
├── app.py                                  # Streamlit dashboard application
├── data/
│   └── raw/
│       └── GlobalWeatherRepository.csv     # Weather dataset
├── GlobalWeather_EDA_Notebook_FIXED.ipynb  # EDA Jupyter Notebook
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

---

## 📊 Dataset Description

The dataset (`GlobalWeatherRepository.csv`) contains weather metrics for multiple locations across the globe.  
**Key columns include:**

| Column Name                           | Description |
|---------------------------------------|-------------|
| `country`                             | Country name |
| `location_name`                       | Name of the location or city |
| `latitude`, `longitude`               | Geographic coordinates |
| `timezone`                            | Time zone of location |
| `last_updated`                        | Date & time of record update |
| `temperature_celsius` / `temperature_fahrenheit` | Recorded temperature |
| `condition_text`                      | Weather description (e.g., "Clear", "Rain") |
| `wind_kph`, `wind_mph`                 | Wind speed |
| `humidity`                            | Humidity percentage |
| `precip_mm`, `precip_in`               | Precipitation |
| `pressure_mb`, `pressure_in`           | Atmospheric pressure |
| `air_quality_*`                        | Air quality metrics (CO, O3, NO₂, SO₂, PM2.5, PM10) |
| `sunrise`, `sunset`                    | Sunrise & sunset times |
| `moon_phase`                           | Moon phase information |

---

## 🔍 Notebook Workflow

The **GlobalWeather_EDA_Notebook_FIXED.ipynb** performs:

1. **Data Loading & Inspection**
   - Load CSV
   - Inspect structure, column names, data types
   - Check missing values

2. **Data Cleaning**
   - Remove or impute missing values
   - Clip extreme outliers (temperature, wind speed)
   - Standardize column names

3. **Exploratory Data Analysis (EDA)**
   - Descriptive statistics
   - Histograms & box plots for temperature, humidity, wind speed
   - Correlation matrix for numerical features
   - Geographic visualization using latitude & longitude
   - Seasonal and location-based trends

4. **Modeling (Basic)**
   - Linear regression to predict temperature from humidity & wind speed
   - Evaluate R² score and interpret results

5. **Interactive Dashboard Prep**
   - Prepare cleaned dataset for visualization
   - Rename and reformat columns
   - Filterable fields for the dashboard

6. **Findings & Next Steps**
   - Temperature patterns realistic after outlier clipping
   - Wind speed anomalies removed
   - Humidity is a stronger predictor of temperature than wind speed
   - Missing columns (e.g., solar radiation, cloud cover) could improve predictions
   - Suggest adding time-series models (ARIMA, Prophet, LSTM)

---

## 📈 Streamlit Dashboard Features

The **app.py** dashboard allows:

- **Filters**:
  - Country selection
  - City selection
  - Date/time filtering based on `last_updated`
- **Visualizations**:
  - Temperature trends over time
  - Humidity vs Temperature scatter plot (bubble = wind speed)
  - Monthly temperature distribution
- **Insights**:
  - Displays key EDA findings and suggestions

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GlobalWeatherRepository_EDA.git
   cd GlobalWeatherRepository_EDA
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Dashboard

1. Place your dataset in:
   ```
   data/raw/GlobalWeatherRepository.csv
   ```
2. Run the dashboard:
   ```bash
   streamlit run app.py
   ```
3. Open the **Local URL** (e.g., http://localhost:8501) in your browser.

---

## 📌 Key Findings from EDA

- **Temperature**: After removing extreme outliers, values are within realistic ranges.
- **Wind Speed**: Clipped to 1st–99th percentile.
- **Humidity**: Stronger correlation with temperature compared to wind speed.
- **Geographic Trends**: Clear seasonal differences between regions.
- **Data Gaps**: Some metrics have missing values that could affect models.

---

## 🚀 Next Steps

- Fill missing values with interpolation or by merging with external datasets
- Add meteorological variables such as solar radiation & cloud cover
- Create lag features & rolling averages
- Apply advanced models (Random Forest, XGBoost, Gradient Boosting)
- Build time-series forecasting models for temperature & humidity

---

## 📧 Author
Developed by Mohammed Jamshir
