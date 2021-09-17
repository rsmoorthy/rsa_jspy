TEXT="work is_god"


ENCRYPTED=$(python3 tst.py -p client.pub --text "$TEXT" -e)
DECRYPTED=$(node tst.js -P client.priv -d --text $ENCRYPTED)

if [[ "$DECRYPTED" == "$TEXT" ]]; then
  echo "server to client comm okay"
else
  echo "server to client comm failed"
fi

JENCRYPTED=$(node tst.js -p server.pub --text "$TEXT" -e)
DECRYPTED=$(python3 tst.py -P server.priv -d --text $JENCRYPTED)

if [[ "$DECRYPTED" == "$TEXT" ]]; then
  echo "client to server comm okay"
else
  echo "client to server comm failed"
fi
