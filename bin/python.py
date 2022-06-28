# # from subprocess import list2cmdline


# # list = []
# # for N in range(1, 100):


# #     ans = (pow(N, 2) + 1)
# #     # result = (ans*2) + 1
# #     list.append(ans)
# # print(list)






# arr  = [3,4,1,2]

# for i in range(len(arr)):
#     for j in range(0, len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j], arr[j+1]= arr[j+1], arr[j]
#             # print(arr)
# # print(arr)
# for i in range(len(arr)):
#     if arr[i]<arr[len(arr)-1]:
#         arr[i], arr[len(arr)-1]= arr[len(arr)-1], arr[len(arr)-2]
# print(arr)























# import java.io.*; // for handling input/output
# import java.util.*; // contains Collections framework

# // don't change the name of this class
# // you can add inner classes if needed
# class Main {

# 	public double findMedianSortedArrays(int input1[], int input2[]) {
#         //if input1 length is greater than switch them so that input1 is smaller than input2.
#         if (input1.length > input2.length) {
#             return findMedianSortedArrays(input2, input1);
#         }
#         int x = input1.length;
#         int y = input2.length;

#         int low = 0;
#         int high = x;
#         while (low <= high) {
#             int partitionX = (low + high)/2;
#             int partitionY = (x + y + 1)/2 - partitionX;

#             //if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
#             //if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
#             int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : input1[partitionX - 1];
#             int minRightX = (partitionX == x) ? Integer.MAX_VALUE : input1[partitionX];

#             int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : input2[partitionY - 1];
#             int minRightY = (partitionY == y) ? Integer.MAX_VALUE : input2[partitionY];

#             if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
#                 //We have partitioned array at correct place
#                 // Now get max of left elements and min of right elements to get the median in case of even length combined array size
#                 // or get max of left for odd length combined array size.
#                 if ((x + y) % 2 == 0) {
#                     return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY))/2.0;
#                 } else {
#                     return (Math.max(maxLeftX, maxLeftY);
#                 }
#             } else if (maxLeftX > minRightY) { //we are too far on right side for partitionX. Go on left side.
#                 high = partitionX - 1;
#             } else { //we are too far on left side for partitionX. Go on right side.
#                 low = partitionX + 1;
#             }
#         }

#         //Only we we can come here is if input arrays were not sorted. Throw in that scenario.
#         throw new IllegalArgumentException();
#     }


#     public static void main(String[] args) {

#         Scanner s = new Scanner(System.in);

#         String n1 = s.nextLine();
#         String[] str = n1.split(" ");
#         int var1 = Integer.parseInt(str[0]);

#         int[] input1 = new int[var1];
# 		// System.out.println(input1[1]);
#         for (int i = 0; i < var1; i++) {
#             input1[i] = s.nextInt();

#         }

#         int var2 = Integer.parseInt(str[1]);
#         int[] input2 = new int[var2];

#         for (int i = 0; i < var2; i++) {

#             input2[i] = s.nextInt();
#         }
#         Main obj = new Main();
#         double and = obj.findMedianSortedArrays(input1, input2);
#         System.out.println(and);
        
        



#     }
# }










from tabnanny import check




class Solution:
    def check(nums):
        n = len(nums)
        r = sorted(nums)
        print(reverse(r))

        for start in range(n):
            if nums[start:] + nums[:start] == r:
                return True
        return False

    nums = [1, 3, 2]
    print(check(nums))
