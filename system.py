#test if is in quostion marks 
class exe:

    def __init__(self, line, n, character):
        self.line = line
        self.n = n
        self.result = False
        self.char = character
        self.interpret()

    def between(self, a, b):
        if self.n in [x for x in range(a, b)]:
            return True
        else:
            return False

    def interpret(self):
        local = []
        first = 0 
        for c in range(0, len(self.line)):
            if self.line[c] == self.char:
                if first == 0:        
                    local.append([c])
                    first = 1
                else:
                    local[-1].append(c)
                    first = 0
        for c in range(0, len(local)):
            if self.result == True:
                break
            else:
                self.result = self.between(local[c][0],local[c][1])

def test(line, n, character):
    return exe(line, n, character).result