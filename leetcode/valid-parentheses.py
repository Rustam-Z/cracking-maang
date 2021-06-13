class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack:
                    return False
                    
                char = stack.pop()

                for j in range(3):
                    if char == opening[j]:
                        if i != closing[j]:
                            return False

        if stack:
            return False

        return True

