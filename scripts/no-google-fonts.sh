#!/usr/bin/env bash
# Fails if any file under the given directory hotlinks Google Fonts or the Fontshare CDN.
# Usage: scripts/no-google-fonts.sh [dir]
set -euo pipefail

dir="${1:-.}"
pattern='fonts\.(googleapis|gstatic)\.com|api\.fontshare\.com'

if grep -rEn --exclude-dir={node_modules,.git,dist,build,.next} \
     --exclude=no-google-fonts.sh --exclude=README.md "$pattern" "$dir"; then
  echo
  echo "✗ Third-party font hotlink found. Self-host the files instead." >&2
  exit 1
fi

echo "✓ No third-party font hotlinks in $dir"
