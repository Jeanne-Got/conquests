# CONQUESTS

Conquests is Python3 tools to calculate :
* topological crossraods (TC)
* stoichiometrical crossroads (SC)
* optimal_biomass based crossroads (OBC)

Required package:
* ``pyasp`` (``pip install pyasp``)
* ``cobrapy`` (``pip install cobrapy``)

## Install

```
python setup.py install
```

## usage

```
conquests.py [-h] -d DRAFTNET -b BIOMASS [-s SEED] [-t TARGET] [-l LIMIT] [-r REPOSITORY]

optional arguments:
  -h, --help            show this help message and exit
  -d DRAFTNET, --draftnet DRAFTNET
                        metabolic network in SBML format
  -b BIOMASS, --biomass BIOMASS
                        identifiant of biomass reaction
  -s SEED, --seed SEED  
			list of boundary seeds in SBML format for topological search
  -t TARGET, --target TARGET
                        list of biomass compounds in SBML format
  -l LIMIT, --limit LIMIT
                        limit to flux value to be considered as null
  -r REPOSITORY, --repository REPOSITORY
                        repository to store the answer-files (by default named answer_file in draft repository)

```
