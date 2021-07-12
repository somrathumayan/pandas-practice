import pandas as pd
import json
df = pd.read_json('data.json')

print(df.to_string())
