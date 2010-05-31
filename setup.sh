#!/bin/bash
svn co http://svn.flexget.com/trunk flexget-dev

#Symlink to plugin
cd flexget-dev/flexget/plugins
ln -s ../../../output_growl.py

#Symlink to test
cd ../../tests
ln -s ../../test_growl.py
