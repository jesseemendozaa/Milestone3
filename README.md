## Milestone 2 - Recipes
- Jesse Mendoza (@jesseemendozaa)
- Rustico Cruz (@Rooosti)
- Eric Lazarit-Orozco (@ericlazarit)

# Setup instructions:

<p>Clone repo<br>
Navigate to folder</p>

run:
```
python3 -m venv venv
source venv/bin/activate
```

install necessary libraries using pip3:
```
pip3 install -r requirements.txt
```

run in terminal one command at a time:
```
flask shell
from app import db
db.create_all()
exit()
python3 run.py
```

run in terminal to stop virtual environment:
```
deactivate
```
