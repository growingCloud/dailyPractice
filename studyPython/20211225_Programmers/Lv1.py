# 문제 1 : 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
# 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

# 입출력 예
#strings	                n	    return
#["sun", "bed", "car"]	    1	    ["car", "bed", "sun"]
#["abce", "abcd", "cdx"]	2	    ["abcd", "abce", "cdx"]

def solution(strings, n):
    answer = []
    cap = []
    stringlen = [len(strings[0]), len(strings[1]), len(strings[2])]

    cap.append(strings[0][n])
    cap.append(strings[1][n])
    cap.append(strings[2][n])
        
    print(cap)
    cap.sort()
    print(cap)



    for i in cap :
        for j in range(min(stringlen)) :
            if i == strings[j][n] :
                answer.append(strings[j])
                print(answer)
                # 동일한 문자가 왔을때 어떻게 오름차순 정렬을 해야 하는지 정리못함
                # 좀 더 고민해 볼 것   

            else :
                continue

    print(answer, "\n")
    
    return answer


solution(["sun", "bed", "car"], 1)
solution(["abce", "abcd", "cdx"], 2)