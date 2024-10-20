from creat_scratch_exstention import extension
from scratchvmrep import Scratch
complex_exstnetion = extension(colors={},icons={},name="MATH",id="MATHOPORATORS")
complex_exstnetion.add_menu("oporators",["+","-","*"])

@complex_exstnetion.add_function
def add_complex_number(complex1:list,complex2:list):
    real = complex1[0] + complex2[0]
    imag =  complex1[1] + complex2[1]
    return f"{real}+i{imag}"

@complex_exstnetion.add_function
def sub_complex_number(complex1:list,complex2:list):
    real = complex1[0] + complex2[0]
    imag =  complex1[1] + complex2[1]
    return f"{real}+i{imag}"

@complex_exstnetion.add_function
def mul_complex_number(complex1:list,complex2:list):
    real = complex1[0] * complex2[0] - complex1[1] * complex2[1]
    imag = complex1[0] * complex2[0] + complex1[1] * complex2[1]
    return f"{real}+i{imag}"

@complex_exstnetion.add_function
def congruent(complexnum:list):
    real_congruent = complexnum[0]
    imag_congruent = complexnum[1]
    return f"{real_congruent}+i{imag_congruent}"

@complex_exstnetion.add_function
def div_complex_number(complex1:list,complex2:list):
    real = complex1[0] * complex2[0] - complex1[1] * complex2[1]
    imag = complex1[0] * complex2[0] + complex1[1] * complex2[1]
    return f"{real}+i{imag}"


@complex_exstnetion.add_block(text="[complexnumber1] + [complexnumber2]",
                              args={"complexnumber1" : {"type" : Scratch.ArgumentType.STRING,"defuealValue" : "0+i0"},
                                    "oporations" : {"menu" : "oporators","type" : Scratch.ArgumentType.STRING},
                                    "complexnumber2" : {"type" : Scratch.ArgumentType.STRING,"defuealValue" : "0+i0"}},
                              BlockType = Scratch.BlockType.REPORTER)
def opporation_complex_number(args):
    complex_number_1 = args.complexnumber1.split("+i")
    complex_number_2 = args.complexnumber2.split("+i")
    if args.oporations == "+":
        result = add_complex_number(complex_number_1,complex_number_2)
    elif args.oporations == "-":
        result = sub_complex_number(complex_number_1,complex_number_2)
    elif args.oporations == "*":
        result = mul_complex_number(complex_number_1,complex_number_2)
    return result

print(complex_exstnetion.creat_exstention())
