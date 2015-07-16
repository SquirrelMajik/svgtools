__author__ = 'majik'

import svg
import svgtransformer


if __name__ == "__main__":
	# try:
	# 	svg.svg('assets', 'out1', '-c --ccss --cs')
	# 	svg.svg('assets/example-1.svg', 'out2', '-c --ccss --cs')
	# 	svg.svg(['assets/example-2.svg', 'assets/example-1.svg', 'assets/example-1.png'], 'out3', '-c --ccss --cs')
	# 	svg.svg('123', 'out4', '-c --ccss --cs')
	# except svg.SvgException as svgexception:
	# 	print svgexception.details
    svgtransformer.svgform('1.svg')