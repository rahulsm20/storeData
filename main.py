import pandas as pd
import numpy as np
import streamlit as st 
import matplotlib.pyplot as plt
import altair as alt
from ing_theme_matplotlib import mpl_style
df=pd.read_excel('./superStore.xls')

mpl_style('dark')
df= df.drop(['Order ID','Row ID',
             'Customer ID','Customer Name','Product Name',
             'Postal Code','Product ID'],axis=1)

st.write("""
         # SuperStore Data Analysis 
         ***    
         In this project, we have aimed to analyse 
         the sales data of the super store
         and provide useful insight into customer preferences.
         """)
st.write(df.head())

st.markdown("""
            ## Content  
            \n - [Sales by State](#sales-by-state)  
            \n - [Sales by Region](#sales-distribution-by-region) 
            \n - [Sales by Ship mode](#sales-distribution-by-ship-mode)
            \n - [Sales by Category](#sales-by-category)
            \n - [Sales distribution by segment](#sales-by-segment) 
            \n - [Sales distribution by Sub-Category](#sales-distribution-by-sub-category)
            \n - [Sales by Date](#sales-by-date)
            \n - [Results](#results)
            """)
df['Sales']=df['Sales'].round(1)
salesByState=df.groupby('State')['Sales'].sum()
salesByCategory=df.groupby('Category')['Sales'].sum()
st.write("""
         #### Sales by State
         """)
st.write(salesByState)
st.bar_chart(salesByState,y='Sales')
st.write("""
         #### Sales by Category
         """)
st.bar_chart(salesByCategory)
fig,ax=plt.subplots()
ax.pie(salesByCategory,labels=salesByCategory.keys(),autopct='%1.1f%%')
st.pyplot(fig)

st.write("""
         #### Sales distribution by Ship Mode    
         """)
shipmode=df.groupby('Ship Mode')['Sales'].sum()
st.write(shipmode)
st.bar_chart(shipmode,y='Sales')

fig,ax=plt.subplots()
ax.pie(shipmode.values,labels=shipmode.keys(),autopct='%1.1f%%')
st.pyplot(fig)

st.write('### Sales distribution by Region')
region=df.groupby('Region')['Sales'].sum()
st.write(region)
st.bar_chart(region,y='Sales')
fig,ax=plt.subplots()
ax.pie(region,labels=region.keys(),autopct='%1.1f%%')
st.pyplot(fig)


st.write('### Sales distribution by segment')
segment=df.groupby('Segment')['Sales'].sum()
st.write(segment)
st.bar_chart(segment,y='Sales')
fig,ax=plt.subplots()
ax.pie(segment,labels=segment.keys(),autopct='%1.1f%%')
st.pyplot(fig)

st.write('### Sales distribution by Sub-Category')
subcategory=df.groupby('Sub-Category')['Sales'].sum()
st.write(subcategory)
st.bar_chart(subcategory,y='Sales')
explode=[0.2]*len(subcategory)
fig,ax=plt.subplots()
ax.pie(subcategory,labels=subcategory.keys(),autopct='%1.1f%%',explode=explode)
st.pyplot(fig)

st.write('### Profit by Sub-Category')
subcategory=df.groupby('Sub-Category')['Profit'].sum()
st.bar_chart(subcategory)

st.write('### Sales by Date')
date=df.groupby('Order Date')['Sales'].sum()
st.write(date)
st.area_chart(date,y='Sales')

df.set_index(['Category', 'Order Date'], inplace=True)
categoryDateSales=df.groupby(['Category','Order Date'])['Sales'].sum().reset_index()
st.altair_chart(alt.Chart(categoryDateSales).mark_area().encode(
    x='Order Date:T',
    y='Sales:Q',
    color='Category:N',
    tooltip=['Category:N', 'Order Date:T','Sales:Q']
),use_container_width=True)

st.write('### Profit by Date')

date=df.groupby('Order Date')['Profit'].sum()
st.write(date)
st.line_chart(date,y='Profit')

categoryDate=df.groupby(['Category','Order Date'])['Profit'].sum().reset_index()
st.altair_chart(alt.Chart(categoryDate).mark_area().encode(
    x='Order Date:T',
    y='Profit:Q',
    color='Category:N',
    tooltip=['Category:N', 'Order Date:T','Profit:Q']
),use_container_width=True)


st.write('### Results')
st.markdown("""  
\n * The stores makes the most revenue in terms of sales from the state of California, followed by New York, Texas, Washington and Pennsylvania in that order.
* Over 50% of the store's revenue comes from consumer goods, followed by corporate and home-office in that order.
* The store offers multiple types of shipping modes, but the standard class is by far the most popular.
* The store has branches all over the country and the sales distribution is well spread out. The West brings in the most though, at 31.6% followed by East, Central and South.
* Copiers are the most profitable sub-category of products, whereas tables are the least profitable, actually producing a net loss.
* Continuing with sub-categories, Phones bring in the most revenue at 14.4% followed closely by Chairs at 14.3%""")
