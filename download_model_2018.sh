#!/usr/bin/env bash

if [ ! -e "20180402-114759.zip" ]
then
	rm -f ./cookies.txt
	touch ./cookies.txt
	wget --load-cookies ./cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ./cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-" -O 20180402-114759.zip && rm -rf ./cookies.txt
	unzip 20180402-114759.zip
	rm -f 20180402-114759.zip
	rm -f ./cookies.txt
fi
