from json import dumps
class Scratch:
    class ArgumentType:
        class STRING:
            pass
        class NUMBER:
            pass
        class BOOLEAN:
            pass

    class BlockType:
        class COMMAND:
            pass
        class REPORTER:
            pass
        class BOOLEAN:
            pass
        class CONDITIONAL:
            pass
        class EVENT:
            pass

    class vm:
        class runtime:
            def startHats():
                pass
            def getTargetForStage():
                pass
            def getSpriteTargetByName(emptarg : any):
                pass
            def on():
                pass

    class Cast:
        def toNumber(emtyarg : any):
            pass
        def toString(emtyarg : any):
            pass
        def toBoolean(emtyarg : any):
            pass
        def compare(emtyarg1 : any,emtyarg2 : any):
            pass

    class TargetType:
        class SPRITE:
            pass
        class STAGE:
            pass