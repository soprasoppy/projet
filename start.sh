if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SUPEREL/Elie.git /Elie
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Elie
fi
cd /Elie
pip3 install -U -r requirements.txt
echo "Starting Techno Mindz..."
python3 bot.py
