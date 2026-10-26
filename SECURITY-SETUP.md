# Security deployment changes

Set SECRET_KEY to a new random secret before startup; this invalidates all existing signed sessions. Use Python 3.10 or later and install requirements.txt.

The previously committed SQLite database contained user records. Treat its password hashes and account data as exposed, require password resets, and review Git history access. Removing it from the current tree does not erase history. Do not deploy the sample database.

Back up your production database outside the checkout before deploying. Existing installations must restore their database at calculator/calculator.db; the upgrade explicitly preserves that location. Fresh installations should run `flask --app calculator init-db` before starting the server. Never commit the resulting file.
