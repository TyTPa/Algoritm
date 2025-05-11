# Виды сортировки
#Пузырьковая
mas = [5, 7, 4, 3, 8, 2]
n = 6
for run in range(n-1):
   for i in range(n-1-run):
       if mas[i] > mas[i + 1]:
           mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)


 #Быстрая сортировка
def quick_sort(s):
   if len(s) <= 1:
       return s

   element = s[0]
   left = list(filter(lambda i: i < element, s))
   center = [i for i in s if i==element]
   right = list(filter(lambda i: i > element, s))

   return quick_sort(left) + center + quick_sort(right)

print(quick_sort([5, 2, 9, 0, 1, 5, 3]))


# Cортировка выбором
# Сортировка выбором работает путем поиска минимального элемента в неотсортированной части
# массива и его обмена с первым элементом этой части.
# Затем процесс повторяется для оставшейся части массива
def selection_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print(numbers)  # [11, 12, 22, 25, 64]

# Сортировка вставками работает путем последовательного перемещения элементов массива,
# вставляя каждый элемент на его правильное место в уже отсортированной части массива.
a = [-3, 5, 0, -8, 1, 10]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insert_sort(a)
print(a)
# Результат: [-8, -3, 0, 1, 5, 10]