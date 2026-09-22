from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pandas as pd
df=pd.read_csv(r"C:\Users\user\OneDrive\Desktop\football transfer prediction\data cleaning\output.csv")
from sklearn.preprocessing import OneHotEncoder

columns = [
    "current_club_id",
    "player_code",
    "country_of_birth",
    "city_of_birth",
    "country_of_citizenship",
    "sub_position",
    "position",
    "foot"
]

encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

encoded = encoder.fit_transform(df[columns])

encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(columns),
    index=df.index
)

df = pd.concat([df.drop(columns=columns), encoded_df], axis=1)
