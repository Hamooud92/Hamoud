def spy_game(nums):
    code=[0,0,7,'X']
    for num in nums:
        if num ==  code[0]:
            code.pop(0)
        return len(code)==1
    spy_game([0,0,0,7,8])
    print(spy_game([0,0,0,7,8]))
