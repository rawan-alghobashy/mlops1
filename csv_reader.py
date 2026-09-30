import pandas as pd

# Ask the user to enter the CSV file path
file_path = input("Enter the path to your CSV file: ")

try:
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Print the first 3 rows
    print("\nFirst 3 rows of the CSV file:")
    print(df.head(3))

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

except Exception as e:
    print(f"Error reading the CSV file: {e}")