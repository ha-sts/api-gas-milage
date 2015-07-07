#!/usr/bin/env python

### IMPORTS ###
import json

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

### GLOBALS ###
gasmilage = Blueprint( 'gasmilage', __name__, template_folder = 'templates')

### FUNCTIONS ###
@gasmilage.route( '/')
def show():
    try:
        return render_template( 'index.html')
    except TemplateNotFound:
        abort( 404)

### CLASSES ###

### MAIN ###
if __name__ == '__main__':
    pass
