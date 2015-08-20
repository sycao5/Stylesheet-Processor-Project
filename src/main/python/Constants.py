from collections import namedtuple

Constants = namedtuple('Constants', ['LOADDIRECTIVES', 'STYLEDIRECTIVES', 'DATADIRECTIVES', 'STARTTAG', 'ENDTAG'])
constants = Constants(['LoadStyleSheet', 'LoadData'], ['ApplyNodeStyle', 'ApplyEdgeStyle'], ['Nodes', 'Edges'], '{%', '%}')


#print constants.LOADDIRECTIVES
#print constants.STYLEDIRECTIVES
#print constants.DATADIRECTIVES
#print constants.STARTTAG
#print constants.ENDTAG