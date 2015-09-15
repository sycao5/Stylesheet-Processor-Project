# Stylesheet Processor Project

A. Introduction
================

This stylesheet processor is used for customizing and visualizing the outputs from yesWorkflow. It requires three input files: `template file (F)`, `graph data yaml file (G)`, and `stylesheet yaml file (S)`. It can produce a valid `dot file (D)`.

B. Architecture
===============

The current template syntax supports 3 different directives (placeholders):

(1) LOADDIRECTIVES (`LoadStyleSheet`, `LoadData`)

(2) STYLEDIRECTIVES (`ApplyNodeStyle`, `ApplyEdgeStyle`)

(3) DATADIRECTIVES (`Nodes`, `Edges`)

A directives statement is denoted by a starttag (`{%`) and an endtag (`%}`)


C. Installation:
================

(1) Download the `Stylesheet Processor Project` to your local machine which runs linux-family operating system.

(2) Install `docopt` library from https://github.com/docopt/docopt#installation.

(3) Install `Graphviz` visualization software from http://graphviz.org/Download.php
 
 
D. Run StyleProcessor on the example
=====================================

The example input files are in the directory ([`src/resources/examples/simulate_data_collection/input/`](https://github.com/sycao5/Stylesheet-Processor-Project/tree/master/src/resources/examples/simulate_data_collection/input)). The example template file is ([`combinedDotTemplate.gv`](https://github.com/sycao5/Stylesheet-Processor-Project/blob/master/src/resources/examples/simulate_data_collection/input/combinedDotTemplate.gv)), the example graph data yaml file is ([`combined.yaml`](https://github.com/sycao5/Stylesheet-Processor-Project/blob/master/src/resources/examples/simulate_data_collection/input/combined.yaml)), and the example stylesheet yaml file is ([`stylesheet.yaml`](https://github.com/sycao5/Stylesheet-Processor-Project/blob/master/src/resources/examples/simulate_data_collection/input/stylesheet.yaml)) .

(1) Go to the installation folder: 

    cd StylesheetProcessorProject/

(2) To display the help menu:  `./yasp.py --help`
      
    Stylesheet Processor
    Usage:
        yasp  graph <input-directory> <template-file-name> <output-directory> <output-file-name>
        yasp  open <file-name>
        yasp  dot2pdf  <output-directory> <dot-file-name> <pdf-file-name>
        yasp [--help]
        yasp  [--version]
    
(3) To generate a dot graph:
    
    ./yasp.py graph src/resources/examples/simulate_data_collection/input/  combinedDotTemplate.gv   output   comb2.gv 

(4) To open a file: 

    ./yasp.py open output/comb2.gv 

(5) To transform a dot file to a pdf file: 

    ./yasp.py dot2pdf output comb2.gv comb_gray.pdf 

(6) To open the generated pdf file:  

    ./yasp.py open output/comb_gray.pdf 


E. Change the stylesheet rules
===============================

(1) Go to the folder ([`src/resources/examples/simulate_data_collection/input/`] (https://github.com/sycao5/Stylesheet-Processor-Project/tree/master/src/resources/examples/simulate_data_collection/input)) and open the ([`stylesheet.yaml`](https://github.com/sycao5/Stylesheet-Processor-Project/blob/master/src/resources/examples/simulate_data_collection/input/stylesheet.yaml)) file

(2) Change the color for the AtomicProgramNodes from Gray to Yellow. 

    Gray color: `node.AtomicProgramNodes: {shape: box, style: filled, fillcolor: "gray", peripheries: 1, fontname: Courier}`

    Yellow color: `node.AtomicProgramNodes: {shape: box, style: filled, fillcolor: "yellow", peripheries: 1, fontname: Courier}` 

(3) Save the changes.

(4) Go to the root folder of the project, run

    ./yasp.py graph src/resources/examples/simulate_data_collection/input/  combinedDotTemplate.gv   output   comb-yellow.gv 

(5) The generated dot file `comb-yellow.gv` is located in the `output/` folder


F. Demo
========

(1) Display Yellow color image ([`comb_yellow.pdf`](https://github.com/sycao5/Stylesheet-Processor-Project/blob/master/output/comb_yellow.pdf))

(2) Display Gray color image ([`comb_gray.pdf`](https://github.com/sycao5/Stylesheet-Processor-Project/blob/master/output/comb_gray.pdf))




