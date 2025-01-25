import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
dataset_path = 'food_coded.csv'  # Replace this with the correct file path if needed
data = pd.read_csv(dataset_path)
# Display initial dataset info
print("Initial Dataset Info:")
print(data.info())
print("\nPreview of the Dataset:")
print(data.head())
# Plot missing values before cleaning
missing_before = data.isnull().sum()
print("\nMissing Values Before Cleaning:")
print(missing_before)
missing_before.plot(kind='bar', title='Missing Values Before Cleaning', figsize=(10, 6))
plt.show()

# Step 1: Handle Missing Values
# Fill missing values in numerical columns with the mean
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    mean_value = data[column].mean()
    data[column] = data[column].fillna(mean_value)  # Reassign column after fillna
    print(f"Filled missing values in numerical column '{column}' with mean: {mean_value}")

# Fill missing values in categorical columns with the mode
for column in data.select_dtypes(include=['object']).columns:
    mode_value = data[column].mode()[0]
    data[column] = data[column].fillna(mode_value)  # Reassign column after fillna
    print(f"Filled missing values in categorical column '{column}' with mode: {mode_value}")

# Step 2: Remove Duplicates
# Drop duplicate rows
initial_row_count = data.shape[0]
data = data.drop_duplicates()
final_row_count = data.shape[0]
print(f"Removed {initial_row_count - final_row_count} duplicate rows.")

# Drop duplicate columns
data = data.loc[:, ~data.columns.duplicated()]
print("Removed duplicate columns, if any.")

# Save the cleaned dataset
cleaned_dataset_path = 'cleaned_food_coded.csv'
data.to_csv(cleaned_dataset_path, index=False)
print(f"\nCleaned dataset saved as '{cleaned_dataset_path}'")

# Step 3: Display final dataset info
print("\nCleaned Dataset Info:")
print(data.info())
print("\nPreview of the Cleaned Dataset:")
print(data.head())

# Plot missing values after cleaning
missing_after = data.isnull().sum()
print("\nMissing Values After Cleaning:")
print(missing_after)
missing_after.plot(kind='bar', title='Missing Values After Cleaning', figsize=(10, 6))
plt.show()

# Assert no missing values remain
assert not data.isnull().values.any(), "Dataset still contains missing values."
assert data.shape[0] > 0, "Dataset is empty after cleaning!"
