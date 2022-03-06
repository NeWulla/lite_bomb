
def bomb(count):
    if count <= 0:
        return bomb(count + 1)
    else:
        msg = input('Message\n>')
        for i in range(count):
            print(msg, end=' ')
            
def trying():
    try:
        bomb(int(input('Count of bombing\n>')))
    except ValueError:
        trying()
trying()

