#!/bin/bash

multimarkdown --to=latex content.mmd > content.tex &&
    omgtex.rb -ob content.tex
