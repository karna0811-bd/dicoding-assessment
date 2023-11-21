import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

by_month_df = pd.read_csv("dashboard/most_sold_items_by_month.csv")
#by_month_df.head()
st.write(pd.DataFrame({
    by_month_df
}))