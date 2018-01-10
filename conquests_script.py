#!python
# -*- coding: utf-8 -*-
import argparse
import sys
import os.path

    
from conquests.seed_target_sbml import seed_target_from_sbml
from conquests.topo_crossroad import topological_crossroad
from conquests.stoichio_crossroad import stoichio_crossroad
from conquests.optimal_crossroad import optimal_crossroad

if __name__ == '__main__':


    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--draftnet", help='metabolic network in SBML format', required=True)
    parser.add_argument("-b","--biomass", help='identifiant of biomass reaction', required=True)
    parser.add_argument("-s","--seed", help='list of boundary seeds in SBML format for topological search', default="")
    parser.add_argument("-t","--target", help='list of biomass compounds in SBML format', default="")
    parser.add_argument('-l', '--limit', help='limit to flux value to be considered as null (by default 10E-5)', type=float, default=1E-5)
    parser.add_argument('-r',"--repository", help="repository to store the answer-files (by default named answer_file in draft repository)",default="")


    args         = parser.parse_args()
    draft        = args.draftnet
    biomass_id   = args.biomass
    seed_cofactor= args.seed
    target       = args.target
    limit        = args.limit
    repository   = args.repository
    
    if repository == "" :
        repository = "/".join(draft.split("/")[:-1])+"/answer_file/"
    else :
        if repository[-1] != "/" : repository += "/"
    
    if not os.path.isdir(repository) :
        os.makedirs(repository)
    
    
    seed_target_from_sbml(draft, biomass_id,repository)
    seed = repository+"seeds_from_sbml.sbml"
    target = repository+"targets_from_sbml.sbml"
    
    if seed_cofactor == "" :
        topological_crossroad(draft, seed, target, repository)
    else :
        topological_crossroad(draft, seed_cofactor, target, repository)
   

    stoichio_crossroad(draft, draft, seed, target, limit, repository)

    optimal_crossroad(draft, seed, target, limit, repository)
