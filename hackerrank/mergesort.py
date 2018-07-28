#O(nlogn) time
#O(n) space - downside b/c merging requires more space


# function: helper function 
#           merges left and right half arrays in sorted order
# input:nums= array to be sorted
#       temp= place holder array, hard to do inplace sorting
#       leftStart = start index of the left half array
#       rightEnd =  end index of the right half array
# ouput: none
# effect: sorts portion of nums array
def mergeHalves(nums, temp, leftStart,rightEnd):
    leftEnd = rightEnd//2 +leftStart//2 #middle 
    rightStart = leftEnd +1 # middle +1
    size = rightEnd -leftStart +1

    left = leftStart
    right = rightStart
    index = leftStart

    #comparing elements of the two halves 
    #smaller element of the two taken and copied into temp array
    #then the array's(that the smaller element was in) ptr is incremented
    #compared again until you reach the end of one of the arrays first
    while(left <= leftEnd and right<=rightEnd):
        if nums[left] <=nums[right]:
            temp[index]=nums[left]
            left =left +1
        else:
            temp[index] = nums[right]
            right = right +1
        index = index +1
    # recall python array slices go from left index : to right index (not inclusive on the right end)
    # only one or the other of the halves will have remaining elements so only one of the two following lines
    # will have an effect
    # copying remaining elements of left half and right half
    temp[index:index + leftEnd-left+1]=nums[left:left +leftEnd-left+1]
    temp[index:index + rightEnd-right+1]=nums[right: right +rightEnd-right+1]
    nums[leftStart:leftStart+size]=temp[leftStart:leftStart+size]
    print("after")
    print("nums=", nums)

def mergesort(nums, temp, leftStart, rightEnd):
    if leftStart >= rightEnd:
        return
    middle = leftStart//2 +rightEnd//2 #written like this b/c (leftstart+rightend )/2 <-overflows
    mergesort(nums,temp,leftStart,middle)
    mergesort(nums,temp,middle+1,rightEnd)
    mergeHalves(nums,temp, leftStart,rightEnd)

def main():
    nums = [10,5,2,7,4,9,12,1,8,6,11,3]
    temp = list(0 for i in range(0,len(nums))) #temp array used to stored values in between sorting
    mergesort(nums,temp,0,len(nums)-1)


if __name__ == "__main__":
    main()