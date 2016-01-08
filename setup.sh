#!/bin/sh

echo 'Activate tracked git pre commit hook.'
ln -vsf ../../pre-commit .git/hooks/pre-commit
