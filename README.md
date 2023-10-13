# new_insta

1. Clone repo
2. Create config.ini inside Configugation
          new_insta:
             <<Configurations:
                   -config.ini
                   -here.txt
             <<PageObjects
             <<TestCases
             <<utilities
4. Open config.ini in any text editor
5. Change username, password, search_name etc.
   config.ini content:
              [common info]
              baseURL = https://www.instagram.com/
              username = write here username
              password = write here password
              search_name = write here item to searched for
7. Save changes.
8. Open cmd in rool folder
9. Execute command:
             pytest -sv --browser chrome
