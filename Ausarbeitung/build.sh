#!/bin/bash

multimarkdown --to=latex content.mmd > content.tex &&
    omgtex.rb -obe content.tex
