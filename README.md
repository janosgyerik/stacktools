Stack Tools
===========
Custom tools based on a python API of Stack Exchange:
http://stackapps.com/questions/198/py-stackexchange-an-api-wrapper-for-python
https://github.com/lucjon/Py-StackExchange/wiki


Setup
-----
1. Install required python modules

        pip install -r requirements.txt


Command Line Interface
----------------------
All the scripts ./scripts/\* have useful help with `-h` or `--help`


Examples
--------
- Print the list of sites

        $ ./scripts/sites.py | head
        Stack Overflow - http://stackoverflow.com
        Server Fault - http://serverfault.com
        Super User - http://superuser.com
        Meta Stack Overflow - http://meta.stackoverflow.com
        Web Applications - http://webapps.stackexchange.com
        Arqade - http://gaming.stackexchange.com
        Webmasters - http://webmasters.stackexchange.com
        Seasoned Advice - http://cooking.stackexchange.com
        Game Development - http://gamedev.stackexchange.com
        Photography - http://photo.stackexchange.com

- Find a site by keyword

        $ ./scripts/sites.py -s unix
        Unix and Linux - http://unix.stackexchange.com

- Print the list of badges of a selected site

        $ ./scripts/sites.py -s unix -b | head
          6784 Supporter: First up vote
          5452 Autobiographer: Completed all user profile fields
          5022 Student: Asked first question with score of 1 or more
          3585 Teacher: Answered first question with score of 1 or more
          3177 Scholar: Asked a question and accepted an answer
          2880 Editor: First edit
          1355 Nice Answer: Answer score of 10 or more
          1170 Popular Question: Asked a question with 1,000 views
           889 Yearling: Active member for a year, earning at least 200 reputation
           824 Commentator: Left 10 comments

