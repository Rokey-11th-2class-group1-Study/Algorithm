def solution(s):
    answer = 0
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for x in range(len(s)):
        rotated = s[x:] + s[:x]
        stack = []
        
        for char in rotated:
            if char in "([{":
                stack.append(char)
        
            elif char in ")]}":
                if not stack or stack.pop() != pairs[char]:
                    break
                
        else: 
            if not stack:
                answer += 1
            
    return answer

