def flatten_list(nested_list):
    flattened = []
    
    for element in nested_list:
        if isinstance(element, list):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)
    
    return flattened

# Test cases
test_case_1 = [[1, 2, 3], [4, 5, 6]]
test_case_2 = [1, [2, 3]]

print(f"Input: {test_case_1} -> Output: {flatten_list(test_case_1)}")
print(f"Input: {test_case_2} -> Output: {flatten_list(test_case_2)}")
