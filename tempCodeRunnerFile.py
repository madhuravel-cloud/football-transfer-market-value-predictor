import pandas as pd

df1=pd.read_csv(r"C:\Users\user\Downloads\football transfer market\players.csv")
df2=pd.read_csv(r"C:\Users\user\Downloads\football transfer market\player_valuations.csv")
df3=pd.read_csv(r"c:\Users\user\Downloads\football transfer market\transfers.csv")
df4=pd.read_csv(r"C:\Users\user\Downloads\football transfer market\appearances.csv")
common=df1["player_id"]

common=common.intersection(df2["player_id"])
common=common.intersection(df3["player_id"])
common=common.intersection(df4["player_id"])

print(common)