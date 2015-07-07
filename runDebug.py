#!/usr/bin/env python

### IMPORTS ###
from flask import Flask

from gasmilage import gasmilage

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    app = Flask( __name__)
    app.register_blueprint( gasmilage)
    app.run( debug = True, host = '0.0.0.0')

if __name__ == '__main__':
    main()
