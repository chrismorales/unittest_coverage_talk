#!/usr/bin/env bash

rst2html5 \
  --jquery \
  --reveal-js \
  --pretty-print-code \
  docs/index.rst \
> output/reveal.html
