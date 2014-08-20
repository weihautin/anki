#!/bin/bash
#
# update translation
#

if [ ! -d "libanki" ]
then
    echo "Please run this from the anki-i18n project root directory"
    exit
fi

if [ x$1 = x ]
then
    echo "Please pass the language code (eg, 'sv')"
    exit
fi

msgmerge -s --no-wrap libanki/$1.po libanki/libanki.pot > $1.new && mv $1.new libanki/$1.po
msgmerge -s --no-wrap ankiqt/$1.po ankiqt/ankiqt.pot > $1.new && mv $1.new ankiqt/$1.po
