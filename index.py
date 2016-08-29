from Naked.toolshed.shell import execute_js
def edit(*temp):
	success = execute_js('saveFile.js')
	print "sone"
	print success
	pass

edit()
