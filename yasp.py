"""YASP

Usage:
  yasp <starting-path> <template-file-name> <output-directory> <output-file-name>
  yasp [-h | --help]
  yasp [--version]

Options:
  -h --help     show this screen.
  --version     show version.

"""

from docopt import docopt
from src.main.python.TemplateProcessor import TemplateProcessor as TemplateProcessor

def main():
    args = docopt(__doc__)

    print args

    if args['--version']:
        print 'template project'
        return

    startPath = args['<starting-path>']
    print startPath

    templateFile = args['<template-file-name>']
    print templateFile

    outputPath = args['<output-directory>']

    outputFileName = args['<output-file-name>']

    processor = TemplateProcessor(startPath, templateFile, outputPath, outputFileName)


    # T2: import graph data to replace directives (Nodes, Edges) with the selected graph data
    processor.processTemplateT2(outputPath, 'default_t2_output.gv')

    # T1: apply styling rules to the output of T2
    processor.processTemplateT1('default_t2_output.gv', outputFileName)


if __name__ == '__main__':
    main()