def sort_arrays(main_array, keys_array):
    indices = list(range(len(keys_array)))

    sorted_indices = sorted(indices, key=lambda x: keys_array.index(main_array[x][0]))

    array1 = [main_array[i][1:-1] for i in sorted_indices]
    array2 = [[main_array[i][-1]] for i in sorted_indices]

    return array1, array2
