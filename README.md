# bin
## Description
A collection of scripts for systems administrators. 

# Installation
## No installation//local directory
  1) clone the repository
  ```bash
  git clone git@github.com:jay13jay/bin.git $HOME/bin
  ```
  2 set permissions
  ```bash
  find ~/bin -type d -exec chmod 700 {} \;
  find ~/bin  -type f -exec chmod 500 {} \;
  ```
  3 run scripts directly
  ```bash
  bash ~/bin/[SCRIPT]
  ```
  
## Local user installation
  1) Clone the repo into home directory
  ```bash
  git clone git@github.com:jay13jay/bin.git $HOME/bin
  ```
  2) Modify $PATH to include users bin
  ```bash
  echo "export PATH=$PATH;$HOME/bin" >> ~/.bashrc
  ```
  3) source path changes
  ```bash
  source ~/.bashrc
  ```
  4) set permissions
  ```bash
  find ~/bin -type d -exec chmod 700 {} \;
  find ~/bin  -type f -exec chmod 500 {} \;
  ```
