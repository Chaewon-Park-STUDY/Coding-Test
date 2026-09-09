

def solution(n):
    num=0
    for i in range(n):
        visited=[i]
        def node():
            nonlocal num
            if len(visited)==n:
                num+=1
                return
            for j in range(n):
                if (
                    j not in visited 
                    and all(
                        abs(j-visited[k])!=len(visited)-k
                        for k in range(len(visited))
                    )
                ):
                    visited.append(j)
                    node()
                    visited.pop()
                else:
                    continue
        node()
    return num
        