#!/bin/bash
set -evx

mkdir ~/.PACGlobal

# safety check
if [ ! -f ~/.PACGlobal/.pacglobal.conf ]; then
  cp share/pacglobal.conf.example ~/.PACGlobal/pacglobal.conf
fi
