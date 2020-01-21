# MatplotlibAndMakefile
A Demo on Makefiles
## Overview
This is a demo of using makefile. `make` is a tool to automate tasks which are usually shell commands. We can also mention dependencies so that a series of tasks can be done
## What this demo does?
1. A C file (`datagen.c`) gets compiled to genereate an executable (`datagen`)
2. The executable (`datagen`) is runned to dump the population data into a text file
3. A Python program is called to read the file and plot the data
4. We have 'clean' target to remove the temproary files (which is the dependency for the dataplot target)
## Running the demo
- Start by cloning this repo by running: `git clone https://github.com/vishalbala-nps/MatplotlibAndMakefile`
- After cloning, run the command: `make` This will plot the data
## NOTE
Install the matplotlib module before running it
