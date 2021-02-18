# kamer/version.py
#
#

""" version plugin. """

from kamer import __version__

txt = "using the law to administer poison the king commits genocide"

def ver(event):
    event.reply("KAMER #%s - %s" % (__version__, txt))
