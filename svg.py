#python2.7
import subprocess
import os
import cairosvg


# for test
# subprocess.Popen('./svg-sprite/bin/svg-sprite.js -cD out --ccss --cx assets/*.svg',shell=True)
# subprocess.Popen('./svg-sprite/bin/svg-sprite.js -cD out1 --ccss --cx assets/example-1.svg',shell=True)
# subprocess.Popen('./svg-sprite/bin/svg-sprite.js -cD out1 --ccss --cx assets/example-2.svg assets/example-1.svg',shell=True)


def svg(arg, out, mode):

	cli = './svg-sprite/bin/svg-sprite.js'
	out = '--dest=' + out
	mode = mode.split(' ')
	files = []

	if type(arg) == list:
		for svgfile in arg:
			if svgfile.endswith('.svg'):
				if os.path.exists(svgfile):
					files.append(svgfile)
		print 'list'

	elif os.path.isfile(arg):
		if arg.endswith('.svg'):
			files.append(arg)
			print 'svgfile'

	elif os.path.isdir(arg):
		files.append(os.path.join(arg, r'*.svg'))
		print 'dir'
	
	else:
		raise SvgException('no such file!')

	cmd = []
	cmd.append(cli)
	cmd.extend(mode)
	cmd.append(out)
	cmd.extend(files)
	print cmd
	subprocess.call(cmd)

class SvgException(Exception):
	def __init__(self,details):
		self.details = details




def exportsvg(fromDir, targetDir, exportType):
    num = 0
    for a,f,c in os.walk(fromDir):
        for fileName in c:
            path = os.path.join(a, fileName)
            if os.path.isfile(path) and fileName.endswith('.svg'):
                num += 1
                fileHandle = open(path)
                svg = fileHandle.read()
                fileHandle.close()
                exportPath = os.path.join(targetDir, fileName[:-3] + exportType)
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
