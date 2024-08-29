#!/bin/bash

#!/bin/bash
set -e
# Run test cases
python3 manage.py test myapp --settings=setup.settings.dev

# If tests pass, start the Django server
if [ $? -eq 0 ]; then
    echo "All tests passed. Starting Django server..."
    python3 manage.py runserver 0.0.0.0:8000 --settings=setup.settings.dev
else
    echo "Tests failed. Not starting Django server."
    exit 1  # Exit with a non-zero status to indicate failure
fi

# Start the Django server
python3 manage.py makemigrations --settings=setup.settings.dev
python3 manage.py migrate --settings=setup.settings.dev
python3 manage.py runserver --settings=setup.settings.dev 0.0.0.0:8000
