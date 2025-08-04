import pandas as pd

data=pd.read_csv(r"C:\Users\PAKML\Documents\sales_data.csv.zip")

df=pd.DataFrame(data)

#checks Null Values
#print(df.isnull().values.any())

#checks Duplicated values and removed duplicates
print(df.duplicated().sum())
df=df.drop_duplicates()

#removes extra space
for col in df.select_dtypes(include='object').columns:
    df[col]=df[col].str.strip()

df.columns=df.columns.str.strip('_')

#Extracing only the group not along with age
df['Age_Group']=df['Age_Group'].str.extract(r'(^[A-Za-z\s]+)',expand=False).str.strip()

#Replacing Values
df['Customer_Gender']=df['Customer_Gender'].str.strip().str.upper().replace({'M':'Male','F':'Female'})

#Calculating Revenue
df['Revenue']=df['Order_Quantity'] * df['Unit_Price']

#Caculating Profit
df['Profit']=df['Revenue'] - df['Cost']

#Changed Datatype
df['Date']=pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')


df.drop(columns=['Day','Month','Year'],inplace=True)

#Changed column names
df.rename(columns={'Customer_Age':'Age','Customer_Gender':'Gender'}, inplace=True)

#Cleaned Data Ready for     
print(df)
output=df.to_csv(r"C:\Users\PAKML\Downloads\Final_sales_data.csv",index=False)
