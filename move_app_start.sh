#! /bin/bash
# 获取相对路径
PRG="$0"
while [ -h "$PRG" ]; do
  ls=$(ls -ld "$PRG")
  link=$(expr "$ls" : '.*->  \(.*\)$')
  if expr "$link" : '.*/.*'  >/dev/null; then
    PRG="$link"
  else 
    PRG=$(dirname "$PRG")/"$link"
  fi
done
PRGDIR=$(dirname "$PRG")
# full path
cd  "$PRGDIR"/ 
PRGDIR=$(pwd)

python -m pip install pyperclip -i https://pypi.tuna.tsinghua.edu.cn/simple
python $PRGDIR/move_app.py