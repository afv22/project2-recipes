import requests
from bs4 import BeautifulSoup
import random
from src.helpers import unibigrams
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import re
import fractions
import sys
import itertools
from nltk.corpus import stopwords
from string import punctuation
import random


def to_indian(steps):
    spices = [line.strip() for line in open('data/spices.txt')]
    sauces = [line.strip() for line in open('data/sauces.txt')]
    indian_spices = [line.strip() for line in open('data/indian_spices.txt')]
    indian_sauces = [line.strip() for line in open('data/indian_sauces.txt')]
    breads = [line.strip() for line in open('data/breads.txt')]
    cheeses = [line.strip() for line in open('data/cheeses.txt')]
    red_meats = [line.strip() for line in open('data/red_meats.txt')]
    ans_spices = unibigrams(spices)
    ans_sauces = unibigrams(sauces)
    ans_cheese = unibigrams(cheeses)
    ans_rm = unibigrams(red_meats)
    ans_breads = unibigrams(breads)
    
    for step in steps:
        for i in step['ingredients']:
            name = word_tokenize(i)
            if len(name) == 1:
                if name[0] in spices:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(indian_spices), step['ingredients']))
                elif name[0] in sauces:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(indian_sauces), step['ingredients']))
                elif name[0] == 'rice':
                    step['ingredients'] = list(map(lambda x: x if x != i else 'basmati rice', step['ingredients']))
                elif name[0] in breads:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'naan', step['ingredients']))
                elif name[0] in red_meats:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'chicken', step['ingredients']))
                elif name[0] in cheeses:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'paneer', step['ingredients']))
                #else:
                #    new_dict[key] = value
            elif len(name) == 2:
                if name in ans_spices['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(indian_spices), step['ingredients']))
                elif name in ans_sauces['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(indian_sauces), step['ingredients']))
                elif name in ans_breads['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'naan', step['ingredients']))
                elif name in ans_rm['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'chicken', step['ingredients']))
                elif name in ans_cheese['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'paneer', step['ingredients']))
               # else:
               #     new_dict[key] = value
            elif len(name) == 3:
                if name in ans_spices['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(indian_spices), step['ingredients']))
                elif name in ans_sauces['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(indian_sauces), step['ingredients']))
                elif name in ans_breads['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'naan', step['ingredients']))
                elif name in ans_rm['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'chicken', step['ingredients']))
                elif name in ans_cheese['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'paneer', step['ingredients']))
    return steps
