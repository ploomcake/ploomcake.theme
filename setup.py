# Authors: Andrea D'Este <andrea.deste@ploomcake.com> and contributors (see docs/CONTRIBUTORS.txt)
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#

from setuptools import setup, find_packages
import os

version = '1.8'

setup(name='ploomcake.theme',
      version=version,
      description="An installable theme for Plone 4 based on redomino.css3theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author="Andrea D'Este",
      author_email='andrea.deste@redomino.com',
      url='https://github.com/ploomcake/ploomcake.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploomcake'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'redomino.breadcrumbsbrain',
          'redomino.css3theme>=1.3',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
