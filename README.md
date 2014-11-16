Overview
===
Convert Google Contacts CSV to XML suitable for most Grandstream VoIP phones. 

Compatibility
-
Written using Python 3 and tested on Granstream GXP 2130

Use
-
Download grandstreamXMLphonebook.py and make it executable.
Run the script: ./grandstreamXMLphonebook.py /location/of/google_contacs.csv /location/of/phonebook.xml

Note
-
At the time this was writted Google contacts exports to CSV with the follwoing field names
You may have more numbered items (Phone # - Value) but the code should still be able to handle this

Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Address 1 - Type,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address,Website 1 - Type,Website 1 - Value

Licence
-
You are free to use, reuse, change, distribute, etc.
