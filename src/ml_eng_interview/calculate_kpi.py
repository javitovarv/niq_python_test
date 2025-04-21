"""The candidate receives two lists with the same length, one with the ground truth and the other
with the predictions. The candidate has to implement a function that calculates the accuracy,
precision and recall of the predictions. returning them in a dictionary

Context: 
You can think on a retrieval task where the ground truth is a list of list with the ids of the expected
documents and the predictions is a list of list with the ids of the retrieved documents."""

import pandas as pd
    

def calculate_kpis(groud_truth:list[list[int]], predictions:list[list[int]])->dict[str, float]:
    pass

if __name__ == "__main__":
    # Example usage
    ground_truth = [[1,2,3], [2,3], [3], [4,5], [5,6], [6,7]]
    predictions = [[1,], [3,4], [2,3] , [5], [5,6], [6,7]]
    kpis = calculate_kpis(ground_truth, predictions)
    print(kpis)


