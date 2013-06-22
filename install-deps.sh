#!/bin/bash
#
# usage: ./install-deps.sh [<target-package>]

set -e

if [ $# -ge 1 ]; then
  TARGET_PACKAGE=$1
fi

PROJECT_DIR=`cd \`dirname $0\` && pwd`

SPECS=`find $PROJECT_DIR -type f -name "${TARGET_PACKAGE:-*}.spec"`

yum-builddep -y $SPECS
