#!/bin/bash

# --- Script ---
echo "Regenerating Virolang parser..."

# Run the ANTLR command to generate the parser with the visitor flag
antlr4 -Dlanguage=Python3 -visitor parser/Virolang.g4

echo "Parser regenerated successfully in the 'parser/' directory."
