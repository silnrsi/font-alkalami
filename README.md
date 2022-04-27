# Alkalami

Alkalami is the local word for the Arabic "qalam", a type of sharpened stick used for writing on wooden boards in the Kano region of Nigeria and in Niger, and what gives the style its distinct appearance. The baseline stroke is very thick and solid. The ascenders and other vertical strokes including the teeth are very narrow when compared to the baseline. A generous line height is necessary to allow for deep swashes and descenders, and the overall look of the page is a very black, solid rectangle. Diacritics are much smaller in scale, with very little distance from the main letters.

## Project status [![Build Status](http://build.palaso.org/app/rest/builds/buildType:Fonts_Alkalami/statusIcon)](http://build.palaso.org/viewType.html?buildTypeId=Fonts_Alkalami&guest=1)

Alkalami v1.300 has been released. 

In a future version of Alkalami, we plan to split Alkalami Regular and Alkalami Light into two separate font families. Alkalami Regular will stay the same. Alkalami Light will become Ruwudu Regular. Future versions of this font will remove non Unicode compliant solutions. Font sources are published in a public repository. The build process requires [smith](https://github.com/silnrsi/smith) and project build parameters are set in the [wscript](wscript).    

## About ftml tests

After a successful build, the results/ folder will contain, along with the built ttf and woff fonts, a number of
test files in an xml-based format called FTML. Examples are AllChars-ng.xml, Diac-ng.xml. 
There is an ftml.xsl file that can be used to view these ftml documents directly in Firefox. 

However, in order for Firefox to access the .xsl file, you need to relax its "strict URI" policy by going to about:config and
setting [security.fileuri.strict_origin_policy](http://kb.mozillazine.org/Security.fileuri.strict_origin_policy) to false.

Once you have this setting in effect, you can load the FTML documents directly into Firefox and see the built font rendered.

## License

Alkalami is licensed under the SIL Open Font License. See [OFL.txt](OFL.txt) and [OFL-FAQ.txt](OFL-FAQ.txt) for details.

## See also

For more details about this project, including changelog and acknowledgements see [FONTLOG.txt](FONTLOG.txt).

For further information about this font, including Unicode ranges supported and OpenType font features and how to use them, and licensing, please see the documentation on [software.sil.org/alkalami](http://software.sil.org/alkalami/) or in the documentation/ subfolder.

# Developer notes

This project uses a UFO-based design and production workflow, with all sources in open formats and a completely open-source build toolkit. For more details see [SIL Font Development Notes](https://silnrsi.github.io/silfontdev/en-US/Introduction.html).

We welcome contributions to this font project, such as new glyphs, enhanced smart font code, or bug fixes. The best way to begin the process is to file an issue in the [Github project](https://github.com/silnrsi/font-alkalami) or respond to an existing issue and express your interest. Then we can begin to correspond with you regarding what all might be required and discuss how to best submit your contributions.

To enable us to accept contributions in a way that honors your contribution and respects your copyright while preserving long-term flexibility for open source licensing, you would also need to agree to the SIL International Contributor License Agreement for Font Software (v1.0) prior to sending us your contribution. To read more about this requirement and find out how to submit the required form, please visit the [CLA information page](https://software.sil.org/fontcla).
