# make_scope_list (version 2)
This python tool is designed to create a 'targeted' wordlist to use with any util that uses a wordlist.txt like Brute Forcing tools (Hydra, wfuzz, and more...)

The goal is to narrow the contents of the wordlist to a scope that matches the target user.

For example, you may know your target user is a male from the UK, so is worth first tying a wordlist that includes only names, surnames and variations from British English Male names and surnames.

### Usage
Run the script with python3.

The program will first ask you the Mode.

Mode 1 - 'Scope'  will ask you: Language and Gender of the target, and size of the output file.

Mode 2 - 'Laser'  will ask you: Name and surname (if surname not known, will ask language to use the right surname list from /data)

There are currently 4 available language options:

1 - UK english

2 - US english

3 - Spain spanish

4 - LATAM spanish

Using either mode, the resulting wordlist.txt will be available in the tool directory ready to be used.
________________

Feel free to edit the source lists in  /data.

The Extra size option cuts the wordlist to 1 and a half mill. words. To obtain bigger lists feel free to toggle the size of Extra option to a bigger number if your system can handle it ( around line 172 ).

Either for english or spanish target/s, if you didnt get results with your scoped wordlist I recommend trying the other variant of the selected language by running the script again.
________________

________________

###### This is what I consider my first ever 'relevant' personal programming project in python. Any issue, idea, comment will be read and appreciated.

###### Created by Exbinary

