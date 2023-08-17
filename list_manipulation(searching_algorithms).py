def linearSearch(lst,target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binarySearch(lst,target):
    left,right = 0, len(lst)-1
    while left <= right:
        mid= left+((right-left)//2)
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

def ternarySearch(lst,target):
    left,right =0, len(lst)-1
    while left <= right:
        mid1= left+((right-left)//3)
        mid2= right-((right-left)//3)
        if lst[mid1] == target:
            return mid1
        elif lst[mid2] == target:
            return mid2
        elif lst[mid1] > target:
            right = mid1-1
        elif lst[mid2] < target:
            left = mid2 +1
        else:
            left = mid1+1
            right = mid2-1
    return -1
def main():
    s=input("enter comma seperated values you want in the list: ")
    y=s.split(',')
    lst=[int(x) for x in y]
    lst.sort()
    print("The ordered list is: ",lst)
    target=int(input("Enter the number you want to search: "))
    print("Enter which search algorithm you want to perform?")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Ternary Search")
    choice=int(input("Enter your choice (1 or 2 or 3): "))
    match choice:
        case 1:
            index = linearSearch(lst,target)
        case 2:
            index = binarySearch(lst,target)
        case 3:
            index = ternarySearch(lst,target)
        case _:
            print("Invalid choice. Exiting program.")
    print()
    if index != -1:
        print(f"Target value {target} found at index {index} of ordered list.")
    else:
        print("Target value not found.")
if __name__ == "__main__":
    main()
