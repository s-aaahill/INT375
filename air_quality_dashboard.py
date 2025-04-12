import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")
df = pd.read_csv("cleaned_air_quality.csv")

st.title("🌫️ Air Quality Insights Dashboard")

with st.expander("Raw Data"):
    st.dataframe(df)

# Numeric columns
num_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

# Distribution
col = st.selectbox("Select column to view distribution", num_cols)
st.subheader(f"Distribution of {col}")
fig1, ax1 = plt.subplots()
sns.histplot(df[col], kde=True, ax=ax1)
st.pyplot(fig1)

# Boxplot
st.subheader(f"Boxplot of {col}")
fig2, ax2 = plt.subplots()
sns.boxplot(x=df[col], ax=ax2)
st.pyplot(fig2)

# Correlation matrix
st.subheader("Correlation Matrix")
fig3, ax3 = plt.subplots()
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)
