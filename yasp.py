#!/usr/bin/env python

"""Stylesheet Processor

Usage:
    yasp  graph <input-directory> <template-file-name> <output-directory> <output-file-name>
    yasp  open <file-name>
    yasp  dot2pdf  <output-directory> <dot-file-name> <pdf-file-name>
    yasp [--help]
    yasp  [--version]

Options:
  --help     show this screen.
  --version     show version.
"""

from docopt import docopt
from src.main.python.TemplateProcessor import TemplateProcessor as TemplateProcessor
from subprocess import call
import os

def main():
    args = docopt(__doc__)
    print args

    if args['--version']:
        print 'template project'
        return

    if args['--help']:
        print args
        return

    if args['graph']:
        inputPath = args['<input-directory>']

        templateFile = args['<template-file-name>']

        outputPath = args['<output-directory>']

        outputFileName = args['<output-file-name>']

        # initialize a template processor
        processor = TemplateProcessor(inputPath, templateFile, outputPath, outputFileName)

        # T2: import graph data to replace directives (Nodes, Edges) with the selected graph data
        processor.processTemplateT2(outputPath, 'default_t2_output.gv')

        # T1: apply styling rules to the output of T2
        processor.processTemplateT1('default_t2_output.gv', outputFileName)
        return

    if args['open']:
        fileName = args['<file-name>']
        call(["open", fileName])
        return

    if args['dot2pdf']:
        outputPath = args['<output-directory>']
        dotFileName = args['<dot-file-name>']
        dotFile = os.path.join(outputPath, dotFileName)
        pdfFileName = args['<pdf-file-name>']
        pdfFile = os.path.join(outputPath, pdfFileName)
        call(["dot", "-Tpdf", dotFile, "-o", pdfFile])
        return

if __name__ == '__main__':
    main()