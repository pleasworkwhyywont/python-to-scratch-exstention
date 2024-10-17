from pscript import py2js
from collections.abc import Callable
from re import sub,split,compile,findall
from json import dumps

#the only reson for this is so that the code can only see bool as javascript code
class false:
    pass

#the only reson for this is so that the code can only see bool as javascript code
class true:
    pass

class extension:
    def __init__(self,name : str , id : str , colors : dict,icons : dict):
        self.color = colors
        self.icons = icons
        self.name = name
        self.id = id
        self.blocks = []
        self.compilejava = ""
        self.funcs = []
        self.menus = {}
        self.vars = []

    def add_block(self,**args):
        def reconizsed_func(func : Callable):
            args["opcode"] = func.__name__
            self.funcs.append(func)
            self.blocks.append(args)
            def wrapper(**kwargs):
                return func(type(**kwargs))
            return wrapper
        return reconizsed_func
    
    def add_menu(self,name,items : list):
        self.menus[name] = items
    def add_variable(self,name):
        self.vars.append(name)

    def creat_exstention(self):
        def formatargs(args : dict):
            unformatedargs = args
            for key,value in unformatedargs.items():
                if isinstance(value,type):
                    unformatedargs[key] = value.__qualname__
                if isinstance(value,dict):
                    unformatedargs[key] = formatargs(value)
            return unformatedargs
        self.compilejava += f"class {self.name}"
        self.compilejava += "{\n"
        for var in self.vars:
            self.compilejava += f"{var};"
        for func in self.funcs:
            unparsedfunc = py2js(func)
            goodfuncs = split("var .*;",unparsedfunc)
            for command in goodfuncs:
                self.compilejava += f"{split(" = ",command)[0]};"
                self.compilejava += command
        self.compilejava += "getInfo() {\n"
        self.compilejava += "return {\n"
        self.compilejava += f"name: '{self.name}',\n"
        self.compilejava += f"id : '{self.id}',\n"

        if "color1" in self.color:
            self.compilejava += f"color1 : '{self.color["color1"]}',\n"
        if "color2" in self.color:
            self.compilejava = f"color2 : '{self.color["color2"]}',\n"
        if "color3" in self.color:
            self.compilejava += f"color3 : '{self.color["color3"]}',\n"

        if "blockIconURI" in self.icons:
            self.compilejava += f"blockIconURI : {self.icons["blockIconURI"]}\n"
        if "menuIconURI" in self.icons:
            self.compilejava += f"blockIconURI : {self.icons["menuIconURI"]}\n"


        self.compilejava += f"blocks : [\n"
        dicttojson = compile("\"([^\"]+)\":")
        for i,block in enumerate(self.blocks):
            unparsedstr = dicttojson.sub(r"\1:", dumps(formatargs(block),indent=4))
            strpatters = findall("Scratch\\..*?\\..*?\"", unparsedstr)
            replacepatterns = findall("\"Scratch\\.?.*?\\.?.*?\"", unparsedstr)
            for index in range(len(replacepatterns)):
                strpattern = strpatters[index]
                unparsedstr = sub(pattern=replacepatterns[index],repl=strpattern[0:len(strpattern)-1],string=unparsedstr)
            parsedstr = unparsedstr
            self.compilejava += parsedstr
            if not i+1 == len(self.blocks):
                self.compilejava += ","
        self.compilejava += "],\n"
        self.compilejava += f"menus : {dicttojson.sub(string=dumps(formatargs(self.menus),indent=4),repl=r"\1:")}\n"
        self.compilejava += "};"
        self.compilejava += "}"
        self.compilejava += "}"
        self.compilejava += f"Scratch.extensions.register(new {self.name}());\n"
        return self.compilejava
