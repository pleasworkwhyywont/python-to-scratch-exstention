from pscript import py2js
from enum import Enum
from re import sub 
from json import dumps

class blocktypes(Enum):
    COMMAND = "Scratch.BlockType.COMMAND"
    REPORTER = "Scratch.BlockType.REPORTER"
    BOOLEAN = "Scratch.BlockType.BOOLEAN"

class argtypes(Enum):
    STRING = "Scratch.ArgumentType.STRING"
    NUMBER = "Scratch.ArgumentType.NUMBER"
    BOOLEAN = "Scratch.ArgumentType.BOOLEAN"
    COLOR = "Scratch.ArgumentType.COLOR"
    ANGLE = "Scratch.ArgumentType.ANGLE"
    MATRIX = "Scratch.ArgumentType.MATRIX"
    NOTE = "Scratch.ArgumentType.NOTE"
    IMAGE = "Scratch.ArgumentType.IMAGE"
    COSTUME = "Scratch.ArgumentType.COSTUME"
    SOUND = "Scratch.ArgumentType.SOUND"

class block:
    def __init__(self,func,text,args,blocktype,terminal : bool, funcname : str):
        self.func = func
        self.text = text
        self.args = args
        self.blocktype = blocktype
        self.terminal = terminal
        self.funcname = funcname

    def __getitem__(self,itemrequest):
        return exec(f"self.{itemrequest}")

class exstention:
    def __init__(self,name : str , id : str , colors : dict,icons : dict):
        self.color = colors
        self.icons = icons
        self.name = name
        self.id = id
        self.blocks = []
        self.compilejava = ""

        
    def add_block(self,text,args,blocktype,terminal):
        def reconizsed_func(func):
            def wrapper(*pars,**kwargs):
                self.blocks.append(
                    block(
                    func,
                    text,
                    args,
                    blocktype,
                    terminal,
                    func.__name__
                ))
                return
            return wrapper
        return reconizsed_func
    
#like the name says it auto compile to java script
    def compile(self):
        self.compilejava += f"class {self.name} \n"
        self.compilejava += " {\n"
        for block in self.blocks:
            self.compilejava += py2js(block.func)
        self.compilejava += "getinfo() {\n"
        self.compilejava += "return {\n"
        self.compilejava += f"name : '{self.name}',\n"
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
        for i,block in enumerate(self.blocks):
            self.compilejava += "{\n"
            self.compilejava += f"text : '{block.text}',\n"
            self.compilejava += f"opcode : '{block.funcname}',\n"
            self.compilejava += f"blockType : '{block.blocktype.value}',\n"
            # João Pedro on stackoverflow whoever you are thank you
            self.compilejava += f"arguments : {sub("\"([^\"]+)\":", r"\1:", dumps(block.args))}\n"
            self.compilejava += f"terminal : '{block.terminal}',\n"
            self.compilejava += "}\n"
            if not i == len(self.blocks) - 1:
                self.compilejava += ","
        self.compilejava += "],\n"
        self.compilejava += f"menu : []\n"
        self.compilejava += "};\n}\n"

        self.compilejava += f"Scratch.extensions.register(new {self.name}());\n"
        return self.compilejava