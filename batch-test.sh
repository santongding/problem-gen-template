
# export CUR_PROB=squares
for i in {1..100}
do
  echo "start check $i"
  python3 checker.py > check-log
  if [ $? -eq 0 ]; then
    echo "check success"
  else
    echo "failed"
    exit 1
  fi
done