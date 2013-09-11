from setuptools import setup, find_packages
import os

version = '1.7'

setup(name='wcc.assemblypolicy',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Izhar Firdaus',
      author_email='izhar@inigo-tech.com',
      url='http://github.com/inigoconsulting/wcc.assemblypolicy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['wcc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'collective.carousel',
        'Products.ContentWellPortlets',
        'Products.BlingPortlet',
        'plone.app.dexterity',
        'fourdigits.portlet.twitter',
        'redturtle.video',
        'collective.rtvideo.youtube',
        'collective.rtvideo.vimeo',
        'collective.contentleadimage',
        'wcc.tinymce',
        'collective.socialbar',
        'collective.plonetruegallery',
        'collective.ptg.presentation',
        'collective.ptg.galleriffic',
        'collective.ptg.highslide',
        'collective.ptg.nivoslider',
        'collective.ptg.nivogallery',
        'collective.ptg.contentflow',
        'wcc.songs',
        'wcc.common',
        'Products.RedirectionTool',
        'collective.js.moment',
        'wcc.twitterportlet',
        'z3c.jbot',
        'wcc.assemblytheme',
        'wcc.songs',
        'wcc.content',
        'collective.js.jqueryui',
        'wcc.videolink',
        'wcc.assemblyhomepage',
        'wcc.programmeplanner',
        'wcc.video'
        # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone

      """,
      )
