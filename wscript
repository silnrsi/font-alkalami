#!/usr/bin/python
# encoding: utf8

# Smith configuration file for Alkalami

# set the default output folders
DOCDIR = ["documentation", "web"]
STANDARDS = "tests/previous"

# set the product name
APPNAME = "Alkalami"

# set licensing and description

DESC_SHORT = "Font for Arabic-based writing systems in the Kano region."

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/masters/Alkalami-Regular.ufo')

#BUILDLABEL = 'beta'

# APs to omit:
OMITAPS = '--omitaps "topright, ogonek, caret_1, caret_2, caret_3, top_1, top_2, top_3, top_4, top_alef, bottom_1, bottom_2"'

# set the build and test parameters

# Notes about DS variables:
#   The phrase '${DS:NAME}' references the 'name' attribute from the instance as defined 
#   in the designspace file, i.e. either "Alkalami-Light" or "Alkalami-Regular" -- 
#   and we use that to construct all the filenames.
designspace('source/Alkalami.designspace',
    instanceparams = '-l generated/${DS:NAME}_createintance.log',
    target = process('${DS:NAME}.ttf',
        cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/masters/${DS:NAME}.ufo']),
#        Note: ttfautohint-generated hints don't maintain stroke thickness at joins (nor hamza), so we're not hinting these fonts
#        cmd('${TTFAUTOHINT} -n -c  -D arab -W ${DEP} ${TGT}')
    ),
    opentype = fea('generated/${DS:FILENAME_BASE}.fea',
        mapfile = 'generated/${DS:FILENAME_BASE}.map',
        master = 'source/opentype/master.feax',
        make_params = OMITAPS
    ),
    script = ['arab'],
    version = VERSION,
    fret = fret('generated/${DS:FILENAME_BASE}-fret.pdf', params='-r -oi'),
    woff = woff('web/${DS:NAME}.woff', params='-v '+VERSION +' -m ../source/${DS:FAMILYNAME_DASH}-WOFF-metadata.xml'),
    typetuner = typetuner("source/typetuner/feat_all.xml"),
)


#def configure(ctx):
#    ctx.find_program('ttfautohint')
