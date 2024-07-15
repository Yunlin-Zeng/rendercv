import bibtexparser
import yaml

def bibtex_to_yaml(bibtex_file, yaml_file):
    with open(bibtex_file) as bibfile:
        bib_database = bibtexparser.load(bibfile)
    
    publications = []
    for entry in bib_database.entries:
        publication = {
            'title': f"*{entry.get('title', '')}*",
            'authors': entry.get('author', '').replace(' and ', ', ').split(', '),
            'doi': entry.get('doi', ''),
            'date': f"{entry.get('year', '')}-01"  # Assuming only year is given
        }
        publications.append(publication)
    
    with open(yaml_file, 'w') as yamlfile:
        yaml.dump({'publications': publications}, yamlfile, sort_keys=False, default_flow_style=False)

# Convert the BibTeX file to YAML
bibtex_to_yaml('my_citations.bib', 'bibtex.yaml')

