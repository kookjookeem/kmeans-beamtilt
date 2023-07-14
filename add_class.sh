#!/bin/bash

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -h, --help                Display this help message."
    echo "  -d, --dir DIRECTORY       Set the micrograph directory path."
    echo "  -i, --input FILE          Set the input CSV file path."
}

dir=""
csvfile=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            exit 0
            ;;
        -d|--dir)
            dir="$2"
            shift 2
            ;;
        -i|--input)
            csvfile="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

if [[ -z $dir ]] || [[ -z $csvfile ]]; then
    echo "Error: Micrograph directory and input CSV file must be provided."
    usage
    exit 1
fi

while IFS=',' read -r filename class; do
    if [ -f "$dir/$filename" ]; then
        name=${filename%.*}
        mv "$dir/$filename" "$dir/${name}_${class}.mrc"
    else
        echo "${filename} does not exist in $dir."
    fi
done < "$csvfile"
