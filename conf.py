import os
import sys
 
# Ajouter le chemin du module à la variable sys.path
sys.path.insert(0, os.path.abspath('../'))
 
project = 'Doc Logs'
copyright = '2024, gabriel'
author = 'gabriel'
release = 'V1'
 
# Extensions Sphinx utilisées
extensions = [
    'sphinx.ext.autodoc',  # Pour générer la documentation à partir des docstrings
    'sphinx.ext.viewcode',  # Pour inclure des liens vers le code source
    'sphinx.ext.napoleon'   # Pour supporter les styles Google et NumPy de docstrings
]
 
templates_path = ['_templates']
exclude_patterns = []
 
# Thème pour la sortie HTML
html_theme = 'alabaster'
html_static_path = ['_static']