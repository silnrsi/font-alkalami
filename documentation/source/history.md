---
title: Alkalami - Version History
fontversion: 1.300
---

### 2022-04-27 (WSTech team) Alkalami Version 1.300 (production release)
- Added characters to support other languages: U+0600, U+0657..U+0658, U+065D, U+067D, U+0684, U+06A5, U+06E5, U+0761, U+0870, U+0872, U+0874, U+08A2..U+08A3, U+08F4..U+08FD, U+FDFD, U+2212
- Changed design of U+0643 (KAF) and U+06AD (NG)
- Added ss09 to support "Wagaf small"
- Added more contextual substitutions of swash tails for collision avoidance
- Fixed bug in outline of U+0624 (Regular)
- Added positional digit variants for Latin digits

### 2020-01-31 (Sharon Correll) Alkalami Version 1.200 (production release)
- Added many characters required for codepage 1252 and macRoman
- Deleted many Latin characters not required for codepage 1252 and macRoman
- Added Arabic script characters: U+063F, U+0751, U+08C3 (pipelined for Unicode 13.0), U+08C4 (pipelined for Unicode 13.0)
- Added UI name strings for OpenType features
- Repositioned below attachment points on qaf-based isolate and final forms
- Changed ss07 hah medial and final forms to match jeem medial and final forms (Light only)
- Changed ss05 (Wagaf Hack) version of U+06A0 to include single large nukta (bug in previous version of the font)
- Added mirrored versions of some glyphs such as radical and summation
- Increased right side-bearing for Light version of U+0623 

### 2018-07-11 (Becca Spalinger) Alkalami 1.100
- Changed qaf-based characters: isolate now has tail; tail on final flattened to match isolate

### 2017-05-23 (Becca Spalinger) Alkalami 1.000
- Fixed issues related to lam/alef/hamza shaping
- Fixed issue with jeem/hah combinations not shaping properly
- Added larger left sidebearing on U+0622 (isolate and final forms)
- Repositioned below attachment points on isolate and final forms of noon, lam, seen, sad, qaf and yeh
- Added Stylistic set (ss08) to make fatha, kasra and damma touch the isolate alef
- Decomposed U+0623 and U+0625 in order to allow the hamza part of the character to be colored
- Changed position of dagger alef when with fatha

### 2016-12-15 (Becca Spalinger) Alkalami 0.924
- Repositioned below attachment points on reh and waw
- Changed depth of swash on the sad/dad, seen/sheen, and lam isolate
- Digits reduced in size
- Width of U+0640 reduced by 50%
- Left sidebearing on U+0621 reduced
- Changed positioning of dagger alef above fatha and alef maksura

### 2016-10-06 (Becca Spalinger) Alkalami 0.919
- Updated OpenType code to handle hah/jeem/khah/nyeh positioning

### 2016-04-04 (Becca Hirsbrunner Spalinger) Alkalami 0.910
- Added anchor points to U+FDF2
- Removed U+064A to ss05 and added U+06CC to ss05 with wagaf above

### 2016-02-04 (Becca Hirsbrunner Spalinger) Alkalami 0.909
- Fixed medial alternate form of peh

### 2016-01-12 (Becca Hirsbrunner Spalinger) Alkalami 0.908
- Fixed OpenType code for "Allah"

### 2015-12-11 (Becca Hirsbrunner Spalinger) Alkalami 0.906 Preliminary design and smart behaviours
- Smart behaviours for wagaf and Warsh implemented in OpenType
- TypeTuner code added to support features
- Space character changed to be bigger for use Latin script and smaller for Arabic script

### 2015-11-05 (Becca Hirsbrunner Spalinger) Alkalami 0.1-alpha Preliminary design and smart behaviours
- Preliminary design of isolate characters
- Smart behaviours implemented in OpenType

