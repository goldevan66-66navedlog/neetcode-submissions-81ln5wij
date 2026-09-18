class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = set()
        oper.add("+")
        oper.add("-")
        oper.add("*")
        oper.add("/")

        if(len(tokens)<=1):
            return int(tokens[0])

        for i in range(len(tokens)):
            if(tokens[i] not in oper):
                stack.append(tokens[i])
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if(tokens[i] == "+"):
                    stack.append(num1+num2)
                elif(tokens[i] == "-"):
                    stack.append(num1-num2)
                elif(tokens[i] == "*"):
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1/num2))
                    # print(stack)

        return stack[0]