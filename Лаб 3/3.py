lst = [1, 2, 3, 4, 5]
print("Исходный список:", lst)
print("Обратный список:", lst[::-1]) 
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

numbers = [3, -7, 2, -10, 5]
print("Исходный список:", numbers)
print("Сортировка по убыванию абсолютного значения:", list_sort(numbers))
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

nums = [10, 20, 30, 40]
print("Исходный список:", nums)
print("После замены:", change(nums))