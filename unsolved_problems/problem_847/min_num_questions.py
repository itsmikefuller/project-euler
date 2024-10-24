# Let Q(M) be the minimum number of questions needed to find the magic bean in a selection of M beans
# Split the M beans into a partition P of beans. Then
# Q(M) = [(no. of partitions - 1) + Q(size of largest partition)]

# We can minimise both of these terms of Q(M) by choosing two even partitions of M/2 beans (or (M+1)/2, (M-1)/2 if M is odd)
# Then Q(M) = 1 + Q(M/2) if M is even (or Q(M) = 1 + Q((M+1)/2) if M is odd), as demonstrated below:

# M = 1         => B                        => Q(1) = 0
# M = 2         => B | B                    => Q(2) = 1
# M = 3         => B B | B                  => Q(3) = 1 + Q(2) = 2
# M = 4         => B B | B B                => Q(4) = 1 + Q(2) = 2
# M = 5         => B B B | B B              => Q(5) = 1 + Q(3) = 3
# M = 6         => B B B | B B B            => Q(6) = 1 + Q(3) = 3
# M = 7         => B B B B | B B B          => Q(7) = 1 + Q(4) = 3
# M = 8         => B B B B | B B B B        => Q(8) = 1 + Q(4) = 3
# ...
# M = 2k        => B ... B | B ... B        => Q(2k) = 1 + Q(k)
# M = 2k + 1    => B ... B B | B ... B      => Q(2k+1) = 1 + Q(k+1)
# ...
# M = 2**k      => B ... B | B ... B        => Q(2**k) = 1 + Q(2**{k-1}) = ... = k

# Inductively we discover that Q(M) = k when 2**{k-1} < M <= 2**k => k-1 < log_2(M) <= k
# Hence k = ceil(log_2(M))


from math import log2, ceil


def Q(num_beans: int) -> int:
    return ceil(log2(num_beans)) if num_beans != 0 else 0


def partition(num_beans: int):
    if num_beans % 2 == 0:
        return num_beans/2, num_beans/2
    else:
        return (num_beans + 1)/2, (num_beans - 1)/2


def min_num_questions_given_plates(a: int, b: int, c: int) -> int:
    # Return h(a, b, c)

    plates = [a, b, c]
    plates.sort()
    [smallest_plate, middle_plate, largest_plate] = plates

    return Q(largest_plate) + min(1, Q(middle_plate)) + min(2, Q(smallest_plate))


    # if middle_plate + smallest_plate == 0:
    #     return min_num_questions_given_selection(largest_plate) # Q(largest_plate)
    
    # elif smallest_plate == 0:
    #     partition_1, partition_2 = partition(largest_plate)
    #     plates.remove(smallest_plate)
    #     plates.remove(largest_plate)
    #     plates.append(partition_1, partition_2)
    #     # return NEW h(a', b', c')
    
    # elif smallest_plate == 0:
    #     return 1 + max(min_num_questions_given_selection(largest_plate), min_num_questions_given_selection(middle_plate))
    
    # else:
    #     return 1 + max(min_num_questions_given_selection(largest_plate), 1 + min_num_questions_given_selection(middle_plate))
