#O(log(n)) = n -> n/2 n/2 -> n/4 n/4 n/4 n/4 ->...-> 1
def binarySearch(nums,left,right,value):
    if left >right:
        return -1
    else:
        mid= left +(right-left)//2
        if nums[mid] ==value:
            return mid
        elif nums[mid]>value:
            return binarySearch(nums,left,mid-1,value)
        else:
            return binarySearch(nums,mid+1,right,value)      

def main():
    nums = [1,2,3,4,5,6,8,10,15,35,36,37,38,40,41]
    indeces = list( range(0,len(nums)))
    value= 39
    result = binarySearch(nums,0,len(nums)-1,value)
    if result == -1:
        print(value,"not in array")
    else:
        print(value,"found at index=",result)
    print(nums)
    print(indeces)
    
if __name__ == '__main__':
    main()