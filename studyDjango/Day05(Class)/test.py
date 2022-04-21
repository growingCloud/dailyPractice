# 함수는 사용하려고 있는것!!
# 클래스는 객체를 생성하려고 있는것!!!!!!!!✨✨✨✨✨✨✨✨

class 모험가:
# 생성자 : 객체가 생성될때 변수들을 세팅해줌
def __init__(self, nick, s, sp):
    self.닉네임 = nick
    self.성별 = s
    self.스피드 = sp


# 클래스안에서의 함수 > 메서드
# python 에서 메서드에 무조건 self 라는 인자를
# 가지고 있어야함!!

def 걷는다(self):
    print(self.스피드, "속도로 걷는다.")
    pass

def 뛴다(self):
    pass

def 달팽이세마리(self):
    pass

def 줍는다(self):
    pass

# A 라는 객체 생성
# A 는 객체
# A 는 모험가 class 의 인스턴스

A = 모험가(sp=3000, nick="jeju", s="남")
print(A.닉네임)
A.걷는다()

B = 모험가("BJ kennen", "여", 3500)
B.걷는다()

class 법사(모험가):
    def 매직클로(self):
        pass
    C = 법사("최강법사", "여", 300)

class maple:
    pass

def add(self):
    pass

D = maple()
E = add()