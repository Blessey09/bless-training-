#python codedemonstrate creating
#DataFrame from dict narray/lists
#by default addresss

import pandas as pd

#initialize data of lists
data={'Name':['Tom','nick','krish','jack'],'Age':[21,21,19,18]}

#create DataFrame
df=pd.DataFrame(data)

#print the output
print(df)