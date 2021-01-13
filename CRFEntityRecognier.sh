#!/usr/bin/env bash
# vim: set noexpandtab tabstop=2:

n_jobs=1
outdir='model'

usage="Usage:\n\t$0 <-i input_file> [-n number_of_threads] [-o outdir_of_model]"

declare -g -A __sourced__files__
if [[ ! -v __sourced__files__[$BASH_SOURCE] || $__force__source__ ]]; then
	__sourced__files__[$BASH_SOURCE]=$(realpath "$BASH_SOURCE")
	path=$(dirname $(realpath "$BASH_SOURCE"))
	function CRFEntityRecognier {
		while true; do
			case $1 in
				-h|--help)
					echo -e $usage
					return
					;;
				-i)
					infile="$2"
					shift
					shift
					;;
				-n)
				  n_jobs="$2"
					shift
					shift
					;;
				-o)
				  outdir="$2"
					shift
					shift
					;;
				-*)
				  echo "$FUNCNAME:ERROR: Bad option '$1'." >&2
					echo -e $usage
					return -1
					;;
				*)
				  break
					;;
			esac
		done

    if [ ! -d $outdir ];then
      mkdir -p $outdir
		fi

    "$path"/run_pipeline.py $infile $outdir $n_jobs
	}

	if ! { ( return ) } 2>/dev/null; then
		set -e
		CRFEntityRecognier "$@" || exit
	fi
fi

