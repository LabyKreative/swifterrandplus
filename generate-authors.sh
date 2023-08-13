#!/bin/sh
git log --format='%aN <%aE>' | sort -u > AUTHORS