#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
try:
    import pyperclip
except:
    print "*** ATTENTION *** : Installer pyperclip"
    exit(0)

PREFIX = "http://action.metaffiliation.com/trk.php?mclic=P4572B52EEE1191&redir="

input_url = raw_input("URL irun : ")
if not "i-run.fr" in input_url:
    print "*** ATTENTION *** : URL invalide"
else:
    generated_link = "%s%s" % (PREFIX, urllib.quote_plus(input_url))
    print "\nLien copié dans le presse-papier :"
    print "%s" % generated_link
    pyperclip.copy(generated_link)
