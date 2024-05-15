import openai
import os
import pandas as pd  # Import pandas for data manipulation
from datetime import datetime

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Load the dataset and ensure 'InvoiceDate' is converted to datetime
data_path = "C:\\!Projects\\DI-Bootcamp\\Week9\\online_retail_II.csv"
try:
    df = pd.read_csv(data_path)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    print("Dataset loaded and date converted successfully.")
except Exception as e:
    print(f"Failed to load dataset: {e}")

# Function to generate Python code for RFM analysis using the OpenAI API
def generate_code_for_rfm_analysis(df):
    # Define the prompt with specific requirements
    prompt = (f"""Analyze the dataset: {df}.\n
              You have a dataset containing transactional information including 'InvoiceDate', 'Quantity', and 'Price' for each purchase made by customers . 
              Your task is to calculate RFM (Recency, Frequency, Monetary) scores for each customer based on this data. 
              Write a python code for it.
              """)
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000
    )
    # Extract and print the generated Python code
    generated_code = response.choices[0].text
    print("Generated Code:\n", generated_code)

    # Evaluate the generated code
    try:
        exec(generated_code, globals())
    except Exception as e:
        print(f"Failed to execute generated code: {e}")

# Call the function with the dataframe
generate_code_for_rfm_analysis(df)
