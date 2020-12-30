import sys
import os
import math


def give_me_ingredients(req_element, conversions):
    for output in conversions.keys():
        if req_element == output.split(' ')[1]:
            return output


def calculate_ingredients(conversions, req_amount, req_element, depth):
    output = give_me_ingredients(req_element, conversions)
    inputs = conversions[output].split(', ')
    output_amount = int(output.split(" ")[0])

    for i in inputs:
        input_amount, input_element = i.split(' ')
        input_amount = int(input_amount)
        multiplier = int(math.ceil(req_amount / output_amount))
        required_amount = (multiplier * input_amount)

        if input_element not in requirements.keys(): requirements[input_element] = 0

        if input_element != "ORE":
            if requirements[input_element] < 0: required_amount += requirements[input_element]
            calculate_ingredients(conversions, required_amount, input_element, depth + 1)

        requirements[input_element] += (multiplier * input_amount)

    requirements[req_element] -= (multiplier * output_amount)


def main():
    cwd = os.path.dirname(os.path.realpath(__file__))
    with open(cwd + '/input.txt') as f:
        reactions = f.read().splitlines()

    global requirements, conversions
    fuel = 1

    requirements = { "FUEL": fuel, "ORE": 0 }
    conversions  = {}

    for reaction in reactions:
        left, right = reaction.split(' => ')
        conversions[right] = left

    calculate_ingredients(conversions, fuel, "FUEL", 0)
    print(requirements["ORE"])

if __name__ == '__main__':
    main()
