#! /bin/sh

dir=`dirname $0`
todoc=`ls -1 $dir | grep '\.html$'`

for doc in $todoc; do
    docdir=$dir/$doc
    docbase=$(basename $doc .html)
    # Update "in-file" anchor links, replace:
    # current-file.{cpp,html} -> documentation-example-current-file.html
    perl -ne "s/<a href=\"$docbase.(cpp|html)/<a href=\"documentation-example-$docbase.html/g;print" $docdir > $docdir.tmp
    cat documentation-module.header.tpl.html $docdir.tmp documentation-module.footer.tpl.html > documentation-example-$docbase.html
    rm $docdir.tmp
done
