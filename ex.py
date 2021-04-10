TOKENS = {
    
    ##############
    "######": "h6",
    "#####": "h5",
    "####": "h4",
    "###": "h3",
    "##": "h2",
    "#": "h1",
        
    ############
    "$$$": "div",
    "||": "br",
    "!":  "a",
    "@": "img",
    
    #############
    "```": "code",
    "**": "strong",
    "_": "i", 
    "°": "mark",
    
    ##############
    "%%": "ol",
    "-": "li",
    "%": "ul",

    ##############
    '¨': "blockquote",
    "£": "cite",

    ##############     
    "{[]}": "form",
    "???": "input",

    ###############
    '|{+}|': "nav",
    "^{}^": 'p style="text-align: center;"',

    ###############
    "<html>": 'html',
    "{{": "script",
    "}}": "/script",
    "<<": "style",
    ">>": "/style",
    "//": "link",
    
    ###############
    '<::>': 'audio',
    '&&': 'video'
}


execptions = [
    "@", 
    "--"
    "???",
    "<<",
    ">>",
    "//"
]

t = []

for k,v in TOKENS.items():
    t.append(v)

class inter:

    def __init__(self, line):
        self.line = line
        self.alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'ñ', 'ó', 'ô', 'õ', 'â', 'ã', 'á', 'à', 'ú', 'í', 'ì', 'ù', 'é', 'è', 'ç']
        self.interprer()

    def interprer(self):
        self.tokens = []
        for k,v in TOKENS.items():
            self.tokens.append(k)
        self.ex()

    def openEnd(self, t, op):
        if op:
            return f"<{t}>"
        else:
            return f"</{t}>"

    def replace(self, line, t, op):
        l = line
        l1 = l[:l.find(t)+len(t)]
        l = l1.replace(t, self.openEnd(TOKENS[t], op))
        after = line[len(l1):]
        if t in after: 
            after = self.replace(after, t, not(op)) if not(t in execptions) else self.replace(after, t, op) 
        return l+after

    def paramter(self):
        pass

    def ex(self):
        for token in self.tokens:
            if token in self.line:
                self.line = self.replace(self.line, token, True)

def ex(line):
    a = inter(line).line
    a = a.replace('>(', ' ')
    a = a.replace(')', '>')
    return a