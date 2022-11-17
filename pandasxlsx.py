import pandas as pd

data=pd.read_excel(r'C:\Users\test\Desktop\csv\Companies.xlsx')
df=pd.DataFrame(data,columns=['CEO'])
print(df)