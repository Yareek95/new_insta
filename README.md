# new_insta

1. Clone repo
2. Create <config.ini> in <<Configugation>> folder
          new_insta:
             <<Configurations:
                   -config.ini
                   -here.txt
             <<PageObjects
             <<TestCases
             <<utilities
4. Open config.ini in any text editor.
5. Replace "username1" and "password" with your own credentials.
                        <config.ini>
                        [common info]
                        baseURL = https://www.instagram.com/
                        username1 = write here username
                        password = write here password
7. Save changes.
8. Open cmd in root folder
9. Execute any command,
                        replace "*****" with the Instagram username you want to perform a test on
                        in the following command:
                                 pytest -sv -n auto -k "like and follow" --browser chrome --name *****
                                 pytest -sv -n auto -k "message and follow" --browser chrome --name *****
                                 pytest -sv -n auto -k "like or message or follow" --browser chrome --name *****
   -------
                                 *** Multiple Instagram profiles ***
   
   -modify <config.ini>
             [common info]
             baseURL = https://www.instagram.com/
             username1 = write here username
             username2 = write here username
             username3 = write here username
             username4 = write here username
             password = write here password

Tests run in parallel 
If you want to add more profiles create a copy of any test and change :
                              class TestMessage:
                                  baseURL = ReadConfig.getApplicationURL()
                                  username = ReadConfig.getUserName5()          #replace with number from <config.ini> ReadConfig.getUserName5()
                                  password = ReadConfig.getPassword()
          -modify <config.ini>
                                  [common info]
                                  baseURL = https://www.instagram.com/
                                  username1 = write here username
                                  username2 = write here username
                                  username3 = write here username
                                  username4 = write here username
                                  username5 = write here username
                                  password = write here password
