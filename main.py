
def clclt(first_num: float = 1,sec_num: float = 1, action: str = '+'):
    if action == '+':
        answer = first_num + sec_num
    if action == '-':
        answer = first_num - sec_num
    if action == '*':
        answer= first_num * sec_num
    if action == '/':
        answer=first_num/sec_num

    with open('calc.txt', 'w') as cucumber:
        cucumber.write(f"{first_num} {action} {sec_num} = {answer} \n")


b = clclt(5,4,)
