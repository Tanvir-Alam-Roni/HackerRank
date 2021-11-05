def set_ops(s, cmd, n):
    cmd += '(' + ''.join(n) + ')'
    return eval('s.' + cmd)


n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    get_input = input().split()
    cmd = get_input[0]
    args = get_input[1:]
    set_ops(s, cmd, args)

print(sum(s))