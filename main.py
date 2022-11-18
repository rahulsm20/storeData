import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st 
import altair as at

ex=pd.read_excel('./superStore.xls')

# Category to Sales graph
# ex=pd.read_excel('./superStore.xls')
# plt.bar(ex.Category,ex.Sales)
# plt.plot()
# plt.show()

# Sales data by States
# plt.bar(ex.State,ex.Sales)
# plt.title('Sales data by States')
# plt.xlabel('State -->')
# plt.ylabel('Sales in $')
# plt.xticks(rotation='vertical')
# plt.legend()
# plt.show()

# Sales data by Sub-Category
# plt.bar(ex['Sub-Category'],ex.Sales)
# plt.title('Sales by Category')
# plt.xlabel('Category')
# plt.ylabel('Sales in $')
# plt.xticks(rotation='vertical')
# plt.show()

# # Pie chart for delivery types
# sameDay=ex.loc[ex['Ship Mode']=='Same Day'].count()[0]
# standardClass=ex.loc[ex['Ship Mode']=='Standard Class'].count()[0]
# firstClass=ex.loc[ex['Ship Mode']=='First Class'].count()[0]
# secondClass=ex.loc[ex['Ship Mode']=='Second Class'].count()[0]
# print('Same Day:',sameDay,'\n','Standard Class:',standardClass,'\n',
#       'First Class:',firstClass,'\n','Second Class',secondClass)
# plt.pie([sameDay,standardClass,firstClass,secondClass])
# plt.show()

# # Pie chart for distribution of orders among california, new york and florida
# requiredStates = ['California','New York','Florida']
# caliOrders=ex.loc[ex.State=='California'].count()[0]
# nyOrders=ex.loc[ex.State=='New York'].count()[0]
# flOrders=ex.loc[ex.State=='Florida'].count()[0]
# print(caliOrders,nyOrders,flOrders)
# majStates=[caliOrders,nyOrders,flOrders]
# plt.pie([caliOrders,nyOrders,flOrders],labels=requiredStates,autopct='%.2f %%')
# plt.title('Distribution of orders among the most popular states')
# plt.legend()
# plt.show()

# id=[1,2,3,4,5]
# names=['Mark','James','Harry','Pete','Kate']
# db=pd.DataFrame({'ID':id,'Name':names},index=['A','B','C','D','E'])
# db['USN']=db['ID']+100
# di=db['USN']
# db['Marks']=[24.5,25.0,26.7,23.9,25.0]
# df = db['Marks']
# print(db.iloc[0:3])
# print('Average marks:',df.mean(),'\n','Median:',df.median(),'\n','Mode:',df.mode())   
# arr=np.array([1,2,3,4])
# plt.plot(df,di,label='2x')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.title('Marks',fontdict={'fontname':'Times New Roman','fontsize':20})
# x=[1,2,3,4]
# y=[24,28,21,30]
# bars=plt.bar(x,y)
# bars[0].set_hatch('o')
# plt.figure(figsize=(5,3),dpi=100)
# print(ex.columns)
# plt.savefig('sampleGraph1.png')
# plt.figure((4,3))
# for State in ex:
#     if State == requiredStates:
#         plt.bar(ex.State,ex.Sales)
# plt.show()        
# print(sorted(set(ex.State)))
# print(ex.columns)

# # Pie chart 
# states = ex.State.value_counts()
# plt.pie(states,autopct='%.2f %%')
# plt.show()

# image=Image.open('./Figure_1.png')

# st.write("""
# # Simple Math app

# ***         """
# )
# st.header('Sin X graph')
# st.image(image,use_column_width=True)
# values="For x=0, Sin X = Sin 0° = 0\nFor x=30, Sin X = Sin 30° = 1/√2"
# st.text_area('The graph above represents the change in value between the value of x and sinx',values)
# values=values.splitlines()
# values

ex= ex.drop(['Order ID','Row ID','Ship Date','Order Date',
             'Customer ID','Customer Name','Product Name',
             'Quantity','Postal Code'],axis=1)

#Objectives



st.write("""
         # SuperStore Data Analysis 
         ***    
         In this project, we have aimed to analyse 
         the sales data of the super store
         and provide useful insight into it's customer's
         preferences.
         """)
st.write("""
         #### Sales by Category
         """)
category=np.array(ex.Category)
sales=np.array(ex.Sales)
states=np.array(ex.State)
salesByCategory=pd.DataFrame(sales,category)
st.bar_chart(salesByCategory)
salesByState=pd.DataFrame(sales,states)
st.bar_chart(salesByState)
