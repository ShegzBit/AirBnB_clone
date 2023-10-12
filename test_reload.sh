#!/usr/bin/env bash
"""
Tests models
"""

bash="shegz~bash$"
echo "$bash cat file.json"
cat file.json

echo "$bash ./test_save_reload_base_model.py"
./test_save_reload_base_model.py

echo "$bash cat file.json ; echo \"\""
cat file.json ; echo ""

echo "$bash ./test_save_reload_base_model.py"
./test_save_reload_base_model.py

echo "$bash ./test_save_reload_base_model.py"
./test_save_reload_base_model.py

echo "$bash cat file.json ; echo \"\""
cat file.json ; echo ""
