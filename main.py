import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ex=pd.read_excel('./superStore.xls')
#Category to Sales graph
# ex=pd.read_excel('./superStore.xls')
# plt.bar(ex.Category,ex.Sales)
# plt.plot()
# plt.legend()
# plt.show()

#Sales data by States
plt.bar(ex.State,ex.Sales)
plt.title('Sales data by States')
plt.xlabel('State -->')
plt.ylabel('Sales in $')
plt.xticks(rotation='vertical')
plt.legend()
plt.show()
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

requiredStates = ['California','Florida','New York']
# plt.figure((4,3))
# for State in ex:
#     if State == requiredStates:
#         plt.bar(ex.State,ex.Sales)
# plt.show()        
# print(sorted(set(ex.State)))
