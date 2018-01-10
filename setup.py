
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
from setuptools import setup, find_packages
                         
setup(
  name             = 'conquests',
  version          = '1.0.1',
  license          = 'GPLv3+',
  description      = 'Crossroads in metabOlic NEtwork from Stoichiometrical and Topological Studies',
  long_description = 'Python 3 tool to analyze metabolic networks through the computation of metabolic crossroads',
  author           = 'Julie Laniau',
  author_email     = 'laniau.julie@orange.fr',
  packages         = find_packages(),
  install_requires = ['pyasp','cobra'], 
  zip_safe         = False
)
