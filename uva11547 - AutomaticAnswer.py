def SkillTest(n):
    result = ((((n*63)+7492) * 5) - 498)
    Strres = str(result)
    arr = [(d) for d in str(Strres)]
    print(arr[-2])

T = int(input())
for _ in range(T):
    n = int(input())
    SkillTest(n)
