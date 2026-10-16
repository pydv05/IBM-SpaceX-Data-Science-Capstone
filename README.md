# IBM Applied Data Science Capstone — SpaceX Falcon 9 Landing Prediction

This repository contains a reconstructed, runnable implementation of the IBM Applied Data Science Capstone
workflow used for the accompanying **Data Science Capstone Project Report**.

## Project objective

Predict whether the first stage of a Falcon 9 launch will land successfully and analyze the relationship
between launch site, payload, orbit, flight number, and landing outcome.

## Repository structure

```text
notebooks/
  01_Data_Collection_API.ipynb
  02_Web_Scraping.ipynb
  03_Data_Wrangling.ipynb
  04_EDA_Visualization.ipynb
  05_EDA_SQL.ipynb
  06_Folium_Map.ipynb
  07_Machine_Learning_Prediction.ipynb

dashboard/
  spacex_dash_app.py

sql/
  eda_queries.sql

data/
  README.md
report/
  Data Science Capstone Project Report.pdf
requirements.txt
```

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```

Run the notebooks in numerical order. The notebooks use the IBM Skills Network course datasets and the
public SpaceX REST API/Wikipedia source where appropriate.

To launch the dashboard:

```bash
python dashboard/spacex_dash_app.py
```

## Important note

These notebooks are an original reconstruction of the project workflow based on the final project report and
the IBM capstone methodology. They are not the original Coursera lab notebook files. Execute the notebooks
before relying on their generated outputs.

## Main tools

Python, Pandas, NumPy, Matplotlib, Seaborn, SQL/SQLite, Folium, Plotly Dash, and Scikit-learn.
