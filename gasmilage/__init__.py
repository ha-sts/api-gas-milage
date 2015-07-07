#!/usr/bin/env python

### IMPORTS ###
from flask import Flask

### GLOBALS ###
app = Flask( __name__)

### FUNCTIONS ###
@app.route( '/')
def hello():
    return "Hello World!"

### CLASSES ###

### MAIN ###
def main():
    app.run()

if __name__ == '__main__':
    main()
