#!/bin/bash
FILES=$@
if [ -z $FILES ]
then
   DEB=`echo *.deb`
   CHANGES=`echo *.changes`
   UDEB=`echo *.udeb`
   FILES=""
   echo "DEB: $DEB"
   echo "CHANGES: $CHANGES"
   echo "UDEB: $UDEB"
   echo
   [ "$DEB"     != "*.deb"     ] && FILES="$FILES $DEB"
   [ "$CHANGES" != "*.changes" ] && FILES="$FILES $CHANGES"
   [ "$UDEB"    != "*.udeb"    ] && FILES="$FILES $UDEB"
fi

if [ "n" != "n$FILES" ]
then
   echo "Uploading $FILES."
   cp -rf $FILES /var/packages/pr2-dev/ubuntu/queue/precise/ && \
      reprepro -V -b /var/packages/pr2-dev/ubuntu processincoming precise && \
      mv -i $FILES old/
else
   echo "Nothing to upload"
fi
