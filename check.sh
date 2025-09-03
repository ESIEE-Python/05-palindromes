#!/bin/bash
# Script to check pylint and pytest scores

# Run pylint and extract the score
PYLINT_SCORE=$(pylint main.py --score=y --output-format=text | grep -o 'Your code has been rated at [0-9]\+\.[0-9]\+/10' | awk '{print $7}' | cut -d'/' -f1)
echo "Pylint score: $PYLINT_SCORE/10"

# Run pytest and output JUnit XML
pytest .python/test_.py --junitxml=pytest_results.xml > /dev/null 2>&1

# Get pytest score using the provided script
PYTEST_RESULT=$(python .python/get_pytest_score.py pytest_results.xml)
echo "Pytest score: $PYTEST_RESULT"
