import system as sys

class error:

    def __init__(self, line, tokens):
        self.line = line
        self.tokens = tokens
        self.list = []
        self.fofError(True)
        self.fofError(False)
        self.uniunError()


    def convert(self, b, token):
        if b:
            return f"{token}>",len(token),-1,'<'
        else:
            return f"</{token}",len(token)+1,1,'>'
    
    def replace(self,string):
        char1 = '>('
        char2 = ' '
        result = string 
        changes = []
        for c in range(0, len(string)):
            r = len(char1) if c + len(char1) < len(string)-1 else 0
            if string[c:c+r] == char1 and not(sys.test(string, c, '"')) and not(sys.test(string, c, "'")):
                changes.append(c-1)
        for c2 in changes:
            result = result[:c2+1] + char2 + result[c2+3:]
        return result

    def fofError(self, b):
        for token in self.tokens:
            space = self.line.replace(f'</{token}', f'</{token}>')
            space = space.replace(f'{token}>', f'<{token}>')      
        self.line = space.replace('<<', '<').replace('>>', '>').replace('</<', '</')

    def uniunError(self):
        self.line = self.line.replace('>(', ' ')

def garb(line, token):
    l = line
    l = error(l, token).line
    return l