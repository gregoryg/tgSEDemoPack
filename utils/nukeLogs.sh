#!/bin/bash

echo 'nuke the tg logs'
echo ''
echo 'Make sure TG is not running first'

resp=$(gsql -v)
if [[ "$resp" == *"refused"* || "$resp" == *"not found"* ]]; then
	find . -type f -name '*.log' -delete
	find . -type f -name '*.progress' -delete
	find . -type f -name '*.progress.summary' -delete
	find . -type f -name '*.out' -delete

    echo "Tigergraph logs cleaned up."
    exit 0
fi

    echo "Tigergraph server is running here. Please stop with:"
    echo "   gadmin stop all"
    echo "...and re-run this script"

