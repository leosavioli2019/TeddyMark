import text
import ex
import os
import conf
import system as sys

path = os.path.dirname(os.path.realpath(__file__))

def compile(file):
	f = open(file, 'r', encoding="utf-8")
	print(ex.ex(f.read()))

def replace(string, char1, char2):
    result = string 
    changes = []
    for c in range(0, len(string)):
        if string[c] == char1 and not(sys.test(string, c, '"')) and not(sys.test(string, c, "'")):
            changes.append(c-1)
    for c2 in changes:
        result = result[:c2+1] + char2 + result[c2+2:]
    return result

def parameters_error(n, func, line):
    end = []
    paramter = str(line).strip()
    paramter = str(paramter).split(' ')
    paramter = paramter[1:]
    for c in range(0, len(paramter)):
        if not(paramter[c][-1] == "'" or paramter[c][-1] == '"') and paramter[c][-1] != ')':
            pass
        else:
            end.append(paramter[c])
    paramter = end
    if n[1] != "*":
        if not(len(paramter) > n[0]-1 and len(paramter) < n[1]+1):
            if n[0] == n[1]:
                return(f'Parameter error: {func} take {n[0]} parameters but {len(paramter)} was given')
            else:
                return(f'Parameter error: {func} take {n[0]} to {n[1]} parameters but {len(paramter)} was given')
    else:
        if not(len(paramter) > n[0]-1):
            if n[0] == n[1]:
                return(f'Parameter error: {func} take {n[0]} parameters but {len(paramter)} was given')
            else:
                return(f'Parameter error: {func} take {n[0]} to {n[1]} parameters but {len(paramter)} was given')

def execute(line, func, fro):
    new = str(line).strip()
    new = replace(new, ' ', ',')
    new = new[str(new).find(','):]
    new = new.replace(',', '(', 1)
    new += ')'
    if fro != '':
        exec(f'{fro}.{func}{new}')
    else:
        exec(f'{func}{new}')    

def do(func, line):
    a = parameters_error([1,1], f'{str(func).capitalize()}', line)
    if a is None:
        execute(line, func, '')
    else:
        print(a)

def imperative():
	text.imperative()
	a = ''
	while a.strip() != 'exit':
		a = input('>>>')
		if a.strip() == 'exit':
			break
		print(ex.ex(a))
	os.system(conf.systemClear())
	text.copright()

def main():
	text.copright()
	a = ''
	while a != 'exit':
		a = input('>>>')
		if a.strip() == 'imperative':
			os.system(conf.systemClear())
			imperative()
			continue	
		if a.strip() == 'exit':
                	break
		compile(a)
######
main()
