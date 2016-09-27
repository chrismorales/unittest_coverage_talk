#!/usr/bin/env bash

# other working, light coloured reveal.js themes
# beige
# sky
# serif
# simple
# solarized

rst2html5 \
  --jquery \
  --reveal-js \
  --pretty-print-code \
  --reveal-js-opts theme=beige \
  docs/index.rst \
> output/reveal.html
