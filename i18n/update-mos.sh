#!/bin/bash
#
# build mo files
#

if [ ! -d "anki" ]
then
    echo "Please run this from the anki-i18n project root directory"
    exit
fi

echo "Updating *.po..."
for file in anki/*.po
do
    outdir=$(echo $file | \
        perl -pe 's%.*/(.*)\.po%../dtop/locale/\1/LC_MESSAGES%')
    outfile="$outdir/anki.mo"
    mkdir -p $outdir
    msgfmt $file --output-file=$outfile
done
