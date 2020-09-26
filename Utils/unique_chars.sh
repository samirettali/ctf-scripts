#!/usr/bin/env bash
od -cvAnone -w1 | sort -b | uniq -c | sort -rn
