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
#from sets import Set

#from xlwt import Workbook
import csv
  
def clean_up() :
    if os.path.isfile("parser.out"): os.remove("parser.out")
    if os.path.isfile("parsetab.py"): os.remove("parsetab.py")
    if os.path.isfile("asp_py_lextab.py"): os.remove("asp_py_lextab.py")
    if os.path.isfile("asp_py_lextab.pyc"): os.remove("asp_py_lextab.pyc")
    if os.path.isfile("asp_py_parsetab.py"): os.remove("asp_py_parsetab.py")
    if os.path.isfile("asp_py_parsetab.pyc"): os.remove("asp_py_parsetab.pyc")
  
    
def split_proj_id(answer) :
    'renvoie un dico avec [id : {[number,[target]]}]'
    crossroads = {}
    for element in answer :
        if element.pred() == "crossroad" : 
            id_cross = element.arg(0).replace("\"","")
            if id_cross not in crossroads.keys() :
                crossroads.update({id_cross : [0]})
                
        elif element.pred() == "subtarget" : 
            id_target = element.arg(0).replace("\"","")
            id_cross = element.arg(1)  .replace("\"","")
            if id_cross in crossroads.keys() :
                crossroads[id_cross][0] += 1
                crossroads[id_cross].append(id_target)
            else :
                crossroads.update({id_cross : [1,id_target]})
                
    return crossroads

def print_crossroad(answer, dico, file_name, option_ecriture="wt",titre="") :
    #answer : dictionnaire => id_cross : {nbre_target, [target]}
    #dico : dictionnaire => {id_metabolite : [nom,compartiment]}
        
    file = open(file_name,option_ecriture)
    writer = csv.writer(file,delimiter="\t")
    if titre != "" :
        writer.writerow([titre+" :"])
    if len(list(dico)[0]) == 2 :
        writer.writerow(['identifiant','name','compartment','number of targets','targets'])
    else :
        writer.writerow(['identifiant','name','number of targets','targets'])
        
    for element in answer.keys() :
        try :
            writer.writerow([element.replace("\"","")]+dico[element.replace("\"","")]+answer[element.replace("\"","")]) 
        except KeyError :
            writer.writerow([element.replace("\"","")]+[element.replace("\"","")]) 
            print(element,"pas dans le dico !!!!!!!!!!!!!!!!!!!!!!")

    file.close()



