class plswork{
;
hello_world;
hello_world = function flx_hello_world () {
    return "hello world";
};
getInfo() {
return {
name: 'plswork',
id : 'plsssssssssswork',
blocks : [
{
text : 'hello world',
opcode : 'hello_world',
blockType :  Scratch.BlockType.REPORTER,
arguments : {},
terminal : false
}
],
menu : []
};}}Scratch.extensions.register(new plswork());
