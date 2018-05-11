#!/bin/python3

import os
import sys
import math

#
# Complete the summingPieces function below.
#
def summingPieces(arr):
    total_values = 0
    for segment_size in range(1, len(arr)):
        if segment_size == 1:
            total_values += sum(arr)
        elif len(arr) // segment_size == len(arr) / segment_size:
            tmp = []
            prev_index = 0
            for index in range(segment_size, len(arr)+1, segment_size):
                tmp.append(arr[prev_index:index])
                prev_index = index
            total_values += sum([sum(elem)*len(elem) for elem in tmp])
        else:
            tmp = []
            prev_index = 0
            for index in range(segment_size, len(arr), segment_size):
                tmp.append(arr[prev_index:index])
                prev_index = index
            tmp.append([arr[-1]])
            total_values += sum([sum(elem)*len(elem) for elem in tmp])
            tmp = []
            prev_index = 1
            for index in range(segment_size+1, len(arr)+1, segment_size):
                tmp.append(arr[prev_index:index])
                prev_index = index
            tmp.append([arr[0]])
            total_values += sum([sum(elem)*len(elem) for elem in tmp])
            # handle the case of uneven splits
    total_values += sum(arr) * len(arr)
    return int(total_values % (math.pow(10, 9) + 7))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
