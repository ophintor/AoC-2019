import sys
import re
import math

# def calculate_lcm(a,b):
#     return (a * b) // math.gcd(a, b)

# def multiply_formula(formula, mult):
#     f = [x.strip() for x in formula.split()]
#     for i, comp in enumerate(f):
#         if comp.isdigit():
#             f[i] = str(mult * int(comp))
#     formula = ' '.join(f)
#     return formula

def get_current_formula_values(formula):
    formula_solution = formula.split('=>')[1].strip()
    formula_solution_mult = int(formula_solution.split(' ')[0])
    formula_solution_chem = formula_solution.split(' ')[1]
    formula_components = [x.strip() for x in formula.split('=>')[0].split(',')]
    return formula_solution_mult, formula_solution_chem, formula_components

def display_everything(depth, formula, quantities, remains, mult):
    print (str(formula) + (70-(len(formula)))*' ' + str(quantities) + (80-(len(str(quantities))))*' ' + str(remains) + (40-(len(str(remains))))*' ' + str(mult) + 'x')

def find_next_formula(lines, formula_solution_chem):
    for formula in lines:
        next_formula_solution_mult, next_formula_solution_chem, next_formula_components = get_current_formula_values(formula)
        if  formula_solution_chem == next_formula_solution_chem:
            return formula, next_formula_solution_mult, next_formula_solution_chem, next_formula_components
    return '',1,'',{}

def get_component_values(component):
    return int(component.strip().split(' ')[0]), component.strip().split(' ')[1]

def store_quantities(quantities, formula_component_mult, formula_component_chem, mult):
    if not formula_component_chem in quantities:
        quantities[formula_component_chem] = int(formula_component_mult * mult)
    else:
        quantities[formula_component_chem] += int(formula_component_mult * mult)

def apply_discount_if_available(remains, mult, chem, formula):

    if chem in remains:
        print(" ****************************** HERE I AM")
        mult_orig = mult
        print(mult_orig,mult)
        print(remains)
        if remains[chem] >= mult:
            remains[chem] -= mult
            mult = 0
        else:
            mult -= remains[chem]
            remains[chem] = 0

        print(remains[chem],mult)
        print(formula)
        formula = formula.replace(str(mult_orig) + ' ' + chem, str(mult) + ' ' + chem)
        print(formula)
        print(remains)

    return formula, mult

def calculate_multiplier(next_formula_solution_mult,formula_component_mult,chem,remains):
    print (float(formula_component_mult),float(next_formula_solution_mult))
    mult = math.ceil(float(formula_component_mult) / float(next_formula_solution_mult))
    store_remains(remains,chem,next_formula_solution_mult-formula_component_mult)
    return mult


def calculate_remains(formula_component_mult, mult, next_formula_solution_mult):
    return (formula_component_mult * mult) - (next_formula_solution_mult)

def store_remains(remains, chem, r):
    if not chem in remains and r > 0:
        remains[chem] = int(r)
    elif r > 0:
        remains[chem] += int(r)

    remains = {x:y for x,y in remains.items() if y!=0}
    # print("Updated remains: " + str(remains))

def use_remains(remains, quantities):
    comp_remains = 0
    for comp in quantities:
        if comp in remains and remains[comp] > 0:
            print("**************** USING REMAINS")
            comp_remains = remains[comp]
            del remains[comp]
    return comp_remains

def count_chems(lines, formula, quantities, mult, depth, remains):
    # depth += 5
    formula_solution_mult, formula_solution_chem, formula_components = get_current_formula_values(formula)
    formula, formula_solution_mult = apply_discount_if_available(remains, formula_solution_mult, formula_solution_chem, formula)


    display_everything(depth, formula, quantities, remains, mult)

    if formula_solution_mult > 0:

        for component in formula_components:

            formula_component_mult, formula_component_chem = get_component_values(component)
            next_formula, next_formula_solution_mult, next_formula_solution_chem, next_formula_components = find_next_formula(lines, formula_component_chem)

            if 'ORE' not in next_formula:

                mult = calculate_multiplier(next_formula_solution_mult,quantities[formula_component_chem],formula_component_chem,remains)
                # comp_remains = use_remains(remains, quantities)
                store_quantities(quantities, formula_component_mult, formula_component_chem, mult)


                # print (mult, next_formula_solution_mult,quantities[formula_component_chem])
                # r = (mult * next_formula_solution_mult) - quantities[formula_component_chem]
                # store_remains(remains, formula_component_chem, r)



                count_chems(lines, next_formula, quantities, mult, depth+5, remains)
            else:
                mult = calculate_multiplier(next_formula_solution_mult,quantities[formula_component_chem],formula_component_chem,remains)
                display_everything(depth, next_formula, quantities, remains, mult)
                print("-"*200)





def count_ores(ores,quantities,remains):
    total = 0

    for ore in ores:
        solution_mult, solution_chem, ore_components = get_current_formula_values(ore)
        ore_mult, ore_chem = get_component_values(ore_components[0])
        ore, solution_mult = apply_discount_if_available(remains, solution_mult, solution_chem, ore)
        total += ore_mult * math.ceil(float(quantities[solution_chem]) / float(solution_mult))
        print(" * * * * * * ORE total : " + str(total))

    return int(total)


def main():
    filename = 'example1.txt'
    reactions = []
    ores = []

    with open(filename) as f:
        lines = f.read().splitlines()

    for l in lines:
        print(l)
        if 'FUEL' in l:
            fuel = l
            reactions.append(l)
        elif 'ORE' not in l:
            reactions.append(l)
        else:
            ores.append(l)
    print("-"*200)

    quantities, remains = {'FUEL': 1}, {}
    count_chems(lines, fuel, quantities, 1, -5, remains)
    total = count_ores(ores,quantities,remains)
    print(total)


if __name__ == '__main__':
    main()
