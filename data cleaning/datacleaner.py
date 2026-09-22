import pandas as pd
df1=pd.read_csv(r"C:\Users\user\Downloads\football transfer market\players.csv")
data=df1.drop(["player_id","first_name","last_name","name","date_of_birth","contract_expiration_date","agent_name","image_url","international_caps","international_goals","current_national_team_id","current_club_domestic_competition_id","current_club_name","market_value_in_eur","highest_market_value_in_eur","url"],axis=1)
df=data.dropna(subset=["country_of_birth"])
df=df.dropna(subset=["sub_position"])
df=df.dropna(subset=["foot"])
df["height_in_cm"]=df["height_in_cm"].fillna(df["height_in_cm"].mean())
df.to_csv(r"C:\Users\user\OneDrive\Desktop\football transfer prediction\data cleaning\output.csv", index=False)