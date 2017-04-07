# Copyright (c) 2012, Sven Thiele <sthiele78@gmail.com>
#
# This file is part of meneco.
#
# meneco is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# meneco is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with meneco.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-
import os
import tempfile
from pyasp.asp import *

root = __file__.rsplit('/', 1)[0]

producible_prg =      root + '/encodings/producible_targets.lp'
project_cross   =       root + '/encodings/proj_cross.lp'
#project_class   =       root + '/encodings/proj_class.lp'
#projection      =       root + '/encodings/proj_proj.lp'

def get_producible(draft, seeds, targets):
    draft_f = draft.to_file()
    seed_f =  seeds.to_file()
    target_f = targets.to_file()
    prg = [producible_prg, draft_f, seed_f, target_f ]
    solver = Gringo4Clasp()
    models = solver.run(prg,collapseTerms=True,collapseAtoms=False)
    assert(len(models) == 1)
    os.unlink(draft_f)
    os.unlink(seed_f)
    os.unlink(target_f)
    return models[0]


def compute_crossroad(draft, seeds, targets):
    draft_f = draft.to_file()
    seed_f =  seeds.to_file()
    target_f = targets.to_file()
    prg = [project_cross, draft_f, seed_f, target_f]
    solver = Gringo4Clasp()
    models = solver.run(prg,collapseTerms=True, collapseAtoms=False)
    assert(len(models) == 1)
    os.unlink(draft_f)
    os.unlink(seed_f)
    os.unlink(target_f)
    return models[0] 
    
#def compute_classes(draft, seeds, targets, crossroad):
    #instance = draft.union(seeds).union(targets)
    #instance_f = TermSet(instance).to_file()
    #crossroad_f = TermSet(crossroad).to_file()
    #prg = [project_class, instance_f, crossroad_f]
    #solver = Gringo4Clasp()
    #models = solver.run(prg,collapseTerms=True, collapseAtoms=False)
    #os.unlink(instance_f)
    #assert(len(models) == 1)
    #return models[0] 
    
#def search_projection(draft, seeds, targets) : 
    #"recherche element produit, consomme et necessaire a au moins une target"
    #"les regroupe en classe d'equivalence et renvoie un de la classe"
    #draftfac = TermSet(draft.union(String2TermSet('draft("draft")')))
    #draft_f = draftfac.to_file()
    #seed_f =  seeds.to_file()
    #target_f = targets.to_file()
    #crossroad = compute_crossroad(draftfac, seeds, targets)
    #classes = compute_classes(draftfac, seeds, targets, crossroad)
    #crossroad_f = crossroad.to_file()
    #classes_f = classes.to_file()
    #prg = [projection, draft_f, seed_f, target_f, crossroad_f, classes_f ]
    #solver = Gringo4Clasp()
    #models = solver.run(prg,collapseTerms=True,collapseAtoms=False)
    #os.unlink(draft_f)
    #os.unlink(seed_f)
    #os.unlink(target_f)
    #return models[0]  
    

