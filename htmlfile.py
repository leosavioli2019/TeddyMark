from html.parser import HTMLParser as HTML
import system as sys

class html(HTML):

    global tags
    global local
    global ram
    tags = ''
    local = []
    ram = 0

    def handle_starttag(self, tag, atr):
        global ram
        global tags
        tags = tag
        ram += len(tags)+1

    def feed(self,line):
        super().feed(line)

    def handle_data(self, data):
        global ram
        if data[0] == '(':
            local.append({
                "tag": tags, 
                "local": ram
            })
        ram += len(data)-1

    def handle_endtag(self, data):
        global ram
        ram += len(data)+2

class convert:

    def __init__(self, line, local):
        self.local = local
        self.line = line
        self.list = []
        self.list_str()
        self.inter()

    def list_str(self):
        for line in self.line:
            self.list.append(line)
        
    def replace(self,string, char1, char2):
        result = string 
        changes = []
        for c in range(0, len(string)):
            if string[c] == char1 and not(sys.test(string, c, '"')) and not(sys.test(string, c, "'")):
                changes.append(c-1)
        for c2 in changes:
            result = result[:c2+1] + char2 + result[c2+2:]
        return result

    def str_list(self):
        self.line = ''
        for i in self.list:
            self.line += i

    def inter(self):
        for c in local:
            self.list[c["local"]] = ' '
            self.list[c["local"]+1] = ''
        self.str_list()
        self.line = self.replace(self.line, ')', '>')
        
def interpret(line):
    global local
    global ram
    print(line)
    a = html()
    a.feed(line)
    b = convert(line, local)
    local = []
    ram = 0
    return b.line