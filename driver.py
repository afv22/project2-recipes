import sys

from get_recipe_data import get_recipe_data

from src.parse_ingredients import parse_ingredients
from src.query_methods import query_methods
from src.query_tools import query_tools
from src.query_steps import query_steps

from src.change_health import change_health
from src.to_indian import to_indian
from src.to_med import to_mediterranean

from src.supplemental_project2 import *

from src.helpers import *

def main():
	print('Welcome to the Recipe Transformer!\n')
	url = input('Please enter the url of a recipe:\n>> ')

	recipe_data = get_recipe_data(url)

	print('\n' + recipe_data['title'] + '\n')

	ingredients = parse_ingredients(recipe_data['ingredients'])
	methods = query_methods(recipe_data['directions'])
	tools = query_tools(ingredients, recipe_data['directions'])

	steps = query_steps(ingredients, recipe_data['directions'], tools, methods['methods'])

	print('\nPlease enter the number of your desired transformation:\n'
		'1: Healthier\n'
		'2: Unhealthier\n'
		'3: Vegetarian\n'
		'4: Non-Vegetarian\n'
		'5: Indian\n'
		'6: Mediterranean\n'
		'7: Double')

	while True:
		transform = input('>> ')
		if transform == '1':
			change_health(True, steps)
		elif transform == '2':
			change_health(False, steps)
		elif transform == '3':
			make_veg(steps)
		elif transform == '4':
			make_meat(steps)
		elif transform == '5':
			to_indian(steps)
		elif transform == '6':
			to_mediterranean(steps)
		elif transform == '7':
			double_amount(steps)
		else:
			print('Invalid Input')
			continue

		break

	print_recipe(steps)

	print('\nBon Appetit!')

if __name__== '__main__':
	main()
