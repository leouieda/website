#!/bin/bash
# Based on
# http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html
# and https://github.com/richfitz/wood
echo -e "Preparing to copy generated files to leouieda.com"
if [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_BRANCH" == "master" ]; then
    echo -e "Starting to update website\n"
    cp -R output $HOME/keep
    # Go to home and setup git
    cd $HOME
    git config --global user.email "leouieda@gmail.com"
    git config --global user.name "Leonardo Uieda"
    git config --global github.user "leouieda"
    echo -e "Cloning project"
    # Clone the project, using the secret token. Uses /dev/null to avoid leaking decrypted key
    git clone --quiet --branch=master --single-branch https://${GH_TOKEN}@github.com/leouieda/leouieda.github.com.git leouieda.com > /dev/null
    cd leouieda.com
    # Move the old branch out of the way and create a new one:
    git branch -m master-old
    git checkout --orphan master
    # Delete all the files and replace with our good set
    git rm -rf .
    cp -Rf $HOME/keep/. $HOME/leouieda.com
    # add, commit and push files
    git add -f .
    git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to leouieda.github.com"
    echo -e "Pushing to leouieda.github.com"
    git push -fq origin master > /dev/null
    echo -e "Uploaded generated files\n"
else
    echo -e "This is a pull request, not copying files"
fi
echo -e "Done"
