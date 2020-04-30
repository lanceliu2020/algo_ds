#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = address.replance(".", "[.]")
        return s
        
# @lc code=end

