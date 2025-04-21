import pandas as pd

"""
We have identified an issue with the function provided in the codebase. To resolve this,
 you can either debug the function using pytest or add a main function to test its behavior.
Alternatively, adding a main function will enable you to run the function independently and 
observe its output directly.

The minimum requirement for you is to setup a break point and get the value of result in the
line which is failing.
"""

def transform_and_aggregate(data):
    """
    Transforms the input DataFrame by pivoting and aggregating data.
    """
    # Example DataFrame transformation using pivot_table
    try:
        pivoted = data.pivot_table(
            index="Category", columns="Subcategory", values="Value", aggfunc="sum"
        )
    except KeyError as e:
        raise ValueError(f"Missing required column: {e}")

    # Reset index to flatten the DataFrame
    result = pivoted.reset_index()

    result["Total"] = result.sum(axis=1)
    return result




if __name__ == "__main__":
    # Create a sample DataFrame
    data = pd.DataFrame({
        "Category": ["A", "A", "B", "B"],
        "Subcategory": ["X", "Y", "X", "Y"],
        "Value": [10, 20, 30, 40]
    })

    # Run the function and print the result
    result = transform_and_aggregate(data)
    print(result)