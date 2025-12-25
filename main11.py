import random


def sort_rows(matrix):

    for row in matrix:
        row.sort()
    return matrix

def find_min_sum_neighbors(matrix):

    min_sum = float('inf')
    index1, index2 = 0, 0
    
    row_sums = [sum(row) for row in matrix]
    
    for i in range(len(row_sums) - 1):
        current_pair_sum = row_sums[i] + row_sums[i+1]
        if current_pair_sum < min_sum:
            min_sum = current_pair_sum
            index1, index2 = i, i + 1
            
    return index1, index2, min_sum

if __name__ == "__main__":
    
    matrix = [[random.randint(1, 100) for _ in range(2)] for _ in range(15)]
    
    print("Початковий масив:")
    for i, row in enumerate(matrix):
        print(f"Рядок {i}: {row}")
    
    idx1, idx2, total = find_min_sum_neighbors(matrix)
    print(f"\nМінімальна сума у сусідніх рядків {idx1} та {idx2} (Сума: {total})")

    sorted_matrix = sort_rows(matrix)
    print("\nМасив після сортування рядків:")
    for row in sorted_matrix:
        print(row)