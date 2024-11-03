from datetime import datetime  # Import datetime module
import pandas as pd 

def convert_to_datetime(date_str):
    """
    Convert a given date string to a standard datetime object.
    Supports various formats, modify as needed.
    """
    try:
        if pd.isnull(date_str) or date_str == '':
            return None  # Handle missing or empty dates as None
        return datetime.strptime(str(date_str), "%m/%d/%Y")  # Modify the format as per your data
    except ValueError:
        return None

def test_convert_to_datetime():
    # Test case: valid date format
    input_date = "12/31/2023"
    expected_output = datetime(2023, 12, 31)
    
    result = convert_to_datetime(input_date)
    assert result == expected_output, f"Test failed: Expected {expected_output}, got {result}"
    print(f"Actual result: {result}")

# Run the test function
test_convert_to_datetime()

