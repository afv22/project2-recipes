from src.helpers import unibigrams

def to_mediterranean(steps):
    cheeses = [line.strip() for line in open('data/cheeses.txt')]
    dressings = [line.strip() for line in open('data/dressings.txt')]
    red_meats = [line.strip() for line in open('data/red_meats.txt')]
    meats = [line.strip() for line in open('data/meats.txt')]
    breads = [line.strip() for line in open('data/breads.txt')]
    sauces = [line.strip() for line in open('data/sauces.txt')]
    dressings = [line.strip() for line in open('data/dressings.txt')]
    spices = [line.strip() for line in open('data/spices.txt')]
    veggies = ['onion','red pepper','tomato','peppers','green pepper','roasted vegetables']
    ans_veggies = unibigrams(veggies)
    ans_spices = unibigrams(spices)
    ans_sauces = unibigrams(sauces)
    ans_cheeses = unibigrams(cheeses)
    ans_meats = unibigrams(meats)
    ans_rm = unibigrams(red_meats)
    ans_breads = unibigrams(breads)
    ans_dressings = unibigrams(dressings)
    med = ["lamb", "chicken", "falafel"]
    med_sauces = ["Tahini sauce","Tzatziki sauce","Chermoula","Harissa","Toum"]
    c_f = ['chicken','falafel']
    med_spices = ['za\'atar','rosemary','sage','basil']
    
    for step in steps:
        for i in step['ingredients']:
            name = word_tokenize(i)
            if len(name) == 1:
                if name[0] in spices:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(med_spices), step['ingredients']))
                elif name[0] in breads:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'pita', step['ingredients']))
                elif name[0] in sauces:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(med_sauces), step['ingredients']))
                elif name[0] in cheeses:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'feta cheese', step['ingredients']))
                elif name[0] == 'butter':
                    step['ingredients'] = list(map(lambda x: x if x != i else 'olive oil', step['ingredients']))
                elif name[0] in meats:
                    if name[0] in red_meats:
                        step['ingredients'] = list(map(lambda x: x if x != i else 'lamb', step['ingredients']))
                    else:
                        step['ingredients'] = list(map(lambda x: x if x != i else random.choice(c_f), step['ingredients']))
                elif name[0] in dressings:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'Greek dressing', step['ingredients']))
            elif len(name) == 2:
                if name[0] in ans_spices['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(med_spices), step['ingredients']))
                elif name[0] in ans_breads['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'pita', step['ingredients']))
                elif name[0] in ans_sauces['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(med_sauces), step['ingredients']))
                elif name[0] in ans_cheeses['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'feta cheese', step['ingredients']))
                elif name[0] in ans_meats['bigrams']:
                    if name[0] in ans_rm['bigrams']:
                        step['ingredients'] = list(map(lambda x: x if x != i else 'lamb', step['ingredients']))
                    else:
                        step['ingredients'] = list(map(lambda x: x if x != i else random.choice(c_f), step['ingredients']))
                elif name[0] in ans_dressings['bigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'Greek dressing', step['ingredients']))
            elif len(name) == 3:
                if name[0] in ans_spices['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(med_spices), step['ingredients']))
                elif name[0] in ans_breads['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'pita', step['ingredients']))
                elif name[0] in ans_sauces['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else random.choice(med_sauces), step['ingredients']))
                elif name[0] in ans_cheeses['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'feta cheese', step['ingredients']))
                elif name[0] in ans_meats['trigrams']:
                    if name[0] in ans_rm['trigrams']:
                        step['ingredients'] = list(map(lambda x: x if x != i else 'lamb', step['ingredients']))
                    else:
                        step['ingredients'] = list(map(lambda x: x if x != i else random.choice(c_f), step['ingredients']))
                elif name[0] in ans_dressings['trigrams']:
                    step['ingredients'] = list(map(lambda x: x if x != i else 'Greek dressing', step['ingredients']))
        
        return steps
