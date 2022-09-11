import math


# KNN - KNearest Neighbor

# This is not the full implementation, but the functions you'd need to use

def euclidean_distance(vector1, vector2):

    distance = 0.0
    for i in range(0, len(vector1)-1):
        distance += (vector1[i] - vector2[i])**2
    return math.sqrt(distance)

# Get nearest neighbors
def get_neighbors(train, test_vec, kneighbors):
    distances = ()

    for train_vec in train:
        dist = euclidean_distance(train_vec, test_vec)
        distances.append((train_vec, dist))

    distances.sort(key=lambda x: x[1])
    neighbors = ()
    for i in range(kneighbors):
        neighbors.append(distances[i][0])

    return neighbors

# Make predictions
def predict_classification(train, test_vec, kneighbors):
    neighbors = get_neighbors(train, test_vec, kneighbors)
    output_values = [vec[-1] for vec in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction