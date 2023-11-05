import pandas as pd
import unicodedata

def remove_accent_marks(dataframe, column_name):
    """
    This function identifies names with accent marks in a specific column of a pandas DataFrame and replaces them
    with the same name without the accent mark.
    
    Parameters:
    dataframe (pandas.DataFrame): The DataFrame containing the data
    column_name (str): The name of the column to process
    
    Returns:
    pandas.DataFrame: The modified DataFrame with accent marks removed
    
    Raises:
    ValueError: If the specified column does not exist in the DataFrame
    """
    try:
        # Check if the specified column exists in the DataFrame
        if column_name not in dataframe.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
        
        # Iterate over the values in the specified column
        for i, value in enumerate(dataframe[column_name]):
            # Check if the value contains any accent marks
            if any(char in unicodedata.normalize('NFD', value) for char in ['́', '̀', '̂', '̌', '̋', '̏', '̃', '̄', '̆', '̇']):
                # Remove the accent marks using Unicode normalization
                normalized_value = unicodedata.normalize('NFD', value)
                value_without_accent = ''.join(char for char in normalized_value if unicodedata.category(char) != 'Mn')
                
                # Update the value in the DataFrame
                dataframe.at[i, column_name] = value_without_accent
        
        return dataframe
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return None
    