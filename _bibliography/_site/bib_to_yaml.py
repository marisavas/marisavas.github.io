#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bibtexparser
import yaml
import os

# Mapear os arquivos .bib para os arquivos .yml
files = {
    "publications.bib": "publications.yml",
    "journals.bib": "journals.yml",
    "patents.bib": "patents.yml"
}

def bib_to_yaml(bib_file, yml_file):
    if not os.path.exists(bib_file):
        print("Atenção: {} não encontrado. Pulando.".format(bib_file))
        return
    
    with open(bib_file, encoding='utf-8') as bib:
        bib_database = bibtexparser.load(bib)
    
    yaml_list = []
    for entry in bib_database.entries:
        item = {
            'title': entry.get('title', ''),
            'authors': [a.strip() for a in entry.get('author', '').split(' and ')],
            'year': int(entry.get('year', 0)) if entry.get('year') else None,
            'venue': entry.get('journal', entry.get('booktitle', '')),
            'url': entry.get('url', ''),
            'pdf': entry.get('file', ''),
            'doi': entry.get('doi', ''),
            'abstract': entry.get('abstract', '')
        }
        yaml_list.append(item)
    
    with open(yml_file, 'w', encoding='utf-8') as yml:
        yaml.dump(yaml_list, yml, sort_keys=False, allow_unicode=True)
    
    print("{} → {} concluído!".format(bib_file, yml_file))


# Executar a conversão para todos os arquivos
for bib_file, yml_file in files.items():
    yml_file = f'../_data/{yml_file}'
    bib_to_yaml(bib_file, yml_file)
