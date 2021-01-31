import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def insertion_sort(insertion_list):
    for j_index, j in enumerate(insertion_list[1:], start=1):
        key = j
        i_index = j_index - 1
        while i_index >= 0 and insertion_list[i_index] > key:
            insertion_list[i_index + 1] = insertion_list[i_index]
            i_index = i_index - 1
        insertion_list[i_index + 1] = key
    return insertion_list


def merge(a, b):
    i = 0
    j = 0
    k = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            k.append(a[i])
            i += 1
        else:
            k.append(b[j])
            j += 1
    k.extend(a[i:])
    k.extend(b[j:])
    return k


def merge_sort(merge_list):
    if len(merge_list) == 1 or len(merge_list) == 0:
        return merge_list[:len(merge_list)]
    q = int(len(merge_list) / 2)
    left_branch = merge_list[0:q]
    right_branch = merge_list[q:len(merge_list)]
    new_left = merge_sort(left_branch)
    new_right = merge_sort(right_branch)
    both_branches_merged = merge(new_left, new_right)
    return both_branches_merged


i = 10
limit = 0

insertion_random_time = []
insertion_random_n = []
insertion_descending_time = []
insertion_descending_n = []
insertion_ascending_time = []
insertion_ascending_n = []

merge_random_time = []
merge_random_n = []
merge_descending_time = []
merge_descending_n = []
merge_ascending_time = []
merge_ascending_n = []

while i <= 1000000:
    number_file = open("{}_numbers.txt".format(i), 'w')
    for j in range(i):
        number_file.write(str(random.randrange(-2147483648, 2147483647)) + "\n")
    number_file.close()
    a_list = np.loadtxt('{}_numbers.txt'.format(i), int)
    new_list = []
    for n in a_list:
        new_list.append(n)

    if limit <= 3:
        # random
        start_insertion_timer = timer()
        insertion_sort(new_list)
        np.savetxt("{}_numbers_sorted".format(i), new_list)
        end_insertion_timer = timer()
        insertion_random_time.append(end_insertion_timer - start_insertion_timer)
        insertion_random_n.append(i)

        # descending
        start_insertion_timer = timer()
        insertion_sort(new_list)
        np.savetxt("{}_numbers_sorted".format(i), new_list)
        end_insertion_timer = timer()
        insertion_descending_time.append(end_insertion_timer - start_insertion_timer)
        insertion_descending_n.append(i)

        # ascending
        start_insertion_timer = timer()
        new_list.reverse()
        insertion_sort(new_list)
        np.savetxt("{}_numbers_sorted".format(i), new_list)
        end_insertion_timer = timer()
        insertion_ascending_time.append(end_insertion_timer - start_insertion_timer)
        insertion_ascending_n.append(i)

        # print(str(end_insertion_timer - start_insertion_timer) + " insertion ascending {}".format(i))

        limit += 1

    # random
    start_merge_timer = timer()
    merge_sort(a_list)
    np.savetxt("{}_numbers_sorted".format(i), a_list)
    end_merge_timer = timer()
    # print(str(end_merge_timer - start_merge_timer) + " merge {}".format(i))
    merge_random_time.append(end_merge_timer - start_merge_timer)
    merge_random_n.append(i)

    # descending
    start_insertion_timer = timer()
    merge_sort(new_list)
    np.savetxt("{}_numbers_sorted".format(i), new_list)
    end_insertion_timer = timer()
    # print(str(end_insertion_timer - start_insertion_timer) + " merge descending {}".format(i))
    merge_descending_time.append(end_merge_timer - start_merge_timer)
    merge_descending_n.append(i)

    # ascending
    start_merge_timer = timer()
    new_list.reverse()
    merge_sort(new_list)
    np.savetxt("{}_numbers_sorted".format(i), new_list)
    end_merge_timer = timer()
    # print(str(end_insertion_timer - start_insertion_timer) + " merge ascending {}\n".format(i))
    merge_ascending_time.append(end_merge_timer - start_merge_timer)
    merge_ascending_n.append(i)

    i *= 10

plt.plot(insertion_random_n, insertion_random_time)
plt.title('Insertion Sort (Random)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
# plt.yscale('log')
plt.xscale('log')
plt.show()

plt.plot(insertion_descending_n, insertion_descending_time)
plt.title('Insertion Sort (Descending)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
# plt.yscale('log')
plt.xscale('log')
plt.show()

plt.plot(insertion_descending_n, insertion_ascending_time)
plt.title('Insertion Sort (Ascending)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
# plt.yscale('log')
plt.xscale('log')
plt.show()

plt.plot(merge_random_n, merge_random_time)
plt.title('Merge Sort (Random)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
# plt.yscale('log')
plt.xscale('log')
plt.show()

plt.plot(merge_descending_n, merge_descending_time)
plt.title('Merge Sort (Descending)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
# plt.yscale('log')
plt.xscale('log')
plt.show()

plt.plot(merge_ascending_n, merge_ascending_time)
plt.title('Merge Sort (Ascending)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
# plt.yscale('log')
plt.xscale('log')
plt.show()
