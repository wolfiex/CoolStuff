#!/bin/bash
for f in $(grep -Rl '^>>>>>>> ' --include="*.php" --include="*.css" --include="*.js" --include="*.html" --include="*.svg" --include="*.txt" .)
do
sed -i -e '/^=======/,/^>>>>>>> /d' -e '/^<<<<<<< /d' $f
sed -i -e '/^>>>>>>> /d' $f
echo "$f Fixed"
done
git add . ; git commit -am "[+] Resolved on `date` from `hostname` by `whoami`" --no-verify
