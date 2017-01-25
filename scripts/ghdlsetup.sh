#! /usr/bin/env bash

# from https://github.com/VLSI-EDA/PoC/blob/release/tools/Travis-CI/ghdl.setup.sh#L47
# configure variables in the section below
GHDL_BACKEND="llvm"
GHDL_VERSION="0.34dev"
RELEASE_DATE="2016-09-14"

GITHUB_SERVER="https://github.com"
GITHUB_SLUG="tgingold/ghdl"

CIRCLE_DIR="temp/Circle-CI"


# assemble the GitHub URL
# --------------------------------------
# example: 2016-05-03
GITHUB_TAGNAME="$RELEASE_DATE"

# example: ghdl-llvm-0.34dev-2016-05-03.tgz
GITHUB_RELEASE_FILE="ghdl-$GHDL_VERSION-$GHDL_BACKEND-$RELEASE_DATE.tgz"

# example: https://github.com/tgingold/ghdl/releases/download/2016.05.03/ghdl-0.34dev-llvm-2016-05-03.tar.gz
GITHUB_URL="$GITHUB_SERVER/$GITHUB_SLUG/releases/download/$GITHUB_TAGNAME/$GITHUB_RELEASE_FILE"


# other variables
# --------------------------------------
GITROOT=$(pwd)
GHDL_TARBALL="ghdl.tgz"
mkdir -p $CIRCLE_DIR
cd $CIRCLE_DIR

# downloading GHDL
echo -e "${CYAN}Downloading $GHDL_TARBALL from $GITHUB_URL...${NOCOLOR}"
wget -q $GITHUB_URL -O $GHDL_TARBALL
if [ $? -eq 0 ]; then
	echo -e "Download [SUCCESSFUL]"
else
	echo 1>&2 -e "Download of $GITHUB_RELEASE_FILE [FAILED]"
	exit 1
fi

# unpack GHDL
if [ -e $GHDL_TARBALL ]; then
	echo -e "Unpacking $GHDL_TARBALL... "
	tar -xzf $GHDL_TARBALL
	if [ $? -eq 0 ]; then
		echo -e "Unpack [SUCCESSFUL]"
	else
		echo 1>&2 -e "Unpack [FAILED]"
		exit 1
	fi
fi

# remove downloaded files
rm $GHDL_TARBALL

# gcc debugging
echo -e "Testing GCC version and configuration..."
gcc -v

# # test ghdl version
# export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib"
# echo -e "Testing GHDL version..."
# ./bin/ghdl -v
# if [ $? -eq 0 ]; then
# 	echo -e "GHDL test [SUCCESSFUL]"
# else
# 	echo 1>&2 -e "GHDL test [FAILED]"
# 	exit 1
# fi
