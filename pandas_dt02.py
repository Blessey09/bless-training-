import pandas as pd
# using dict data ---> Df
data={'Country':['Belgium','India','Brazil'],
'Capital':['Brussels','Delhi','Brasilia'],
'Population':[123456,98765,34567]}

#df=pd.DataFrame(data,columns=['Country','Capital','Population'])
df=pd.DataFrame(data,columns=['Customer_Region','City','Population'])
print(df)