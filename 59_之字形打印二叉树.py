class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return None

        direction = '>'

        result = [[pRoot]]
        final_result = [[pRoot]]

        while result:
            level_result = []
            level_list = result.pop(0)

            for i in level_list:

                if i.left:
                    level_result.append(i.left)
                if i.right:
                    level_result.append(i.right)
            if direction == '>':
                direction = '<'
                final_result.append(reversed(level_result))
            else:
                direction = '>'
                final_result.append(level_result)
        return final_result