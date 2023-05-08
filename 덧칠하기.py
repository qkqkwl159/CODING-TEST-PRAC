
def solution(n, m, section):
    answer = 1
    
    pos = section[0]
    
    for sec in section:
        if sec - pos >= m:
            pos = sec
            answer +=1
        
        
    return answer