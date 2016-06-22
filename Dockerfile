from ubuntu:16.04

run apt-get -y update && apt-get install -y git
run apt-get install -y python2.7
run apt-get install -y python-pip
run pip install gitpython
run pip install Flask
run pip install unidiff
