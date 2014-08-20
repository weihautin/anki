#!/bin/bash
#
# update POs from launchpad export
#

if [ x$1 = x ]
then
    echo "Please pass the path to the export file"
    exit
fi

if [ ! -d "libanki" ]
then
    echo "Please run this from the anki-i18n project root directory"
    exit
fi

rm libanki/*.po
rm ankiqt/*.po
tar xzf $1
cd libanki
rename 's/libanki-//' *
cd ../ankiqt
rename 's/ankiqt-//' *
cd ..
bzr st
