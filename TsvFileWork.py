#WORKING WITH CSV FILE AND HOW CAN WE HANDLE DATA IN CSV
import pandas as pd
#SEP PARAMETER
df=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.tsv",sep="\t",names=['id','year','Team1',"team2",'Winner','Venue','Runs by player'])
print(df)
#INDEX_COLS PARAMETER
df1=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.csv",index_col='match_id')
print(df1)
#HEADER PARAMETER
df2=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.csv",header=1)
print(df2)
#USE COLS PARAMETER
df3=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.csv",usecols=['match_id','team1','team2','winner'],index_col='match_id')

print(df3)
#SKIPSROW PARAMETER
df4=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_clean_dataset.csv",skiprows=[5,6,7])
print(df4)
#BAD LINES PARAMETER
s=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.tsv",sep='\t',on_bad_lines="skip")
print(s)
#DATA TYPES CHANGE 
t=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.tsv",sep='\t',dtype={'runs':'Int64'})
print(t)
print(t.dtypes)
#DROPNA
t=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.tsv",sep="\t")
df_clean=t.dropna()
print(df_clean)
#CONVERTORS
def rename(name):
    if name=="RCB":
        return "Royal challengers banglore"
    else:
        return name
rename("RCB")

y=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.csv",converters={'team1':rename})
print(y)
#HANDLING DATES
z=pd.read_csv(r"C:\Users\shlok\OneDrive\Desktop\BasicsOfML\ipl_dataset.csv",parse_dates=['season'])
print(z)