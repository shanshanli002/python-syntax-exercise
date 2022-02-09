def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    sevens = 0
    for number in nums:
        if int(number) == 7:
            sevens += 1

    if sevens > 0:
        return True
    else: 
        return False 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
