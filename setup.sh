#!/bin/bash
read -p "Do you want to (re)create the virtualenv ?[y/n]" reponse
if echo "$reponse" | grep -iq "^y" ;then
    rm -rf venv
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Environnement created"
fi

echo -e "-------------------------------------\n"
echo -e "- source venv/bin/activate\n- python3 bot.py"
