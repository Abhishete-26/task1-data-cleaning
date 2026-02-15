import pandas as pd
import os

# Load Dataset
df = pd.read_csv("medical_appointments.csv")

print("Original Shape:", df.shape)

# Check Missing Values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Remove Duplicates
df = df.drop_duplicates()
print("\nShape After Removing Duplicates:", df.shape)

# Rename Columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Standardize Gender
df['gender'] = df['gender'].str.upper()

# Convert Date Columns
df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# Fix Age Type
df['age'] = df['age'].astype(int)

# Remove Negative Age
df = df[df['age'] >= 0]

# Show Save Location
print("Current Working Directory:", os.getcwd())

# Save Cleaned File
df.to_csv("cleaned_medical_appointments.csv", index=False)

print("\nCleaning Completed Successfully ✅")
print("Final Shape:", df.shape)
