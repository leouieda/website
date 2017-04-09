---
title: "Increase the reproducibility of your papers with conda environments"
date: 2017-04-09
thumbnail: using-conda-envs.png
layout: post
---

Possible titles:

* Keep sane with conda environments
* Manage your dependencies with conda environments

Depends  on target audience. Maybe better to target scientists with the
reproducibility keyword.



Summary.

The problem that conda envs solve.


# Basics

How to create an env from the command line.

Activate and deactivate.


# Managing paper/project dependencies

Create using an `environment.yml` file.

Use one file/env per project.

Adding channels and conda-forge.

Examples from pinga-lab and from my classes.


# Minimize mental load with automation

Only works on bash and terminals (no `cmd.exe`).

It can get really annoying typing `source activate some_env` and `source
deactivate`.

Create *aliases* to minimize typing.

When you have one environment per project/paper, it can get hard to remember
all the env names.

Automation to the rescue.

Use this bash function to identify the conda env of the current folder and
activate it:

    get_env_name() {
        # Get the environment name from a conda yml file
        grep "name: *" $1 | sed -n -e 's/name: //p'
    }

    activate_conda_env() {
        # Activate the env from an environment.yml file if no argument is provided
        if [[ $# -eq 0 ]]; then
            if [[ -e "environment.yml" ]]; then
                source activate `get_env_name environment.yml`;
            else
                echo "No environment.yml found" && exit 1;
            fi
        else
            source activate "$@";
        fi
    }

Aliases:

    alias cenv='activate_conda_env'
    alias off='source deactivate'

Add it to your `.bashrc` or `.bash_profile` file in your home directory.

Now you type `cenv` without having to remember the name of your environment.

There is also autoenv but it can get a bit slow to `cd` into directories.


# Final thought

Use something to manage your dependencies.

Make them explicit with an environment definition file.

Doesn't have to be conda.
Can be Docker and `Dockerfile`s, virtualenv and `requirements.txt`  files.

Conda envs work nicely because you can also define Python version.

Automate activation of environments to minimize frustration and chance of
errors.


**What is your workflow? How do you manage dependency hell?**

----

*["Green Anaconda in Trivandrum Zoo" by Mithun.M.Das](https://commons.wikimedia.org/wiki/File:Green_Anaconda_in_Trivandrum_Zoo.jpg)
is licensed CC-BY-SA.*
