import openai
import os
import pandas as pd  # Import pandas for data manipulation

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

def generate_answer(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text},
            ]
        )
        # Extract and concatenate messages from the response
        result = ''
        for message in response['choices'][0]['message']['content']:
            result += message

        return result

    except Exception as e:
        return f"Oops!! Some problems with OpenAI. Reason: {e}"

# Path to your dataset
data_path = "C:\\!Projects\\DI-Bootcamp\\Week9\\online_retail_II.csv"

# Load the dataset to confirm it is accessible (Optional, remove if not needed)
try:
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Failed to load dataset: {e}")

# Detailed description of the dataset structure for the prompt
dataset_description = f"""
You have a dataset located at '{data_path}' containing transactional information for a series of customer purchases. Each record includes the following fields:
- 'Customer ID': A unique identifier for each customer.
- 'InvoiceDate': The date and time of the transaction, indicating when the purchase was made.
- 'Quantity': The number of items purchased in that transaction.
- 'Price': The price per item in that transaction.
Your task is to calculate RFM (Recency, Frequency, Monetary) scores for each customer based on this data. This involves:
- Recency: Calculating the number of days since the last purchase for each customer.
- Frequency: Counting the total number of transactions for each customer.
- Monetary: Calculating the total amount spent by each customer.
"""

# Function to generate and execute Python code for RFM analysis using the OpenAI API
def execute_python_code_for_rfm_analysis():
    prompt_text = f"""
Based on the dataset described below, write Python code to calculate RFM scores for each customer:
{dataset_description}
The Python code should use pandas library to handle the dataset and perform the necessary calculations. Include comments in the code to explain the steps.
"""
    
    # Generate the code using the OpenAI API
    generated_code = generate_answer(prompt_text)
    print("Generated Code:\n", generated_code)
    
    # Execute the generated Python code
    try:
        exec(generated_code, globals())
    except Exception as e:
        print(f"Failed to execute generated code: {e}")

# Execute the RFM analysis
execute_python_code_for_rfm_analysis()