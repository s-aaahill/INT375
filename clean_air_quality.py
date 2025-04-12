import pandas as pd

df = pd.read_csv("Air_quality.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Drop completely empty rows
df.dropna(how='all', inplace=True)

# Forward fill missing values
df.fillna(method='ffill', inplace=True)

# Convert datetime columns if any
for col in df.columns:
    if 'date' in col or 'time' in col:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Save cleaned file
df.to_csv("cleaned_air_quality.csv", index=False)
print("Cleaned data saved to cleaned_air_quality.csv")
