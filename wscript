#! /usr/bin/python3
# this is a smith configuration file

# set the default output folders
DOCDIR = ['documentation', 'web']
generated = 'generated/'

# set package name
APPNAME = "Alkalami"

# set the font family name
FAMILY = APPNAME

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Regular' + '.ufo')

# set up FTML tests
ftmlTest('tools/ftml-smith.xsl')

# APs to omit:
OMITAPS = '--omitaps "topright, ogonek, caret_1, caret_2, caret_3, top_3, top_4, top_alef"'

typetunerfile = 'source/typetuner/feat_all.xml'

designspace('source/Alkalami.designspace',
    instanceparams='-l ' + generated + '{$FAMILY}_createinstances.log',
    target = process('${DS:FILENAME_BASE}.ttf',
        cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']),
#        Note: ttfautohint-generated hints don't maintain stroke thickness at joins (nor hamza), so we're not hinting these fonts
#        cmd('${TTFAUTOHINT} -n -c  -D arab -W ${DEP} ${TGT}')
    ),
    version = VERSION,  # Needed to ensure dev information on version string
    ap = generated + '${DS:FILENAME_BASE}.xml',
    opentype = fea('generated/${DS:FILENAME_BASE}.fea',
        mapfile = 'generated/${DS:FILENAME_BASE}.map',
        master = 'source/opentype/main.feax',
        make_params = OMITAPS
    ),
    script = ['arab'],
    pdf = fret(params='-m 25 -r -oi'),
    woff = woff('web/${DS:FILENAME_BASE}',
        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
        ),
    typetuner = typetuner(typetunerfile),
)


def configure(ctx):
    ctx.find_program('ttfautohint')
