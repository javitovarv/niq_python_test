import pandas as pd

from ml_eng_interview.fix_error_exercise import transform_and_aggregate

def test_transform_and_aggregate():
    # Create a sample DataFrame
    data = pd.DataFrame({
        "Category": ["A", "A", "B", "B"],
        "Subcategory": ["X", "Y", "X", "Y"],
        "Value": [10, 20, 30, 40]
    })

    # Expected output after transformation
    expected = pd.DataFrame({
        "Category": ["A", "B"],
        "X": [10, 30],
        "Y": [20, 40],
        "Total": [30, 70]  # This will fail due to the error in the script
    })

    # Run the function and compare results
    result = transform_and_aggregate(data)
    assert (result==expected).all().all()