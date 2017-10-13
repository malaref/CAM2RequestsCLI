# CAM2RequestsCLI
A command line interface for the [CAM2RESTfulAPI](https://github.com/muhammad-alaref/CAM2RESTfulAPI) project using Click.

## Requirements

None.
  
**>> The Requests CLI should be installed and run on the users' machines (not on the cluster nodes).**

## Installation

Using [pip](https://pypi.python.org/pypi/pip):
```shell
pip install git+https://github.com/muhammad-alaref/CAM2RequestsCLI
```

## Usage

The CLI provides a very `git`-like interface. All commands, parameters and options are explained by the `CAM2RequestsCLI --help` command.  
Alternatively, its commands can be used by any custom Python script by importing the `CAM2RequestsCLI.commands` module.

## Bash completion (optional)

For safety backup the `.bashrc` first:
```shell
cp ~/.bashrc ~/.bashrc.bak
```
Then, issue these commands:
```shell
_CAM2REQUESTSCLI_COMPLETE=source CAM2RequestsCLI > ~/.CAM2RequestsCLI-complete.sh
echo '. ~/.CAM2RequestsCLI-complete.sh' >> ~/.bashrc
```
