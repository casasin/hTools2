# [h] copy side-bearings

'''Copy side-bearings in selected glyphs from one font to another.'''

# debug

import hTools2
reload(hTools2)

if hTools2.DEBUG:
    import hTools2.dialogs.glyphs
    reload(hTools2.dialogs.glyphs)

# import

from hTools2.dialogs.glyphs import copyMarginsDialog

# run

copyMarginsDialog()
