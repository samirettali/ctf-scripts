#!/bin/bash

# This script searches in the entire git history

 git rev-list --all | GIT_PAGER=cat xargs git grep "$@"
