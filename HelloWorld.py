import sublime, sublime_plugin
import time

class HelloWorldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		localtime = time.asctime( time.localtime(time.time()) )
		Detect = self.view.text_point(1, 0)
		tx = self.view.substr(self.view.line(Detect))
		if tx == "**Author  : caoqing":
			replace = self.view.line(self.view.text_point(3, 0))
			self.view.replace(edit, replace, "**Update time : " + localtime)
		else:
			self.view.insert(edit, 0, "/**********************************************************\n"\
				+"**Author  : caoqing\n"\
				+"**version : 1.0\n"\
				+"**Update time : " + localtime + "\n"\
				+"**********************************************************/\n")
