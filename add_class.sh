#!/bin/bash
# set micrograph directory and km_groups.csv paths
dir="mics"
csvfile=""

{
read
while IFS=',' read -r filename class
do
  if [ -f "$dir/$filename" ]; then
    name=${filename%.*}
    mv "$dir/$filename" "$dir/${name}_${class}.mrc"
  else
    echo "${filename} does not exist in $dir."
  fi
done
}< $csvfile
