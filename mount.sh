#!/bin/bash

source ENV
curlftpfs $HOST ./webroot -o user=$USER:$PASSWORD
