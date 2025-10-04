def find_leaders(arr):
    leaders = []
    max_from_right = float('-inf')
 
    for num in reversed(arr):
        if num > max_from_right:
            leaders.append(num)
            max_from_right = num
  
    leaders.reverse()
    return leaders

arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))  # Output: [17, 5, 2]
