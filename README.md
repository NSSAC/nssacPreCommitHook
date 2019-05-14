# nssacPreCommitHook

## Install

Clone the repository and execute one of the following:

* User local installation
``` shell
./setup.py install --user
```

* System installation
``` shell
sudo ./setup.py install
```
## Configuration
The configuration uses a [JSON schema](https://github.com/NSSAC/nssacPreCommitHook/blob/master/schema/preCommitHook.json) to specify the license and the copyright statements to be used.

Two examples are provided:
  * [Example 1](https://github.com/NSSAC/nssacPreCommitHook/blob/master/schema/example.json)
  * [Example 2](https://github.com/NSSAC/nssacPreCommitHook/blob/master/test/example.json)
  
## Enable nssacPreCommitHook for a repository
Download [Example](https://github.com/NSSAC/nssacPreCommitHook/blob/master/schema/example.json) and save it. 

``` shell
preCommitHook --init -r repository -c Path_to_Example
```

If you saved the example as repository/.nssac.json you may ommit `-c Path_to_Example`

## Suported file formats:
The patterns section of the example currently supports the following formats
* __C/C++__ "*.cpp", "*.hpp", "*.c", "*.h", "*.h.in"
* __Java__ "*.java"
* __XML__ "*.xsd", "*.xml", "*.rng"
* __Shell__ "*.sh"
* __CMake__ "*.cmake", "CMakeLists.txt"
* __Python__ "*.py"

It is not difficult to add more file types often is is just adding another pattern to the include section of an exiting pattern.
