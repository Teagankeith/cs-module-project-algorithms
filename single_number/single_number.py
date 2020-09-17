'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # We have to iterate through the arr to find the number that only occurs once,
    # once we find that number, we just return it

    # We can just the .count() method to check how many times the number we are on
    # occurs in the array we are iterating through
    for num in arr:
        if arr.count(num) == 1:
            correctnum = num
    return correctnum


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")