#!/bin/bash

echo '========= Jasmine Tests =========='
jasmine-node tests/js/spec/

echo '========= Behave Tests =========='
behave tests/py/
