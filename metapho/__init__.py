#!/usr/bin/env python

# metapho: an image tagger and viewer.

# Copyright 2013,2016 by Akkana Peck: share and enjoy under the GPL v2 or later.

'''metapho: an image tagger and viewer.'''

__version__ = "0.5.1"
__author__ = "Akkana Peck <akkana@shallowsky.com>"
__license__ = "GPL v2+"
__all__ = [ 'Image', 'Tagger', 'Organizer' ]

from metapho import *

# Don't import gtkpho automatically; let users choose whether to do that.

