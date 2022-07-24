#!/usr/bin/env sh
# shellcheck disable=SC2059

# Colors
RED_BG='\033[41m'
YELLOW_BG='\033[0;43m'
NO_COLOR='\033[0m'

# Get regex file
if [ -n "$PRE_COMMIT_REGEX" ] && [ -f "$PRE_COMMIT_REGEX" ]; then
  regexes="$PRE_COMMIT_REGEX"

elif [ -f "$(git rev-parse --show-toplevel)/.pre-commit-regex" ]; then
  regexes="$(git rev-parse --show-toplevel)/.pre-commit-regex"

elif [ -f "$HOME/.pre-commit-regex" ]; then
  regexes="$HOME/.pre-commit-regex"

else
  printf "${YELLOW_BG}[WARNING]${NO_COLOR} no regex provided"
  exit 0
fi

exit_code=0

for path in "$@"; do
  while IFS= read -r regex; do

    # Skip blank lines and comments
    if [ -z "$regex" ] || [ "${regex#\#}" != "$regex" ]; then
      continue
    fi

    if match=$(grep -Eio "$regex" "$path"); then
      printf "${RED_BG}[FAIL]${NO_COLOR} $path $match matched $regex\n"
      exit_code=1
    fi

  done < "$regexes"
done

exit $exit_code
