# клавиатурный тренажер в процессе :)
import sys
import termios
import tty

k = 'привет\n'
print(k)
res = ''
while True:
    char = sys.stdin.read(1)
    res += char
    if res == k:
        print('good')

