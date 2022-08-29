probs=$(cat ./changed-probs-for-pack.txt)
python3 pack.py ${probs}
stat=$?
if [ $stat -eq 0 ]; then
  echo pack success
  rm -r release.zip
  cd temp-package || exit 1
  fs=$(ls)
  zip -r ../release.zip $fs
  cd .. || exit 1
elif [ $stat -eq 255 ]; then
  echo nothing to pack
else
  echo "failed"
  exit 1
fi