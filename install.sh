#! /bin/bash


#set the virtual enviroment in local dir with generic name "env" and last actives it.
python3 -m venv env
source env/bin/activate

#install fastapi with all dev features [all] parameters in it last version available, 
#last the requirements is updated with all packages and its installed version since of 
#the date of execution of this script.
pip install -r requirements.txt
pip freeze > requirements.txt

#startsup a server if its incliuded the flag "-y" with the dev basics settigns in port 8000
if[[ "$@" == *"-y"* ]] then
    uvicorn main:app --reload
fi