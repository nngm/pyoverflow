pip install -r requirements.txt
echo "Select language: 1. English (en) 2. Korean (ko)"
read language
if [ "$language" == "1" ]; then
    echo "language: en" > config.yaml
    echo "Language set to English."
elif [ "$language" == "2" ]; then
    echo "language: ko" > config.yaml
    echo "Language set to Korean."
else
    echo "Invalid selection. Defaulting to English."
    echo "language: en" > config.yaml
fi
if [ ! -f main.py ]; then
    echo 'import overwatch' > main.py
fi