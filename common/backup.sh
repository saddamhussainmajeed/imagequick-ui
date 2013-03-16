#!/bin/bash

mongodump -h $1 -d $2 -c $3 -o files/backups/$4 
