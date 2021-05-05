# Luke Gilin
# 1216992
# 5/5/2021

def selection_sort_descend_trace(numbers):

    for i in range(len(numbers) - 1):
        index_greatest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_greatest]:
                index_greatest = j
        temp = numbers[i]
        numbers[i] = numbers[index_greatest]
        numbers[index_greatest] = temp
        for x in numbers:
            print(x, end=' ')
        print('')

if __name__ == '__main__':

    nanora = input().split()
    selection_sort_descend_trace(nanora)
