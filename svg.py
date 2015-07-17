#coding=utf-8

import subprocess
import os
import cairosvg
import config
import time


# for test
# subprocess.Popen('./svg-sprite/bin/svg-sprite.js -cD output --ccss --cx assets/*.svg',shell=True)
# subprocess.Popen('./svg-sprite/bin/svg-sprite.js -cD output1 --ccss --cx assets/example-1.svg',shell=True)
# subprocess.Popen('./svg-sprite/bin/svg-sprite.js -cD output1 --ccss --cx assets/example-2.svg assets/example-1.svg',shell=True)



def svg(input):
    outputDir = os.path.join('.','output',time.ctime())
    mode = getMode(config.mode)
    svgOutputDir = os.path.join(outputDir, 'svg')
    packsvg(input, mode,output=svgOutputDir)
    exportsvg(svgOutputDir, 'png', outputDir=os.path.join(outputDir, 'png'))

	
	
def getMode(mode):
	modelist = []
	for (id,value) in mode.items():
		if value != '' and value != 'false':
			if value == 'true':
				modelist.append(id)
			else:
				str = id + '=' +value
				modelist.append(str)
	return modelist



def packsvg(input, mode, output):

	cli = os.path.join('.', 'svg-sprite', 'bin', 'svg-sprite.js')
	output = '--dest=' + output
	if type(mode) != list:
		mode = mode.split(' ')
	files = []

	if type(input) == list:
		for svgfile in input:
			if svgfile.endswith('.svg'):
				if os.path.exists(svgfile):
					files.append(svgfile)
		print 'list'

	elif os.path.isfile(input):
		if input.endswith('.svg'):
			files.append(input)
			print 'svgfile'

	elif os.path.isdir(input):
		files.append(os.path.join(input, r'*.svg'))
		print 'dir'
	
	else:
		raise SvgException('no such file!')

	cmd = []
	cmd.append(cli)
	cmd.extend(mode)
	cmd.append(output)
	cmd.extend(files)
	print cmd
	subprocess.call(cmd)

class SvgException(Exception):
	def __init__(self,details):
		self.details = details




def exportsvg(inputDir, exportType, outputDir):
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)
    num = 0
    for a,f,c in os.walk(inputDir):
        for fileName in c:
            path = os.path.join(a, fileName)
            if os.path.isfile(path) and fileName.endswith('.svg'):
                num += 1
                fileHandle = open(path)
                svg = fileHandle.read()
                fileHandle.close()
                exportPath = os.path.join(outputDir, fileName[:-3] + exportType)
                exportFileHandle = open(exportPath, 'w')

                if exportType == "png":
                    try:
                        cairosvg.svg2png(bytestring=svg, write_to=exportPath)
                    except:
                        print "error in convert svg file : %s to png."%(path)

                elif exportType == "pdf":
                    try:
                        cairosvg.svg2pdf(bytestring=svg, write_to=exportPath)
                    except:
                        print "error in convert svg file: %s to pdf."%(path)

                exportFileHandle.close()
                print "Success Export ", exportType, " -> ", exportPath

    print num, " files are tranformed from svg to ", exportType
