# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         # we want the number of 1s
#         # can do in one four loop, when you hit the goal you reset
#         # the bits are flipping so every 2 numbers you get an extra 1 until you reset
#         result = []
#         cur_ones = 0
#         next_power = 1
#         for i in range (n + 1):
#             result.append(cur_ones)
#             cur_ones += ((i + 1) % 2)
#             if i + 1 == next_power:
#                 next_power *= 2
#                 cur_ones = 1
#         return result


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        offset = 1  # current power of two

        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            result[i] = 1 + result[i - offset]

        return result