#!/bin/sh

# This script rebuilds the algorithmically-generated ftml files. See README.md

# Copyright (c) 2020-2023 SIL International  (http://www.sil.org)
# Released under the MIT License (http://opensource.org/licenses/

# Assumes we're in the root folder, i.e., font-Alkalami

set -e

if [ ! -e OFL.txt ] 
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

echo "Rebuilding ftml files..."
tools/absgenftml.py -q -t 'AllChars (auto)'         source/masters/Alkalami-Regular.ufo  tests/AllChars-auto.ftml        -l tests/logs/AllChars-auto.log         -s 'local(Scheherazade New)|Sch (inst)' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 250 -i source/glyph_data.csv -s 'url(../references/Alkalami-Regular.ttf)|2.0' -s 'url(../results/Alkalami-Regular.ttf)|Reg'  &
tools/absgenftml.py -q -t 'AL Sorted (auto)'        source/masters/Alkalami-Regular.ufo  tests/ALsorted-auto.ftml        -l tests/logs/ALsorted-auto.log         -s 'local(Scheherazade New)|Sch (inst)' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 250 -i source/glyph_data.csv -s 'url(../references/Alkalami-Regular.ttf)|2.0' -s 'url(../results/Alkalami-Regular.ttf)|Reg'  &
tools/absgenftml.py -q -t 'DiacTest1 (auto)'        source/masters/Alkalami-Regular.ufo  tests/DiacTest1-auto.ftml       -l tests/logs/DiacTest1-auto.log        -s 'local(Scheherazade New)|Sch (inst)' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 250 -i source/glyph_data.csv -s 'url(../references/Alkalami-Regular.ttf)|2.0' -s 'url(../results/Alkalami-Regular.ttf)|Reg'  & 
tools/absgenftml.py -q -t 'DiacTest1 Short (auto)'  source/masters/Alkalami-Regular.ufo  tests/DiacTest1-short-auto.ftml -l tests/logs/DiacTest1-short-auto.log  -s 'local(Scheherazade New)|Sch (inst)' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 250 -i source/glyph_data.csv -s 'url(../references/Alkalami-Regular.ttf)|2.0' -s 'url(../results/Alkalami-Regular.ttf)|Reg'  &
tools/absgenftml.py -q -t 'Subtending Marks (auto)' source/masters/Alkalami-Regular.ufo  tests/SubtendingMarks-auto.ftml -l tests/logs/Subtending-auto.log       -s 'local(Scheherazade New)|Sch (inst)' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 250 -i source/glyph_data.csv -s 'url(../references/Alkalami-Regular.ttf)|2.0' -s 'url(../results/Alkalami-Regular.ttf)|Reg'  &
wait
echo done.
