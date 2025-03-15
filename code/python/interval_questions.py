"""Interval Questions."""
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def get_intersection(intervals_lst):

    # Given a list of ranges, get the intersection of all.
    min_range = max(sublist[0] for sublist in intervals_lst)
    max_range = min(sublist[1] for sublist in intervals_lst)

    interval_range = (min_range, max_range)
    return interval_range


def aggregate_intervals(all_labelers):
    """
    Waymo Coding question:
    Suppose we are training an action localization model to localize the video time ranges 
    that include a person directing the traffic.

    We have N labelers to label these time ranges for each video, each labeler will 
    provide a list of time ranges that include a person directing the traffic as below:

    [(start_0, end_0), (start_1, end_1), (start_k, end_k)]

    Design and implement an algorithm that aggregates all the time ranges of a video 
    from N labelers and return a list of final time ranges for this video.used.
    
    For example, the following

    input represents the labeled time ranges from 3 labelers:
        [

        [(start 0, end 0), (start 1, end 1), (start 2, end 2)],

        [(start_0, end 0), (start_1, end_1), (start_2, end_2), (start_3, end_3)],

        [(start 0, end 0), (start 1, end 1)],

    [Output] A list of aggregated time ranges:

        [(start_0, end_0), (start_1, end_1), (start_2, end_2)]

    Example:

    Input:
    [

    [[0, 4], [25, 30]],

    [[1, 5], [25, 35]],

    [[0, 7]],

    ]

    Output:
    [(1, 4), (25, 30)]
    """
    
    # Flatten the list
    flattened_list = [label for sublist1 in all_labelers for label in sublist1]
    data_array = np.array(flattened_list)

    silhouette_scores = {}
    # Use silhouette_score to pick the best K
    for k in range(2, min(len(data_array), 6)):
        kmeans = KMeans(n_clusters=k)
        clusters = kmeans.fit_predict(data_array)
        score = silhouette_score(data_array, clusters)
        silhouette_scores[k] = score

    best_k = max(silhouette_scores, key=silhouette_scores.get)

    kmeans = KMeans(n_clusters=best_k)
    final_clusters = kmeans.fit_predict(data_array)

    clustered_data = {i: [] for i in range(best_k)}
    for point, label in zip(flattened_list, final_clusters):
        clustered_data[label].append(point)

    valid_intervals = []
    for _, point in clustered_data.items():
        group_interval = get_intersection(point)
        valid_intervals.append(group_interval)

    return valid_intervals