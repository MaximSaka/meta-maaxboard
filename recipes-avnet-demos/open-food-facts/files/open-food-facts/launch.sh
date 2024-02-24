#!/bin/sh
date -d "$(wget --method=HEAD -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f4-10)"

OUTPUT=$(pip3 show pydantic_core | grep Version)
if [[ $OUTPUT != *"2.14.6"* ]]; then
  echo "pydantic_core 2.14.6 not found"
  echo "Installing pydantic_core 2.14.6 ..."
  pip3 install pydantic_core==2.14.6
fi

OUTPUT=$(pip3 show pyzbar | grep Version)
if [[ $OUTPUT != *"0.1.9"* ]]; then
  echo "pyzbar 0.1.9 not found"
  echo "Installing pyzbar 0.1.9 ..."
  pip3 install pyzbar==0.1.9
fi

python3 /home/root/open-food-facts/OpenFoodFactsDemo.py