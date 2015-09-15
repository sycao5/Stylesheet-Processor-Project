"""Stylesheet Processor

Usage:
  yasp <input-directory> <template-file-name> <output-directory> <output-file-name>
  yasp [--help]
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

    if args['--help']:
        print args
        return

    inputPath = args['<input-directory>']
    print inputPath

    templateFile = args['<template-file-name>']
    print templateFile

    outputPath = args['<output-directory>']

    outputFileName = args['<output-file-name>']

    processor = TemplateProcessor(inputPath, templateFile, outputPath, outputFileName)


    # T2: import graph data to replace directives (Nodes, Edges) with the selected graph data
    processor.processTemplateT2(outputPath, 'default_t2_output.gv')

    # T1: apply styling rules to the output of T2
    processor.processTemplateT1('default_t2_output.gv', outputFileName)


if __name__ == '__main__':
    main()