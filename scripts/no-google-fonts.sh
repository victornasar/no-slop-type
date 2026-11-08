#!/usr/bin/env bash
# Fails if any file under the given directory hotlinks Google Fonts.
# Usage: scripts/no-google-fonts.sh [dir]
set -euo pipefail

dir="${1:-.}"
pattern='fonts\.(googleapis|gstatic)\.com'

if grep -rEn --exclude-dir={node_modules,.git,dist,build,.next} \
     --exclude=no-google-fonts.sh --exclude=README.md "$pattern" "$dir"; then
  echo
  echo "✗ Google Fonts hotlink found. Self-host the files instead." >&2
  exit 1
fi

echo "✓ No Google Fonts hotlinks in $dir"
