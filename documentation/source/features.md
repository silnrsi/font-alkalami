---
title: Alkalami - Font Features
fontversion: 1.300
---

Alkalami is a TrueType font with smart font capabilities added using the OpenType font technology. The Alkalami font includes a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The sections below enumerates the details of these features. Whether these features are available to users will depend on both the application and the rendering technology being used. Features are available in OpenType. Some applications let the user control certain features such as Stylistic Sets to turn on the rendering of variant characters. However, at this point, many applications do not make use of those features so another solution is needed to show the variant characters. [TypeTuner](http://scripts.sil.org/ttw/fonts2go.cgi) creates tuned fonts that use the variant glyph in place of the standard glyph. 

See [Using Font Features](https://software.sil.org/fonts/features/). Although that page is not targeted at Arabic script support, it does provide a comprehensive list of applications that make full use of the OpenType (and Graphite) font technologies.

See also [Arabic Fonts — Application Support](http://software.sil.org/arabicfonts/support/application-support/). It provides a fairly comprehensive list of applications that make full use of the OpenType font technology.

This page uses web fonts (WOFF) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Alkalami as a web font see *Alkalami-webfont-example.html* in the font package web folder. 

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Signs Spanning Numbers

These signs spanning numbers are intended to enclose or hold one or more digits. Specific technical details of how to use them are discussed in the [Arabic fonts FAQ -- Subtending marks](http://software.sil.org/arabicfonts/support/faq#Ayah).

Currently, this font only supports the **Number Sign** (U+0600) and **End of Ayah** (U+06DD). Additionally, Alkalami includes two simplified alternates for U+06DD ARABIC END OF AYAH under the Stylistic Alternates (salt) feature, but at this time we know of no OpenType-based applications that can access these. The two alternates are also available through the Stylistic Sets feature discussed below.

## Customizing with TypeTuner

For applications that do not make use of the OpenType Stylistic Sets, you can now download fonts customized with the variant glyphs you choose. Read this document, visit [TypeTuner Web](http://scripts.sil.org/ttw/fonts2go.cgi), then choose the variants and download your font.

### Stylistic Sets

There are some character shape differences in different languages which use the Arabic script. These can be accessed by using the OpenType Stylistic Sets mentioned above.  


#### Imala e (ss04)

<span class='affects'>Affects: U+065C</span>

Feature | Sample | Feature setting
------------- | ------ | -------------
Standard | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss04" 0'>بٜ</span>| `ss04=0`
Alternate | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss04" 1'>بٜ</span>| `ss04=1`

#### Jeem/Hah stacking (ss07)

<span class='affects'>Affects: U+062C, U+062D, U+062E, U+0683, U+0684, U+08A2</span>

Feature | Sample | Feature setting
------------- | ------ | -------------
Standard | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss07" 0'>ج ججج ح ححح خ خخخ ڃ ڃڃڃ ڄ ڄڄڄ ࢢ ࢢࢢࢢ</span>| `ss07=0`
Alternate | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss07" 1'>ج ججج ح ححح خ خخخ ڃ ڃڃڃ ڄ ڄڄڄ ࢢ ࢢࢢࢢ</span>| `ss07=1`

#### Alef diacritic placement (ss08)

<span class='affects'>Affects: U+0627, U+064E, U+064F, U+0650</span>

Feature | Sample | Feature setting
------------- | ------ | -------------
Standard | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss08" 0'>&#x0627;&#x064E; &#x0627;&#x064F; &#x0627;&#x0650; &#x0628;&#x0627;&#x064E; &#x0628;&#x0627;&#x064F; &#x0628;&#x0627;&#x0650; </span>| `ss08=0`
Touching | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss08" 1'>&#x0627;&#x064E; &#x0627;&#x064F; &#x0627;&#x0650; &#x0628;&#x0627;&#x064E; &#x0628;&#x0627;&#x064F; &#x0628;&#x0627;&#x0650;</span>| `ss08=1`


#### Wagaf small (ss09)

<span class='affects'>Affects: U+063F, U+069F, U+0751, U+0763, U+08C3, U+08C4</span>

Feature value | Sample | Feature setting
------------- | ---------------: | -------------
Standard | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss09" 0'>&#x063F; &#x063F;&#x063F;&#x063F; &#x069F; &#x069F;&#x069F;&#x069F; &#x0751; &#x0751;&#x0751;&#x0751; &#x0763; &#x0763;&#x0763;&#x0763; &#x08C3; &#x08C3;&#x08C3;&#x08C3; &#x08C4; &#x08C4;&#x08C4;&#x08C4;</span>| `ss09=0`
Alternate | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss09" 1'>&#x063F; &#x063F;&#x063F;&#x063F; &#x069F; &#x069F;&#x069F;&#x069F; &#x0751; &#x0751;&#x0751;&#x0751; &#x0763; &#x0763;&#x0763;&#x0763; &#x08C3; &#x08C3;&#x08C3;&#x08C3; &#x08C4; &#x08C4;&#x08C4;&#x08C4;</span>| `ss09=1`

#### End of ayah 

<span class='affects'>Affects: U+06DD</span>

Firefox allows you to use U+06DD followed by the digits and proper rendering occurs. Some applications require the following:

* precede the entire sequence (subtending mark plus following digits) with 202D LEFT-TO-RIGHT OVERRIDE
* follow the entire sequence with U+202C POP DIRECTIONAL FORMATTING.

Surrounding the sequence with U+202D and U+202C seems to give the most reliable results in different browsers. However, we have not found a solution that works in Internet Explorer/Edge.

In the example below, the following codepoints are used: U+202D U+06DD U+0031 U+0032 U+0033 U+202C U+202D U+06DD U+0611 U+0622 U+0663 U+202C.

Feature | Sample | Feature setting
------------- | ------ | ------------- 
Standard     | <span dir="rtl" class='alkalami-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span> | `ss02=0` `ss03=0`
Simplified A | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss02" 1'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `ss02=1`
Simplified B | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss03" 2'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `ss03=1`


### Discouraged

These are discouraged from use. They were added to the font before some of the characters were added to Unicode. The characters supported in ss09 are Unicode-compliant.

#### Warsh Hack (ss01)

<span class='affects'>Affects: U+0646, U+064A, U+06A2, U+06A7</span>

Feature | Sample | Feature setting
------------- | ------ | ------------- 
Standard      | <span dir="rtl" class='alkalami-R normal'>ن ننن      ي ييي      ڢ ڢڢڢ      ڧ ڧڧڧ </span>| `ss01=0`
Alternate     | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss01" 1'>ن ننن      ي ييي      ڢ ڢڢڢ      ڧ ڧڧڧ </span>| `ss01=1`

#### Wagaf Hack (ss05)

<span class='affects'>Affects: U+06CC, U+067B, U+069F, U+06A0, U+06A8, U+0763</span>

Feature | Sample | Feature setting
------------- | ------ | ------------- 
Standard      | <span dir="rtl" class='alkalami-R normal'>ی ییی      ٻ ٻٻٻ      ڟ ڟڟڟ      ڠ ڠڠڠ      ڨ ڨڨڨ      ݣ ݣݣݣ </span>| `ss05=0`
Alternate     | <span dir="rtl" class='alkalami-R normal' style='font-feature-settings: "ss05" 1'>ی ییی      ٻ ٻٻٻ      ڟ ڟڟڟ      ڠ ڠڠڠ      ڨ ڨڨڨ      ݣ ݣݣݣ </span>| `ss05=1`

## Contextual Alternates

Alkalami has a few contextual rules applying subtle differences in the shape and position of certain of the characters depending on context (sometimes shortening, sometimes lengthening or lowering a “tail”). InDesign is able to utilize some of these cross word contextual alternates; however, most applications are not advanced enough to use this behavior in the font. Unfortunately, at this point in the development of the font, combining marks above or below may break these contextual alternates.

#### Substitutions to avoid collisions in strings with noon-like characters

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0646;&#x0020;&#x062a;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x0646;&#x0020;&#x0628;</span>

#### Substitutions to avoid collisions in strings with yeh-like characters

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0628;&#x064a;&#x0020;&#x0644;&#x0631;&#x0020;&#x0628;&#x064a;</span>

#### Substitutions to avoid collisions in strings with seen-like characters

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0633;&#x0020;&#x0633;&#x0648;&#x0020;&#x0633;</span>

#### Substitutions for shortening dal-like characters (shorter tail on dal)

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0633;&#x0020;&#x062f;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x062f;</span>

#### Substitutions for shortening waw-like characters

&#x00A0;&#x00A0;&#x00A0;&#x00A0;<span dir="rtl" class='alkalami-R normal'>&#x0628;&#x0646;&#x0020;&#x0648;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x00a0;&#x0648;</span>


   


<!-- PRODUCT SITE ONLY
[font id='alkalami' face='Alkalami-Regular' light='Alkalami-Light' size='150%' rtl=1]
[font id='alkalamiL' face='Alkalami-Regular' light='Alkalami-Light' size='100%' ltr=1]

-->


