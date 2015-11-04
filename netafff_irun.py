#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib

PREFIX = "http://action.metaffiliation.com/trk.php?mclic=P4572B52EEE1191&redir="

input_url = raw_input("URL irun ?\n")

print "\n%s%s" % (PREFIX, urllib.quote_plus(input_url))
