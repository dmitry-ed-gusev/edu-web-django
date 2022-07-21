#!/usr/bin/env bash
###############################################################################
#
#   Development environment setup script. Script can be used to re-create
#   development environment fro 'scratch'.
#
#   Warning: script must be used (run) from shell, not from the virtual
#            environment (pipenv shell).
#
#   Created:  Dmitrii Gusev, 21.07.2022
#   Modified:
#
###############################################################################

# -- verbose output mode
VERBOSE="--verbose"
# -- set up encoding/language
export LANG='en_US.UTF-8'
BUILD_DIR='build/'
DIST_DIR='dist/'

clear
printf "Development Virtual Environment setup is starting...\n\n"

# -- upgrade pip
printf "\nUpgrading pip.\n"
pip --no-cache-dir install --upgrade pip

# -- upgrading pipenv (just for the case)
printf "\nUpgrading pipenv.\n"
pip --no-cache-dir install --upgrade pipenv

# -- remove existing virtual environment, clear caches
printf "\nDeleting virtual environment and clearing caches.\n"
pipenv --rm ${VERBOSE}
pipenv --clear ${VERBOSE}

# -- clean build and distribution folders
printf "\nClearing temporary directories.\n"
printf "\nDeleting [%s]...\n" ${BUILD_DIR}
rm -r ${BUILD_DIR}
printf "\nDeleting [%s]...\n" ${BUILD_DIR}
rm -r ${DIST_DIR}

# -- removing Pipfile.lock (re-generate it)
printf "\nRemoving Pipfile.lock\n"
rm Pipfile.lock

# -- install all dependencies, incl. development
printf "\nInstalling dependencies, updating all + outdated.\n"
pipenv install --dev ${VERBOSE}

# - check for vulnerabilities and show dependencies graph
printf "\nChecking virtual environment for vulnerabilities.\n"
pipenv check
pipenv graph

# - outdated packages report
printf "\n\nOutdated packages list (pip list):\n"
pipenv run pip list --outdated
