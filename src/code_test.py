tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
def evalRPN(tokens) -> int:
    stack = []

    for item in tokens:
        if item in ['+', '-', '*', '/']:
            a = stack.pop()
            b = stack.pop()
            if item == '+' : c = a + b
            elif item == '-': c = b - a
            elif item == '*': c = a * b
            elif item == '/': c = b // a
            stack.append(int(c))
            print(c)
        else:
            stack.append(int(item))
    
    return stack.pop()

print(evalRPN(tokens))

# 这个写法有个出错的地方
# int(a/b) 与(a//b) 有区别吗? 确实有，当结果为正数时确实没啥区别，但为负时，比如：-0.2 前者结果为0
# 而后者结果却为-1， 需要注意呀，不然想死也不知道哪出错了
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []

      for item in tokens:
        if item in ['+', '-', '*', '/']:
          a = stack.pop()
          b = stack.pop()
          if item == '+' : c = a + b
          elif item == '-': c = b - a
          elif item == '*': c = a * b
          elif item == '/': c = b / a    # 若为 b // a 则不通过
          stack.append(int(c))
        else:
          stack.append(int(item))
        
      return stack.pop()