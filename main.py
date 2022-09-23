def two_sum(array, sum_val):
    pairs = []
    array_length = len(array)

    for st_index, st_val in enumerate(array):
        find_val = sum_val - st_val
        if st_index != array_length-1:
            sub_array = array[st_index+1:]

            if find_val in sub_array:
                found_pair = (st_val, find_val)
                pairs.append(found_pair)
    
    if len(pairs) == 0:
        return 0, False
    else:
        return pairs, True




if __name__ == "__main__":
    values, found = two_sum([1,3,5,6,4,23], 20)

    if not found:
        print("No Pairs were found in the array to the sum")
    else:
        print(f"{len(values)} Pair(s) Found:")
        for pair in values:
            print(f'{pair[0]}  :  {pair[1]}')