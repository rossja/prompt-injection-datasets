import csv
import os
from fuzzywuzzy import fuzz, process

infile = os.path.join(os.path.dirname(__file__), 'datasets', 'all-datasets.csv')
eqfile = os.path.join(os.path.dirname(__file__), 'datasets', 'all-datasets-deduped-eq.csv')
fuzzyfile = os.path.join(os.path.dirname(__file__), 'datasets', 'all-datasets-deduped-eqfuzzy.csv')

def equality_dedupe():
    reader = csv.reader(open(infile, 'r', encoding='utf-8'))
    writer = csv.writer(open(eqfile, 'w', encoding='utf-8'))

    fieldnames = ['set', 'prompt']

    prompts = set()
    print(f'\n\nDeduping using equality comparision')
    for row in reader:
        prompt = row[1]
        # only add the prompt if it's not already in the set using basic equality comparision
        if prompt not in prompts:
            writer.writerow(row)
            prompts.add(prompt)
    print(f'Deduping using equality comparision done!')
    return True


def fuzzymatch(prompt, prompts):
    cutoff = 90 # set the cutoff for the fuzzy matching
    if process.extractOne(prompt, prompts, scorer=fuzz.token_sort_ratio, score_cutoff=cutoff):
       return True
    else:
        return False

def fuzzy_dedupe():
    # note that we are using the deduped file from the equality comparision
    reader = csv.reader(open(eqfile, 'r', encoding='utf-8'))
    writer = csv.writer(open(fuzzyfile, 'w', encoding='utf-8'))
    fieldnames = ['set', 'prompt']

    prompts = set()
    print(f'Deduping using fuzzy match (levenshtein)')
    for row in reader:
        prompt = row[1]
        # only add the prompt if it's not already in the set using fuzzy matching
        if not fuzzymatch(prompt, prompts):
            writer.writerow(row)
            prompts.add(prompt)
    print(f'\nDeduping using fuzzy match done!\n\n')

if __name__ == '__main__':
    equality_dedupe()
    fuzzy_dedupe()
    print(f'\n\nAll done!\n\n')
FooterSalesforce
