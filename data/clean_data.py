import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Remove missing values
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning completed successfully!")
