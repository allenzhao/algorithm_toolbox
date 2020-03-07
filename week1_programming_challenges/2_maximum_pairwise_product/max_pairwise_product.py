# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_index_1 = -1
    max_index_2 = -1
    for i in range(0,n):
        if (max_index_1 == -1) or (numbers[i] > numbers[max_index_1]):
            max_index_1 = i
    for j in range(0,n):
        if (j !=max_index_1) and ((max_index_2 == -1) or (numbers[j] > numbers[max_index_2])):
            max_index_2 = j
    max_product = numbers[max_index_1] * numbers[max_index_2]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
