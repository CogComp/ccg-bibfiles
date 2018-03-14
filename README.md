# ccg-bibfiles
Repository to store cogcomp's bib and cited bib files

The full steps of generating ccg-style keys AUTOMATICALLY for your own bibfiles
Step 0 create a new bib file containing *only* your added bib entries: yourfile.bib
Step 1 use the java code to check if the author names is correctly separated by "and"
       correct errors if you encounter any
Step 2 open the program: java -jar jabref.jar
       open the file: yourfile.bib
       select-all and generate!: Ctrl-a then Ctrl-g
       say yes, you want to overwrite the keys
       save! done
Step 3 merge yourfile.bib into both cited.bib and ccg.bib
       either by copy-paste or the "cat" command
Step 4 run script genCitedConference.sh to generate both long and compact bib files
