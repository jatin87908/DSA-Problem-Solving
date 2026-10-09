
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def merge_array(left, right):
            arr = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1

            while i < len(left):
                arr.append(left[i])
                i += 1

            while j < len(right):
                arr.append(right[j])
                j += 1

            return arr

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            list1 = merge_sort(left_arr)
            list2 = merge_sort(right_arr)

            return merge_array(list1, list2)

        return merge_sort(nums)