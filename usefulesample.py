#its not finish i relized that i need to implement another feacher :("think of this as crying emoji"
from creat_scratch_exstention import extension
from scratchvmrep import Scratch

enum_exstention = extension(name="enums",id="enumsss",colors={},icons={})

enum_exstention.add_variable("enums")
enum_exstention.add_variable("currentenumname")
enum_exstention.add_variable("currentenumcases")

@enum_exstention.add_block(text="creat enum[enumname]",
                           args={"enumname" : {"type" : Scratch.ArgumentType.STRING,
                                 "defaultValue" : "enum name"}},
                            blockType = Scratch.BlockType.CONDITIONAL,
                            branchCount = 1)
def creat_enum(args,util):
    enums[args.enumname] = []
    currentenumcases = []
    util.startBranch(1)
    enums[args.enumname] = currentenumcases
    currentenumcases = []


@enum_exstention.add_block(text = "add case[case]",
                           args={"case" : {
                               "type" : Scratch.ArgumentType.STRING,
                               "defaultValue" : "case name"}},
                            blockType = Scratch.BlockType.COMMAND)
def addcase(args):
    currentenumcases.append(args.case)

@enum_exstention.add_block(text = "switch enum instance[enuminstance]",
                           args={"enuminstance" : {
                               "type" : Scratch.ArgumentType.STRING,
                               "defaultValue" : "enum instance name"}},
                            blockType = Scratch.BlockType.CONDITIONAL,
                            branchCount = 1)
def switch_enum(args,util):
    currentenumname = args.enuminstance
    util.startBranch(1)
    currentenumcases = currentenumcases.keys()
