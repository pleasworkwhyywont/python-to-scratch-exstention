from creat_scratch_exstention import *
from scratchvmrep import Scratch

scratch_exstention = extension(name="plswork",id="plsssssssssswork",colors={},icons={})

@scratch_exstention.add_block(
    terminal=False,
    text = "hello world",
    args={},
    blocktype=Scratch.BlockType.REPORTER
)
def hello_world():
    return "hello world"
hello_world()

open("plsworl.js","w").write(scratch_exstention.compile())