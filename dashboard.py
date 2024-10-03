import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv(os.path.join(os.getcwd(), "data.csv"))

st.title("Tugas Akhir")
st.header("Course : Belajar Analisis Data")
st.text("Dataset : Brazilian E-Commerce Public Dataset by Olist")
st.text("Link    : https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_products_dataset.csv")

col1, col2 = st.columns(2)
 
with col1:
    st.subheader("Kategori Produk Terlaris (Last 6 Months)")
    sixmonthorders = data_df[data_df['recency'] <= 180]
    category_order_counts_6_months = sixmonthorders.groupby(by="product_category_name_english").order_id.nunique().sort_values(ascending=False)
    top_10_categories_6_months = category_order_counts_6_months[:10]
    colors =["#00008B","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080"]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x=top_10_categories_6_months.index, height=top_10_categories_6_months.values, color=colors)
    ax.set_xlabel("Kategori Produk")
    ax.set_ylabel("Orders")
    ax.set_title("10 Kategori Produk Terlaris (Last 6 Months)")
    plt.xticks(rotation=90)
    st.pyplot(fig)
    
    st.subheader("Kota Dengan Pembelian Terbanyak")
    city_order_counts = data_df.groupby(by="customer_city").order_id.nunique().sort_values(ascending=False)
    top_10_cities = city_order_counts[:10]
    colors =["#00008B","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080"]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x=top_10_cities.index, height=top_10_cities.values, color=colors)
    ax.set_xlabel("Kota")
    ax.set_ylabel("Orders")
    ax.set_title("10 Kota dengan Pembelian Terbanyak")
    plt.xticks(rotation=90)
    st.pyplot(fig)

with col2:
    st.subheader("Kategori Produk Terlaris (Last 30 Days)")
    recentorders = data_df[data_df['recency'] <= 30]
    category_order_counts = recentorders.groupby(by="product_category_name_english").order_id.nunique().sort_values(ascending=False)
    top_10_categories = category_order_counts[:10]
    colors =["#00008B","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080"]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x=top_10_categories.index, height=top_10_categories.values, color=colors)
    ax.set_xlabel("Kategori Produk")
    ax.set_ylabel("Orders")
    ax.set_title("10 Kategori Produk Terlaris (Last 30 Days)")
    plt.xticks(rotation=90)
    st.pyplot(fig)

    st.subheader("Kota Dengan Pembelian Watches & Gifts Terbanyak")
    watches_gifts_orders = data_df[data_df['product_category_name_english'] == 'watches_gifts']
    watches_gifts_counts = watches_gifts_orders.groupby('customer_city').order_id.nunique().sort_values(ascending=False)
    top_10_cities_watches_gifts = watches_gifts_counts[:10]
    colors =["#00008B","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080"]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x=top_10_cities_watches_gifts.index, height=top_10_cities_watches_gifts.values, color=colors)
    ax.set_xlabel("Kota")
    ax.set_ylabel("Orders")
    ax.set_title("10 Kota Pembeli Watches & Gifts Terbanyak")
    plt.xticks(rotation=90)
    st.pyplot(fig)

st.header("Kota Apa yang memiliki pelanggan terbanyak yang telah melakukan Recent Purchase(s) setidaknya dalam kurun waktu 1 bulan terakhir?")
st.subheader("Pertanyaan 1")

city_order_count = recentorders.groupby('customer_city').order_id.nunique().sort_values(ascending=False)
top_10_city = city_order_count[:10]
colors =["#00008B","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x=top_10_city.index, height=top_10_city.values, color=colors)
ax.set_xlabel("Kota")
ax.set_ylabel("Orders")
ax.set_title("10 Kota dengan Order Terbanyak (Last 30 days)")
plt.xticks(rotation=90)
st.pyplot(fig)

st.header("Bagaimana Performa Penjualan Produk dalam kurun tahun 2016 - 2018?")
st.subheader("Pertanyaan 2")

category_order_counts = data_df.groupby(by="product_category_name_english").order_id.nunique().sort_values(ascending=False)
top_10_categories = category_order_counts.head(10)
colors =["#00008B","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x=top_10_categories.index, height=top_10_categories.values, color=colors)
ax.set_xlabel("Kategori Produk")
ax.set_ylabel("Orders")
ax.set_title("10 Kategori Produk Terlaris")
plt.xticks(rotation=90)
st.pyplot(fig)

st.header("Kategori Produk Apa yang menghasilkan Pendapatan Terbanyak dalam kurun waktu 6 bulan terakhir?")
st.subheader("Pertanyaan 3")

category_payment_sum = sixmonthorders.groupby(by="product_category_name_english").payment_value.sum().sort_values(ascending=False)
top_10_categories_revenues = category_payment_sum.head(10)
colors =["#00008B","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080","#808080"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x=top_10_categories_revenues.index, height=top_10_categories_revenues.values, color=colors)
ax.set_xlabel("Kategori Produk")
ax.set_ylabel("Revenue")
ax.set_title("10 Kategori Produk Revenue Tertinggi (Last 6 Months)")
plt.xticks(rotation=90)
st.pyplot(fig)