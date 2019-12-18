import sys
import re
import math

def multiply_formula(formula, mult):
    f = [x.strip() for x in formula.split()]
    for i, comp in enumerate(f):
        if comp.isdigit():
            f[i] = str(mult * int(comp))
    formula = ' '.join(f)
    return formula

def get_current_formula_values(formula):
    formula_solution = formula.split('=>')[1].strip()
    formula_solution_mult = int(formula_solution.split(' ')[0])
    formula_solution_chem = formula_solution.split(' ')[1]
    formula_components = [x.strip() for x in formula.split('=>')[0].split(',')]
    return formula_solution_mult, formula_solution_chem, formula_components

def display_everything(depth, formula, quantities, remains, mult):
    print (depth * ' ' + str(formula))
    print (depth * ' ' + str(quantities))
    print (depth * ' ' + str(remains))
    print (depth * ' ' + str(mult))
    print

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
        diff = abs(remains[chem] - mult)
        if remains[chem] >= mult:
            remains[chem] = diff
            new_mult = 0
        else:
            new_mult = diff
            remains[chem] = 0

        formula = formula.replace(str(mult) + ' ' + chem, str(diff) + ' ' + chem)

    return formula, mult

def calculate_multiplier(available_chem,formula_solution_mult,formula_component_mult):
    return int(math.ceil(float(available_chem) * float(formula_solution_mult) / float(formula_component_mult)))

def calculate_remains(formula_solution_mult, mult, available_chem, formula_component_mult):
    print(formula_solution_mult, mult, available_chem, formula_component_mult)
    return (formula_solution_mult * mult) - (available_chem * formula_component_mult)

def store_remains(remains, formula_component_chem, mult, r):
    if not formula_component_chem in remains:
        remains[formula_component_chem] = int(r)
    else:
        remains[formula_component_chem] += int(r)

def use_remains(remains, quantities):
    for comp in quantities:
        if comp in remains:
            quantities[comp] += remains[comp]
            remains[comp] = 0

def count_chems(lines, formula, quantities, sol_mult, depth, remains):
    formula_solution_mult, formula_solution_chem, formula_components = get_current_formula_values(formula)
    mult = calculate_multiplier(quantities[formula_solution_chem],formula_solution_mult,sol_mult)


    # formula, formula_solution_mult = apply_discount_if_available(remains, formula_solution_mult, formula_solution_chem, formula)

    for component in formula_components:
        formula_component_mult, formula_component_chem = get_component_values(component)
        store_quantities(quantities, formula_component_mult, formula_component_chem, mult)
        display_everything(depth, formula, quantities, remains, mult)


        next_formula, next_formula_solution_mult, next_formula_solution_chem, next_formula_components = find_next_formula(lines, formula_component_chem)


        r = calculate_remains(formula_solution_mult, mult, quantities[formula_solution_chem], formula_component_mult)
        store_remains(remains, formula_component_chem, formula_solution_mult, r)

        if 'ORE' in next_formula:
            use_remains(remains,quantities)

        if next_formula:
            count_chems(lines, next_formula, quantities, formula_component_mult, depth+5, remains)


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
    filename = 'example3.txt'
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
    print ("--------------------------------------------------------------")

    quantities, remains = {'FUEL': 1}, {}
    count_chems(lines, fuel, quantities, 1, -5, remains)
    total = count_ores(ores,quantities,remains)
    print total


if __name__ == '__main__':
    main()
