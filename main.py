# клавиатурный тренажер в процессе :)
import sys
import termios
import tty

# не работает
def getch():
    """Функция для посимвольного считывания ввода с терминала."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

k = 'привет\n'
print(k)
res = ''
while True:
    char = getch()
    res += char
    if res == k:
        print('good')

