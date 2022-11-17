import pandas as pd

data=pd.read_csv(r'C:\Users\test\Desktop\csv\Giants1.csv')
df=pd.DataFrame(data,columns=['CEO','Established'])

print(df)