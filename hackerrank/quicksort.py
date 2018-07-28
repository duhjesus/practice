


def quicksort(nums, left, right):
    if left >=right:
        return
    pivot = nums[left//2 +right//2]#finding the midpt
    print("curr pivot=",pivot)
    index = partition(nums, left,right,pivot)
    quicksort(nums,left,index-1)
    quicksort(nums,index,right)

    return

def partition(nums,left,right,pivot):
    #left side and right side simultaneously
    #moving these pointers towards each other
    #look for the element bigger than the pivot
    while(left <= right):
        while(nums[left]<pivot):
            left = left+1
        print("index left found=", left)
        while(nums[right] >pivot):
            right = right -1
        print("index right found=", right)
        if left <= right:
            #swap values
            print("before=",nums)
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left = left +1
            right = right -1
            print("result=", nums)
    return left        

    
def main():
    nums = [9,2,6,4,3,5,1]
    print(nums)
    quicksort(nums, 0, len(nums)-1)
    print(nums)

    
if __name__ == '__main__':
    main()