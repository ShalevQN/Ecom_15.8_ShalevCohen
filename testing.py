def two_list_sort(lst_x: list[int], lst_y: list[int]):
    return_list = lst_x.copy()  # Create a copy to avoid modifying the original list

    # Insert elements from lst_y into return_list
    for num in lst_y:
        if num in return_list:  # Avoid duplicates
            continue

        # Find the correct place to insert num by checking each element in return_list
        for i in range(len(return_list)):
            if return_list[i] > num:
                return_list.insert(i, num)
                break
        else:
            # If no insert was made (num is larger than all elements), append at the end
            return_list.append(num)

    return return_list


# Test with your example:
print(two_list_sort([2, 2, 4], [1, 3, 4, 5]))
