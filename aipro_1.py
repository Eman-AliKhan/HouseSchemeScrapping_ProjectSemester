import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ===============================
# Load and Prepare Data
# ===============================
df = pd.read_csv("zameen_peshawar_houses.csv")

# --- Price cleaning function ---
def clean_price(price):
    if pd.isna(price):
        return None
    p = str(price).replace("PKR", "").replace(",", "").strip()
    if "Crore" in p:
        return float(p.replace("Crore", "").strip()) * 1e7
    elif "Lakh" in p:
        return float(p.replace("Lakh", "").strip()) * 1e5
    else:
        try:
            return float(p)
        except:
            return None

df["Price_Clean"] = df["Price"].apply(clean_price)

# --- Ensure Area column exists ---
if "Area" not in df.columns and "Area (Marla)" in df.columns:
    df["Area"] = pd.to_numeric(df["Area (Marla)"], errors="coerce")
else:
    df["Area"] = pd.to_numeric(df.get("Area"), errors="coerce")

# Ensure Beds & Baths are numeric
df["Beds"] = pd.to_numeric(df["Beds"], errors="coerce")
df["Baths"] = pd.to_numeric(df["Baths"], errors="coerce")

# ===============================
# Sidebar Filters
# ===============================
st.sidebar.header("🔍 Filter Listings")

# Location filter
locations = sorted(df["Location"].dropna().unique())
selected_locations = st.sidebar.multiselect("Select Locations", locations, default=locations)

# Price filter
min_price = int(df["Price_Clean"].min() or 0)
max_price = int(df["Price_Clean"].max() or 100000000)
price_range = st.sidebar.slider("Select Price Range (PKR)", min_price, max_price, (min_price, max_price))

# Beds filter
bed_options = sorted(df["Beds"].dropna().unique())
selected_beds = st.sidebar.multiselect("Select Number of Beds", bed_options, default=bed_options)

# Apply filters
filtered_df = df[
    (df["Location"].isin(selected_locations)) &
    (df["Price_Clean"] >= price_range[0]) &
    (df["Price_Clean"] <= price_range[1]) &
    (df["Beds"].isin(selected_beds))
]

# ===============================
# Main Title
# ===============================
st.title("🏠 Peshawar Houses Data Analysis")

# Show dataset preview
if st.checkbox("Show filtered data table"):
    st.write(filtered_df)

# ===============================
# 💰 Price Distribution (Bar Chart)
# ===============================
st.subheader("💰 Price Distribution")

price_bins = [0, 5000000, 10000000, 20000000, 50000000, 100000000]
price_labels = ["0–50L", "50L–1Cr", "1–2Cr", "2–5Cr", "5Cr+"]

filtered_df["Price_Range"] = pd.cut(filtered_df["Price_Clean"], bins=price_bins, labels=price_labels)
price_counts = filtered_df["Price_Range"].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.bar(price_counts.index.astype(str), price_counts.values, color=plt.cm.Paired.colors, edgecolor="black")
ax1.set_xlabel("Price Range")
ax1.set_ylabel("Number of Houses")
ax1.set_title("Number of Houses by Price Range")
ax1.bar_label(ax1.containers[0])
st.pyplot(fig1)

# ===============================
# 🛏 Beds Distribution (Pie Chart)
# ===============================
st.subheader("🛏 Beds Distribution")

bed_counts = filtered_df["Beds"].value_counts()

fig2, ax2 = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax2.pie(
    bed_counts,
    labels=bed_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.tab20.colors,
    pctdistance=0.85
)
plt.setp(autotexts, size=9, weight="bold", color="white")
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight("bold")

ax2.set_title("Distribution of Houses by Number of Beds", fontsize=14)
st.pyplot(fig2)

# ===============================
# 🛁 Price vs Baths (Bar Chart)
# ===============================
st.subheader("🛁 Average Price by Number of Bathrooms")

if not filtered_df["Baths"].dropna().empty:
    avg_price_baths = filtered_df.groupby("Baths")["Price_Clean"].mean()
    fig3, ax3 = plt.subplots(figsize=(7, 4))
    sns.barplot(x=avg_price_baths.index, y=avg_price_baths.values, palette="viridis", ax=ax3)
    ax3.set_xlabel("Number of Bathrooms")
    ax3.set_ylabel("Average Price (PKR)")
    ax3.set_title("Average Price by Bathrooms")
    for i, v in enumerate(avg_price_baths.values):
        ax3.text(i, v, f"{v:,.0f}", ha='center', va='bottom', fontsize=8)
    st.pyplot(fig3)
else:
    st.warning("No bathroom data available for the current selection.")
