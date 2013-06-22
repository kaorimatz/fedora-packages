#!/bin/bash
#
# usage: ./build-remote.sh <vm-name> [<target-package>]

set -e

if [ $# -lt 1 ]; then
  echo "usage: $0 <vm-name> [<target-package>]"
  exit 1
fi

VM_NAME=$1
if [ $# -ge 2 ]; then
  TARGET_PACKAGE=$2
fi

VAGRANT_ROOT='/vagrant'

vagrant up "$VM_NAME" --provider=aws

vagrant ssh "$VM_NAME" -c "sudo $VAGRANT_ROOT/install-deps.sh $TARGET_PACKAGE"
vagrant ssh "$VM_NAME" -c "$VAGRANT_ROOT/build.sh $TARGET_PACKAGE"

SSH_CONFIG_FILE=`mktemp`
vagrant ssh-config "$VM_NAME" > $SSH_CONFIG_FILE
scp -r -F $SSH_CONFIG_FILE "$VM_NAME":~/rpmbuild ~/
rm -f $SSH_CONFIG_FILE
