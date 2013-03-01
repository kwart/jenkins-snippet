#!/bin/bash
if [ `uname -m` == "i86pc" ]; then
    if [ `uname -r` == "5.11" ]; then
        if [ "$1" == "-d64" ]; then
                XARCH=solaris11_x86_64;
        else
                XARCH=solaris11_x86
        fi
    else
        if [ `uname -r` == "5.10" ]; then
                if [ "$1" == "-d64" ]; then
                        XARCH=solaris10_x86_64;
                else
                        XARCH=solaris10_x86;
                fi
        else
            if [ `uname -r` == "5.9" ]; then
                if [ "$1" == "-d64" ]; then
                        XARCH=solaris9_x86_64;
                else
                        XARCH=solaris9_x86;
                fi
            else
                exit 1
            fi
        fi
    fi
else
    if [ `uname -m` == "i686" ]; then
        XARCH=i686;
    else
        if [ `uname -m` == "x86_64" ]; then
            XARCH=x86_64;
        else
            uname -m | grep -q sun
            if [ $? -eq 0 ]; then
                if [ `uname -r` == "5.11" ]; then
                    XARCH=solaris11_sparc;
                else
                    if [ `uname -r` == "5.10" ]; then
                        XARCH=solaris10_sparc;
                    else
                        if [ `uname -r` == "5.9" ]; then
                            XARCH=solaris9_sparc;
                        else
                            exit 1
                        fi
                    fi
                fi
            else
                exit 1
            fi
        fi
    fi
fi
echo $XARCH

