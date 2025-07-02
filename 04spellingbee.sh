gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E "^[oznrica]{4,}$" | grep -c "r"
