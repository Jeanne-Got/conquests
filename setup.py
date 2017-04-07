
# Copyright (c) 201-, Julie Laniau <laniau.julie@orange.fr>
#
# This file is part of conquests.
#
# conquests is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# conquests is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with conquests.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-
from setuptools import setup
                         
setup(
  name             = 'conquests',
  version          = '1.0.0',
  #url              = 'http://bioasp.github.io/conquests/',
  #download_url     = 'https://github.com/cfrioux/MeneTools/tarball/1.0.2',
  license          = 'GPLv3+',
  description      = 'Crossroads in metabOlic NEtwork from Stoichiometrical and Topological Studies',
  long_description = 'Python 3 tool to analyze metabolic networks through the computation of metabolic crossroads',
  author           = 'Julie Laniau',
  author_email     = 'laniau.julie@orange.fr',
  packages         = ['conquests'],
  package_dir      = {'conquests' : 'src'},
  package_data     = {'conquests' : ['encodings/*.lp']},
  scripts          = ['conquests.py'],
  install_requires = ['pyasp == 1.4.2','cobra == 0.5.4']
)
