#!/bin/sh
msg=$(cat ../$1)
file="../$1"
red=`tput setaf 1`
reset=`tput sgr0`
if [[ ${msg:0:1} =~ [a-z] ]]; then
    echo "${red}Sorry, commit failed. First letter must be in uppercase!${reset}"
    exit 1
fi;

if grep -P -n "[^\x00-\x7F]"  ${file} &>/dev/null; then
    echo "${red}Sorry, commit failed. No Chinese plz!${reset}"
    exit 1
fi

# Must reference an issue
if ! grep -i '\(Merge\|Hotfix\|#[[:digit:]]\+\)' ${file} &>/dev/null; then
    echo "${red}Sorry, commit failed. Reference an issue plz!${reset}"
    exit 2
fi
