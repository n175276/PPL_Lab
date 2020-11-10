# Program to find missing pages in a given page number list

list1 = [2, 4, 5, 6, 12, 16, 17, 20, 21]
print("Page number list is :", list1)
print("Missing pages are : ")
for i in range(1, 26):
    if i not in list1:
        print(i, end=' ')









