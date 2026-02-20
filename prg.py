#
#  class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: Optional[TreeNode]
#         :type q: Optional[TreeNode]
#         :rtype: bool
#         """
#         if (p == q):
#             return True
#         if (p is None or q is None):
#             return False
#         return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 217. Contains Duplicate
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False

# 136. Single Number
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = 0
#         for num in nums:
#             result ^= num
#         return result
        
# nums = [4,1,2,1,2]
# 0000 + 0100
# 0100 + 0001
# 0101 + 0010
# 0111 + 0001
# 0110 + 0010
# 0100

# 342. Power of Four
# class Solution(object):
#     def isPowerOfFour(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n<=0:
#             return False
#         else:
#             for i in range(31):
#                 if 4 ** i == n:
#                     return True
#             else:
#                 return False

# 121. Best Time to Buy and Sell Stock
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         min_price = float('inf')
#         max_profit = 0
        
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             elif price - min_price > max_profit:
#                 max_profit = price - min_price
        
#         return max_profit
# explanation:
# The algorithm initializes two variables: min_price to positive infinity and max_profit to 0. It then iterates through each price in the input list. For each price, it checks if the
# price is less than the current min_price. If it is, it updates min_price to the current price. If the price is not less than min_price, it calculates the potential profit by subtracting min_price from the current price. If this potential profit is greater than the current max_profit, it updates max_profit to this new value. Finally, after iterating through all prices, it returns the max_profit, which represents the maximum profit that can be achieved from a single buy and sell transaction.

# OOPS
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)
animal_sound(cat)