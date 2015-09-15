# TemplateProject

This styplesheet processor is used for customizing and visualizing the outputs from yesWorkflow. It requries three input files: template file (F), graph data file (G), and stylesheet yaml file (S). It can produce a valid dot file (D). 

The template file contains 3 different directives (placeholders): LOADDIRECTIVES ("LoadStyleSheet", "LoadData"), STYLEDIRECTIVES ("ApplyNodeStyle", "ApplyEdgeStyle"), DATADIRECTIVES ("Nodes", "Edges"). A directives statement is denoted by a starttag ("{%") and anendgtag ("%}"). 

Installation:
1. Download the TemplateProject to your local machine which runs linux-family operating system.
2. Install docopt library from https://github.com/docopt/docopt#installation
