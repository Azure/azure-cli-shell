# Azure CLI Interactive Shell

## The interactive shell for Microsoft Azure CLI (Command Line Interface)

- Interactive Tutorials
- Lightweight Drop Down Completions 
- Auto Cached Suggestions 
- Dynamic parameter completion 
- Defaulting scopes of commands
- On the fly descriptions of the commands AND parameters 
- On the fly examples of how to utilize each command 
- Query the previous command
- Navigation of example pane 
- Optional layout configurations 
- Optional "az" component 
- Fun Colors 

![Overview](docs/shell_tutorial.gif)

## Installation

```bash
   $ pip install --user azure-cli-shell
```

## Running

To start the application

```bash
   $ az-shell
```

Then type your commands and hit [Enter]

To use commands outside the application

```bash
   $ #[command]
```

To Search through the last command as json
jmespath format for querying

```bash
   $ ? [param]
```

*Note: Only if the previous command dumps out json, e.g. vm list*

To only see the commands for a command

```bash
   $ %% [top-level command]
```

To undefault a value

```bash
   $ ^^ [value to undefault]
```

## Use Examples

Type a command, for example:

```bash
   $ vm create
```

Look at the examples

*Scroll through the pane with Control Y for up and Control N for down #*

Pick the example you want with:

```bash
   $ vm create :: [Example Number]
```

## Dev Setup

Fork and clone repository

```bash
   $ . dev_setup.py
```

To get the Exit Code of the previous command:

```
   $ $
```

## Docker Image


There is a docker image on docker hub

```bash
   $ docker pull oakeyc/az-cli-shell:latest
   $ docker run -it oakeyc/az-cli-shell:latest
   root#: az-shell
```
