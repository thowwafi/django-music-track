def merge_intervals(intervals, threshold):
    if not intervals:
        return []

    # Sort the intervals
    intervals.sort(key=lambda x: x[0])
    merged_list = [intervals[0]]  #get the first interval

    for current in intervals[1:]:
        last = merged_list[-1]

        # Check if the current interval minus last interval 
        # is less than the threshold
        if current[0] - last[1] < threshold:
            # if it is less than the threshold, merge intervals
            last[1] = max(last[1], current[1])
        else:
            # else add to the merged_list
            merged_list.append(current)

    return merged_list


# Examples
print(merge_intervals([[0, 300], [600, 1200], [3500, 6000]], threshold=400))
# Output: [[0, 1200], [3500, 6000]]
