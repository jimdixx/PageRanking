import numpy as np

def get_custom_props():
    return np.array([
        [0.7, 0.3],
        [0.2, 0.8]
    ])

def get_probabilities(arr):
    row_sums = np.sum(arr, axis=1)
    probabilities = 1 / row_sums.astype(float)
    return arr * probabilities[:, np.newaxis]


def get_vector(arr):
    return np.full((1, arr.shape[0]), float(1/arr.shape[0]))


def calc(arr, size):
    new_matrix = get_probabilities(arr)
    # new_matrix = get_custom_props()
    vector = get_vector(new_matrix)

    vector_previous = vector

    while True:
        vector_new = np.dot(vector_previous, new_matrix)
        if np.allclose(vector_previous, vector_new):
            return vector_new

        vector_previous = vector_new



if __name__ == '__main__':
    init_arr = np.array([
        [0, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 1]
    ])

    sym_mat_size = init_arr.shape[0]
    print(calc(init_arr, sym_mat_size))
