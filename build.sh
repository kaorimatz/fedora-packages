#!/bin/bash
#
# usage: ./build.sh [<target-package>]

set -e

if [ $# -ge 1 ]; then
  TARGET_PACKAGE=$1
fi;

PROJECT_DIR=`cd \`dirname $0\` && pwd`

RPMBUILD_TOP_DIR=`rpm --eval '%{_topdir}'`
RPMBUILD_SPEC_DIR=$RPMBUILD_TOP_DIR/SPECS
RPMBUILD_SOURCE_DIR=$RPMBUILD_TOP_DIR/SOURCES

if [ ! -d $RPMBUILD_TOP_DIR ]; then
  rpmdev-setuptree
fi

for SPEC in `find $PROJECT_DIR -type f -name '*.spec'`; do
  DIR=`dirname $SPEC`
  PACKAGE_NAME=`basename $SPEC .spec`

  if [ -n "$TARGET_PACKAGE" ] && [ "$TARGET_PACKAGE" != "$PACKAGE_NAME" ]; then
    continue
  fi

  echo "INFO: Building $PACKAGE_NAME from $SPEC"

  cp $SPEC $RPMBUILD_SPEC_DIR

  for FILE in `spectool --list-files --all $SPEC | cut -d ' ' -f 2`; do
    if expr match "$FILE" '^\(https\?\|ftp\)://' > /dev/null; then
      continue
    fi
    cp $DIR/$FILE $RPMBUILD_SOURCE_DIR
  done

  spectool --get-files --all --sourcedir $SPEC

  rpmbuild -ba --clean --nodeps $SPEC
done
