class Solution:
    def countTriplets(self, target, arr):

        arr.sort()

        count = 0

        for i in range(len(arr) - 2):

            j = i + 1
            k = len(arr) - 1

            while j < k:

                curr_sum = arr[i] + arr[j] + arr[k]

                # valid triplets found
                if curr_sum < target:

                    # all elements between j and k work
                    count += (k - j)

                    j += 1

                else:
                    k -= 1

        return count