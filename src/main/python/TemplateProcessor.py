
import os
import Constants
import re
import errno
from StylesheetYamlProcessor import *
from GraphDataProcessor import *


class TemplateProcessor:

    def __init__(self, startPath, inputTemplateFileName, outRelaPath, outputFileName):

        self.startPath = startPath
        self.templateFile = inputTemplateFileName
        self.outFile = outputFileName
        self.outputPath = outRelaPath

    def readFile(self, fileName):

        lines = []
        f = open(fileName, 'rt')
        for line in f:
            lines.append(line.strip())
        f.close()
        return lines


    def processTemplate(self):

        template_full_path = os.path.join(self.startPath, self.templateFile)
        self.make_sure_path_exists(template_full_path)
        lines = self.readFile(template_full_path)

        output_dir = os.path.join(self.outputPath)
        self.make_sure_path_exists(output_dir)
        self.output_dir = output_dir
        print self.output_dir
        self.outFile = os.path.join(self.output_dir, self.outFile)

        # Iterate over the lines of the file
        for line in lines:
            if not line.startswith('{%'):
                self.writeOutputFile(self.outFile, line)
            else:
                # process the line containing directives
                content = self.findBetween(line, Constants.constants.STARTTAG, Constants.constants.ENDTAG)
                fields = re.split(':', content)

                directCommand = fields[0].strip()
                directContent = fields[1].strip()
                if directCommand in Constants.constants.LOADDIRECTIVES:

                    full_path = os.path.join(self.startPath, directContent)
                    if directCommand == 'LoadStyleSheet':
                        styleProcessor = StylesheetYamlProcessor(full_path)
                        styleDict =  styleProcessor.readYaml()

                    else:
                        graphDataProcessor = GraphDataProcessor(full_path)
                        graphDataDict = graphDataProcessor.readYaml()


                if directCommand in Constants.constants.STYLEDIRECTIVES:
                    if styleDict[directContent]:
                        contentFields = directContent.split('.')
                        s = '%s[' %(contentFields[0].strip())
                        strList = list()
                        strList.append(s)
                        #print aline

                        for key,value in styleDict[directContent].iteritems():
                            #print key, '=', value
                            s = '%s="%s"\t' % (key, value)
                            strList.append(s)
                            #aline = aline.join(s)
                            #s = ''
                        strList.append(']')
                        s = ''.join(strList)
                        #print s
                        self.writeOutputFile(self.outFile, s)

                if directCommand in Constants.constants.DATADIRECTIVES:
                    if graphDataDict[directContent]:
                        self.writeOutputFile(self.outFile, str(graphDataDict[directContent]))


    def writeOutputFile(self, filename, line):

        if not os.path.exists(filename):
            with open(filename, 'w') as out:
                out.write(line)
                out.write('\n')
        else:
            with open(filename, 'a') as out:
                out.write(line)
                out.write('\n')


    def findBetween(self, str, start, end):

        result = re.search('%s(.*)%s' % (start, end),  str) # string substitution
        return result.group(1)


    def make_sure_path_exists(self, path):

        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise


    def processTemplateT2(self, path, T2outFileName):

        template_full_path = os.path.join(self.startPath, self.templateFile)
        self.make_sure_path_exists(template_full_path)
        lines = self.readFile(template_full_path)

        output_dir = os.path.join( path )
        self.make_sure_path_exists(output_dir)
        self.output_dir = output_dir
        t2_template_full_path = os.path.join(output_dir, T2outFileName)
        print t2_template_full_path


        # Iterate over the lines of the file
        for line in lines:
            if not line.startswith('{%'):
                self.writeOutputFile(t2_template_full_path, line)
            else:
                # process the line containing directives
                content = self.findBetween(line, Constants.constants.STARTTAG, Constants.constants.ENDTAG)
                fields = re.split(':', content)

                directCommand = fields[0].strip()
                directContent = fields[1].strip()

                if directCommand in Constants.constants.LOADDIRECTIVES:
                    if directCommand == 'LoadData':
                        full_path = os.path.join(self.startPath, directContent)
                        graphDataProcessor = GraphDataProcessor(full_path)
                        graphDataDict = graphDataProcessor.readYaml()
                    else:
                        self.writeOutputFile(t2_template_full_path, line)  # keep the LoadStyleSheet directive

                if directCommand in Constants.constants.DATADIRECTIVES:
                    if graphDataDict[directContent]:
                        self.writeOutputFile(t2_template_full_path, str(graphDataDict[directContent]))

                if directCommand in Constants.constants.STYLEDIRECTIVES:
                    self.writeOutputFile(t2_template_full_path, line) # not process style directives at step T2


    def processTemplateT1(self, T2outFileName, T1outFileName):

        t2_template_full_path = os.path.join(self.output_dir, T2outFileName)
        self.make_sure_path_exists(t2_template_full_path)
        lines = self.readFile(t2_template_full_path)

        t1_template_full_path = os.path.join(self.output_dir, T1outFileName)
        print t1_template_full_path

        # Iterate over the lines of the file
        for line in lines:
            if not line.startswith('{%'):
                self.writeOutputFile(t1_template_full_path, line)
            else:
                # process the line containing directives
                content = self.findBetween(line, Constants.constants.STARTTAG, Constants.constants.ENDTAG)
                fields = re.split(':', content)

                directCommand = fields[0].strip()
                directContent = fields[1].strip()

                if directCommand in Constants.constants.LOADDIRECTIVES:
                    if directCommand == 'LoadStyleSheet':
                        full_path = os.path.join(self.startPath, directContent)
                        styleProcessor = StylesheetYamlProcessor(full_path)
                        styleDict =  styleProcessor.readYaml()


                if directCommand in Constants.constants.STYLEDIRECTIVES:
                    if styleDict[directContent]:
                        contentFields = directContent.split('.')
                        s = '%s[' %(contentFields[0].strip())
                        strList = list()
                        strList.append(s)
                        #print aline

                        for key,value in styleDict[directContent].iteritems():
                            #print key, '=', value
                            s = '%s="%s"\t' % (key, value)
                            strList.append(s)

                        strList.append(']')
                        s = ''.join(strList)
                        #print s
                        self.writeOutputFile(t1_template_full_path, s)


if __name__ == '__main__':

    processor = TemplateProcessor('../../resources/examples/simulate_data_collection/test/', 'combinedDotTemplate.gv', 'output', 'comb.gv')

    ### process in two steps (T2 and T1)

    ## step T2: extend the graph to replace directives (Nodes, Edges) with the selected graph data
    processor.processTemplateT2('output', 't2_out_template.gv')

    ## step T1: apply styling rules to the output of T2
    processor.processTemplateT1('t2_out_template.gv', 't1_out_template.gv')

    ### process in one step
    #processor.processTemplate()
