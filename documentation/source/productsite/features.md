
Alkalami is a TrueType font with smart font capabilities added using the OpenType font technology. The Alkalami font includes a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The sections below enumerates the details of these features. Whether these features are available to users will depend on both the application and the rendering technology being used. Features are available in OpenType. Some applications let the user control certain features such as Stylistic Sets to turn on the rendering of variant characters. However, at this point, many applications do not make use of those features so another solution is needed to show the variant characters. For applications that do not make use of the OpenType Character Variants, you can now download fonts customized with the variant glyphs you choose. Read this document, visit [TypeTuner Web](https://scripts.sil.org/ttw/fonts2go.cgi), then choose the variants and download your font. 

See [Using Font Features](https://software.sil.org/fonts/features/). Although that page is not targeted at Arabic script support, it does provide a comprehensive list of applications that make full use of the OpenType (and Graphite) font technologies.

See also [Arabic Fonts — Application Support](https://software.sil.org/arabicfonts/support/application-support/). It provides a fairly comprehensive list of applications that make full use of the OpenType font technology.

This page uses web fonts (WOFF) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Alkalami as a web font see *Alkalami-webfont-example.html* in the font package web folder. 

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Complete feature list

### Language system tags

<span class='affects'>Affects: U+065C, U+0627 (with U+064E, U+064F, U+0650), U+063F, U+069F, U+0751, U+0763, U+08C3, U+08C4</span>

Unfortunately, the UI needed to access the language-specific behavior is not yet present in many applications. Some Harfbuzz-based apps, e.g., XeTeX, can access language-specific behavior.

<!-- ha does not work for pdf. Must use hau for proper display in pdf. However, for proper display in html must use ha! -->

Language | Imala e | Touching | Wagaf | Feature setting
---      | -       | ---      | --    | ----
default | <span dir="rtl" class='alkalami-R normal'>&#x0628;&#x065C;</span> | <span dir="rtl" class='alkalami-R normal' >&#x0627;&#x064E; &#x0627;&#x064F; &#x0627;&#x0650; &#x0628;&#x0627;&#x064E; &#x0628;&#x0627;&#x064F; &#x0628;&#x0627;&#x0650; </span> | <span dir="rtl" class='alkalami-R normal'>&#x063F; &#x063F;&#x063F;&#x063F; &#x069F; &#x069F;&#x069F;&#x069F; &#x0751; &#x0751;&#x0751;&#x0751; &#x0763; &#x0763;&#x0763;&#x0763; &#x08C3; &#x08C3;&#x08C3;&#x08C3; &#x08C4; &#x08C4;&#x08C4;&#x08C4;</span> | |
Hausa |  <span dir="rtl" class='alkalami-R normal' lang='ha'>&#x0628;&#x065C;</span> | <span dir="rtl" class='alkalami-R normal' lang='ha'>&#x0627;&#x064E; &#x0627;&#x064F; &#x0627;&#x0650; &#x0628;&#x0627;&#x064E; &#x0628;&#x0627;&#x064F; &#x0628;&#x0627;&#x0650; </span>| <span dir="rtl" class='alkalami-R normal' lang='ha'>&#x063F; &#x063F;&#x063F;&#x063F; &#x069F; &#x069F;&#x069F;&#x069F; &#x0751; &#x0751;&#x0751;&#x0751; &#x0763; &#x0763;&#x0763;&#x0763; &#x08C3; &#x08C3;&#x08C3;&#x08C3; &#x08C4; &#x08C4;&#x08C4;&#x08C4;</span> | `lang=ha`

### Stylistic Sets

There are some character shape differences in different languages which use the Arabic script. These can be accessed by using the OpenType Stylistic Sets, or through the language support mentioned above.

#### Imala e (ss04)

<span class='affects'>Affects: U+065C</span>

Feature | Sample | Feature setting
------------- | ------ | -------------
Standard | <span dir="rtl" class='alkalami-ss04-0-R normal'>بٜ</span>| `ss04=0`
Small | <span dir="rtl" class='alkalami-ss04-1-R normal'>بٜ</span>| `ss04=1`

#### Jeem/Hah (ss07)

<span class='affects'>Affects: U+062C, U+062D, U+062E, U+0683, U+0684, U+08A2</span>

Feature | Sample | Feature setting
------------- | ------ | -------------
Standard | <span dir="rtl" class='alkalami-ss07-0-R normal'>ج ججج ح ححح خ خخخ ڃ ڃڃڃ ڄ ڄڄڄ ࢢ ࢢࢢࢢ</span>| `ss07=0`
Flat style | <span dir="rtl" class='alkalami-ss07-1-R normal'>ج ججج ح ححح خ خخخ ڃ ڃڃڃ ڄ ڄڄڄ ࢢ ࢢࢢࢢ</span>| `ss07=1`

#### Alef diacritic placement (ss08)

<span class='affects'>Affects: U+0627, U+064E, U+064F, U+0650</span>

Feature | Sample | Feature setting
------------- | ------ | -------------
Standard | <span dir="rtl" class='alkalami-ss08-0-R normal'>&#x0627;&#x064E; &#x0627;&#x064F; &#x0627;&#x0650; &#x0628;&#x0627;&#x064E; &#x0628;&#x0627;&#x064F; &#x0628;&#x0627;&#x0650; </span>| `ss08=0`
Touching | <span dir="rtl" class='alkalami-ss08-1-R normal'>&#x0627;&#x064E; &#x0627;&#x064F; &#x0627;&#x0650; &#x0628;&#x0627;&#x064E; &#x0628;&#x0627;&#x064F; &#x0628;&#x0627;&#x0650;</span>| `ss08=1`

#### Wagaf (ss09)

<span class='affects'>Affects: U+063F, U+069F, U+0751, U+0763, U+08C3, U+08C4</span>

Feature value | Sample | Feature setting
------------- | ---------------: | -------------
Standard | <span dir="rtl" class='alkalami-ss09-0-R normal'>&#x063F; &#x063F;&#x063F;&#x063F; &#x069F; &#x069F;&#x069F;&#x069F; &#x0751; &#x0751;&#x0751;&#x0751; &#x0763; &#x0763;&#x0763;&#x0763; &#x08C3; &#x08C3;&#x08C3;&#x08C3; &#x08C4; &#x08C4;&#x08C4;&#x08C4;</span>| `ss09=0`
Small | <span dir="rtl" class='alkalami-ss09-1-R normal'>&#x063F; &#x063F;&#x063F;&#x063F; &#x069F; &#x069F;&#x069F;&#x069F; &#x0751; &#x0751;&#x0751;&#x0751; &#x0763; &#x0763;&#x0763;&#x0763; &#x08C3; &#x08C3;&#x08C3;&#x08C3; &#x08C4; &#x08C4;&#x08C4;&#x08C4;</span>| `ss09=1`

#### End of ayah 

<span class='affects'>Affects: U+06DD</span>

These alternates are also available using the Stylistic Alternates (salt) feature, but at this time we know of no OpenType-based applications that can access these. 

Firefox allows you to use U+06DD followed by the digits and proper rendering occurs. Some applications require the following:

* precede the entire sequence (subtending mark plus following digits) with 202D LEFT-TO-RIGHT OVERRIDE
* follow the entire sequence with U+202C POP DIRECTIONAL FORMATTING.

Surrounding the sequence with U+202D and U+202C seems to give the most reliable results in different browsers. However, we have not found a solution that works in Internet Explorer/Edge.

In the example below, the following codepoints are used: U+202D U+06DD U+0031 U+0032 U+0033 U+202C U+202D U+06DD U+0611 U+0622 U+0663 U+202C.

Feature | Sample | Feature setting
------------- | ------ | ------------- 
Standard     | <span class='alkalami-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span> | `ss02=0` `ss03=0`
End of ayah A | <span class='alkalami-ss02-1-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `ss02=1`
End of ayah B | <span class='alkalami-ss03-1-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `ss03=1`

### Other user font features

#### Proportional Figures

Alkalami supports the OpenType **Proportional Figures (pnum)** for Latin digits. *This feature is not supported in TypeTuner Web.*

<span class='affects'>Affects: U+0030..U+0039</span>

Feature | Sample | Feature setting
------------- | ------ | ------------- 
Tabular Figures      | <span dir="rtl" class='alkalami-R normal'> 0 1 2 3 4 5 6 7 8 9</span>| `pnum=0`
Proportional Figures     | <span dir="rtl" class='alkalami-pnum-1-R normal'> 0 1 2 3 4 5 6 7 8 9</span>| `pnum=1`

#### Contextual Alternates

Alkalami has a few contextual rules applying subtle differences in the shape and position of certain of the characters depending on context (sometimes shortening, sometimes lengthening or lowering a “tail”). InDesign is able to utilize some of these cross word contextual alternates; however, most applications are not advanced enough to use this behavior in the font. Unfortunately, at this point in the development of the font, combining marks above or below may break these contextual alternates.

**Substitutions to avoid collisions in strings with noon-like characters**

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0646;&#x0020;&#x062a;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x0646;&#x0020;&#x0628;</span>

**Substitutions to avoid collisions in strings with yeh-like characters**

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0628;&#x064a;&#x0020;&#x0644;&#x0631;&#x0020;&#x0628;&#x064a;</span>

**Substitutions to avoid collisions in strings with seen-like characters**

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0633;&#x0020;&#x0633;&#x0648;&#x0020;&#x0633;</span>

**Substitutions for shortening dal-like characters (shorter tail on dal)**

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0633;&#x0020;&#x062f;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x062f;</span>

**Substitutions for shortening waw-like characters**

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0628;&#x0646;&#x0020;&#x0648;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x0648;</span>

## Note!

If you used previous versions of this font, we made some decisions which were unfortunately not Unicode compliant. Since the initial release of this font, many of these non Unicode compliant characters have been added to Unicode. You will need to re-encode some characters to be fully Unicode compliant. The characters affected are listed below:

 Glyph | Non Unicode Compliant | → | Glyph | Convert to
 - | ---------- | -: | -- | ---------- 
<span dir="rtl" class='alkalami-R normal'>&#x0643;</span>| 0643 ARABIC LETTER KAF | → | <span dir="rtl" class='alkalami-R normal'>&#x06a9; &#x06a9;&#x06a9;&#x06a9;</span>| 06A9 ARABIC LETTER KEHEH 
<span dir="rtl" class='alkalami-R normal'>&#x06ad;</span>| 06AD ARABIC LETTER NG  | → | <span dir="rtl" class='alkalami-R normal'>&#x0763; &#x0763;&#x0763;&#x0763;</span>| 0763 ARABIC LETTER KEHEH WITH THREE DOTS ABOVE
<span dir="rtl" class='alkalami-R normal'>&#x067b;</span>| 067B ARABIC LETTER BEEH (ss05) | → | <span dir="rtl" class='alkalami-R normal'>&#x0751; &#x0751;&#x0751;&#x0751;</span>| 0751 ARABIC LETTER BEH WITH DOT BELOW AND THREE DOTS ABOVE (use Stylistic Set `ss09` if you wish a small *wagaf*)
<span dir="rtl" class='alkalami-R normal'>&#x069f;</span>| 069F ARABIC LETTER TAH WITH THREE DOTS ABOVE (ss05) | → | | You may continue to use this codepoint (use Stylistic Set `ss09` if you wish a small *wagaf*)
<span dir="rtl" class='alkalami-R normal'>&#x06a0;</span>| 06A0 ARABIC LETTER AIN WITH THREE DOTS ABOVE (ss05) | → | <span dir="rtl" class='alkalami-R normal'>&#x08c3; &#x08c3;&#x08c3;&#x08c3;</span>| 08C3 ARABIC LETTER GHAIN WITH THREE DOTS ABOVE (use Stylistic Set `ss09` if you wish a small *wagaf*)
<span dir="rtl" class='alkalami-R normal'>&#x06a8;</span>| 06A8 ARABIC LETTER QAF WITH THREE DOTS ABOVE (ss05) | → | <span dir="rtl" class='alkalami-R normal'>&#x08c4; &#x08c4;&#x08c4;&#x08c4;</span>| 08C4 ARABIC LETTER AFRICAN QAF WITH THREE DOTS ABOVE (use Stylistic Set `ss09` if you wish a small *wagaf*)
<span dir="rtl" class='alkalami-R normal'>&#x06cc;</span>| 06CC ARABIC LETTER FARSI YEH (ss05) | → | <span dir="rtl" class='alkalami-R normal'>&#x063f; &#x063f;&#x063f;&#x063f;</span>| 063F ARABIC LETTER FARSI YEH WITH THREE DOTS ABOVE (use Stylistic Set `ss09` if you wish a small *wagaf*)
<span dir="rtl" class='alkalami-R normal'>&#x0763;</span>| 0763 ARABIC LETTER KEHEH WITH THREE DOTS ABOVE (ss05) | → | | You may continue to use this codepoint (use Stylistic Set `ss09` if you wish a small *wagaf*)
<span dir="rtl" class='alkalami-R normal'>&#x0646;</span>| 0646 ARABIC LETTER NOON (ss01) | → | <span dir="rtl" class='alkalami-R normal'>&#x08bd; &#x08bd;&#x08bd;&#x08bd;</span>| 08BD ARABIC LETTER AFRICAN NOON (no Stylistic Set required)
<span dir="rtl" class='alkalami-R normal'>&#x064a;</span>| 064A ARABIC LETTER YEH (ss01) | → | <span dir="rtl" class='alkalami-R normal'>&#x06cc; &#x06cc;&#x06cc;&#x06cc;</span>| 06CC ARABIC LETTER FARSI YEH (no Stylistic Set required)
<span dir="rtl" class='alkalami-R normal'>&#x06a2;</span>| 06A2 ARABIC LETTER FEH WITH DOT MOVED BELOW (ss01) | → | <span dir="rtl" class='alkalami-R normal'>&#x08bb; &#x08bb;&#x08bb;&#x08bb;</span>| 08BB ARABIC LETTER AFRICAN FEH (no Stylistic Set required)
<span dir="rtl" class='alkalami-R normal'>&#x06a7;</span>| 06A7 ARABIC LETTER QAF WITH DOT ABOVE (ss01) | → | <span dir="rtl" class='alkalami-R normal'>&#x08bc; &#x08bc;&#x08bc;&#x08bc;</span>| 08BC ARABIC LETTER AFRICAN QAF (no Stylistic Set required)

[font id='alkalami' face='Alkalami-Regular' size='150%' rtl=1]
[font id='alkalamiL' face='Alkalami-Regular' size='100%' ltr=1]



[font id='alkalami-ss04-0' face='Alkalami-Regular' size='150%' rtl=1 feats='ss04 0']
[font id='alkalami-ss04-1' face='Alkalami-Regular' size='150%' rtl=1 feats='ss04 1']
[font id='alkalami-ss07-0' face='Alkalami-Regular' size='150%' rtl=1 feats='ss07 0']
[font id='alkalami-ss07-1' face='Alkalami-Regular' size='150%' rtl=1 feats='ss07 1']
[font id='alkalami-ss08-0' face='Alkalami-Regular' size='150%' rtl=1 feats='ss08 0']
[font id='alkalami-ss08-1' face='Alkalami-Regular' size='150%' rtl=1 feats='ss08 1']
[font id='alkalami-ss09-0' face='Alkalami-Regular' size='150%' rtl=1 feats='ss09 0']
[font id='alkalami-ss09-1' face='Alkalami-Regular' size='150%' rtl=1 feats='ss09 1']
[font id='alkalami-ss02-1' face='Alkalami-Regular' size='150%' rtl=1 feats='ss02 1']
[font id='alkalami-ss03-1' face='Alkalami-Regular' size='150%' rtl=1 feats='ss03 1']
[font id='alkalami-pnum-1' face='Alkalami-Regular' size='150%' rtl=1 feats='pnum 1']
