echo "Installing sqlite3..."
sudo apt install sqlite3
echo ""
echo "Installing sqlitebrowser..."
sudo apt install sqlitebrowser
echo ""
echo "Installing python3.8..."
sudo apt install python3.8
echo ""
echo "Installing python3.8-venv..."
sudo apt install python3.8-venv
echo ""
echo "Installing python3-pip..."
sudo apt install python3-pip
echo ""
echo "Setting up venv..."
python3.8 -m venv venv
echo ""
echo "Changing permission of venv..."
chmod 777 -R venv
sed -i 's/\r$//' ./venv/Scripts/activate
echo ""
echo "Activating venv..."
./venv/Scripts/activate
echo ""
echo "Installing packages..."
pip3 install -r ./requirements.txt
echo ""
echo "Migrating..."
python3.8 manage.py migrate
echo ""
echo "Creating super user..."
python3.8 manage.py createsuperuser
echo ""
echo "Running server..."
python3.8 manage.py runserver 0.0.0.0:8000

