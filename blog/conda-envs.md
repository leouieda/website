---
title: "Manage project dependencies with conda environments"
date: 2018-12-26
---

> **TL;DR:** Create a conda environment for each project, capture exact versions when
> possible, automate [activation and updating with a bash function](https://github.com/leouieda/dotfiles/blob/e95f6d951d8ddf6ffa303fdca38ebcf620dc5d6c/.bash/functions.sh#L72).

I often work on several different projects involving software:
[Python libraries](https://github.com/leouieda),
[papers](/publications),
[presentations](/presentations),
[this website](https://github.com/leouieda/website),
etc.
Each project has different dependencies and there is a non-zero chance that these
dependencies might be in conflict with each other.
For example, I need Python 2.7 to work on a
[tesseroid modeling paper](/publications) with a student,
while my current work on [GMT/Python](/blog/hawaii-gmt-postdoc.html) and
[GPS interpolation](https://github.com/leouieda/agu2018) project are Python
3.5+ only.
Clearly, I can't have everything under the same Python installation.
That's where virtual environments come in.

Virtual environments allow you to create multiple separate Python installations
("environments").
You can install different packages on each and switch between them easily.
Currently, you can do this using Python's
[virtualenv](https://virtualenv.pypa.io/en/latest/) or using the
[conda package manager](https://conda.io/docs/).
I use conda for all my package management because I need non-Python packages and
multiple Python versions.
If you're new to conda, please go check out
[Eric Ma's great tips for working with conda](http://ericmjl.com/blog/2018/12/25/conda-hacks-for-data-science-efficiency/).


In this post, I'll share some more tips and a bash function I made for managing
environments.


## When to create environments

First of all, I want to reiterate Eric's second hack:
**create one conda environment for each project**.

I have been doing this for a few years now and even included a default environment file
in [my research group's paper template](/blog/paper-template.html).
As soon as I start a new project repository, I'll create an `environment.yml` with the
configuration I need:

```yaml
## The name of the environment matching the repository name
name: same-as-repository
## I prefer conda-forge packages for my projects
channels:
- conda-forge
- defaults
## Start with Python and include everything you need
dependencies:
- python=3.7
- pip
- numpy
...
```

With this file in the repository, you can create the new environment by running:

```bash
conda env create
```

The advantage of always having the environment file is that I always know what each
project needs. This is particularly useful when switching back and forth between a
laptop and desktop or when returning to a project after a while.

Now you can activate the environment using `source activate same-as-repository`
to get access to a completely separate Python installation.
When switching to a different project, always `source activate environment-name` and
then run your code.

See the
[conda docs](https://conda.io/docs/user-guide/tasks/manage-environments.html)
for more information on environments.


## Be as specific as you can

When creating environments for papers, it's a good idea to capture the exact versions of
every package so that you can rebuild the environment later on.
Otherwise, there is the risk of dependencies updating and your code no longer running.
You might not want to do this if you're still in the middle of the project and
adding new dependencies.

Once a paper is accepted, I'll usually export the environment with exact version numbers
using:

```bash
conda env export > environment.yml
```


## Automate the boring parts

I have a git repository for
[nearly everything I do](https://github.com/leouieda?tab=repositories) and most of them
have an `environment.yml` file.
With so many environments, it can be really hard to remember all their names and type
out `conda activate paper-moho-inversion-tesseroids`.
Instead of using really short names, let's automate the activation and some other useful
commands with a bash function:

```bash
function cenv() {

## Usage and help message
read -r -d '' CENV_HELP <<-'EOF'
Usage: cenv [COMMAND] [FILE]

Detect, activate, delete, and update conda environments.
FILE should be a conda .yml environment file.
If FILE is not given, assumes it is environment.yml.
Automatically finds the environment name from FILE.

Commands:

  None     Activates the environment
  rm       Delete the environment
  up       Update the environment

EOF

    envfile="environment.yml"

    ## Parse the command line arguments
    if [[ $## -gt 2 ]]; then
        errcho "Invalid argument(s): $@";
        return 1;
    elif [[ $## == 0 ]]; then
        cmd="activate"
    elif [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
        echo "$CENV_HELP";
        return 0;
    elif [[ "$1" == "rm" ]]; then
        cmd="delete"
        if [[ $## == 2 ]]; then
            envfile="$2"
        fi
    elif [[ "$1" == "up" ]]; then
        cmd="update"
        if [[ $## == 2 ]]; then
            envfile="$2"
        fi
    elif [[ $## == 1 ]]; then
        envfile="$1"
        cmd="activate"
    else
        errcho "Invalid argument(s): $@";
        return 1;
    fi

    ## Check if the file exists
    if [[ ! -e "$envfile" ]]; then
        errcho "Environment file not found:" $envfile;
        return 1;
    fi

    ## Get the environment name from the yaml file
    envname=$(grep "name: *" $envfile | sed -n -e 's/name: //p')

    ## Execute one of these actions: activate, update, delete
    if [[ $cmd == "activate" ]]; then
        source activate "$envname";
    elif [[ $cmd == "update" ]]; then
        errcho "Updating environment:" $envname;
        source activate "$envname";
        conda env update -f "$envfile"
    elif [[ $cmd == "delete" ]]; then
        errcho "Removing environment:" $envname;
        source deactivate;
        conda env remove --name "$envname";
    fi
}
```

Copy this code into your `~/.bashrc` file and restart your terminal.
Now you can activate an environment using the `cenv` command:

```bash
(base) $ cd papers/my-long-project-name

(base) $ ls -F
code/ manuscrip/ data/ README.md LICENSE.txt environment.yml

(base) $ head -n 1 environment.yml
name: my-long-project-env-name

(base) $ cenv

(my-long-project-env-name) $
```

With no arguments, `cenv` will find the `environment.yml`, extract the environment name,
and activate it.
You can also specify the file as an argument.
I find this preferable to using `conda-auto-env`, as suggested in Eric's post, because
conda is not the fastest program and I get frustrated by the slowdown in the `cd`
command.

If you add new dependencies to `environment.yml`, you can update the environment by
running:

```bash
$ cenv up
```

Or you can delete the environment using:

```bash
$ cenv rm
```

With these commands, updating and activating environments is simple and quick to type so
there is no excuse for not using them abundantly.

**NOTE:**
If you're using **Jupyter notebooks**, the `cenv` function might not be that useful.
In that case, I recommend installing the
[`nb_conda` package](https://github.com/Anaconda-Platform/nb_conda).
It allows you to specify which environment you want your notebook to run under when you
create a new notebook or change the kernel.


## Final thoughts

The main takeaways here are:

1. Use a tool to manage your dependencies (whatever works for you)
2. Automate the process so you won't be lazy
3. Specify exact version numbers for long(er) term reproducibility

I use conda because it suits my needs but similar features exits in other package
managers.
If you prefer `pip` with [pipenv](https://pipenv.readthedocs.io/en/latest/), by all
means use them.

The source code for the `cenv` function is in
[my `dotfiles` repository](https://github.com/leouieda/dotfiles) and is
[MIT licensed](https://github.com/leouieda/dotfiles/blob/master/LICENSE).
The exact version of the code shown here is
[in `.bash/functions.sh` commit e95f6d9](https://github.com/leouieda/dotfiles/blob/e95f6d951d8ddf6ffa303fdca38ebcf620dc5d6c/.bash/functions.sh#L72).
Additions and contributions are more than welcome!


**What are your conda workflow/productivity hacks?**
