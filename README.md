# ccg-bibfiles
Repository to store cogcomp's bib and cited bib files

The full steps of generating ccg-style keys AUTOMATICALLY for your own bibfiles

Step 1 create a new bib file containing *only* your added bib entries: yourfile.bib

Step 2 open the program: java -jar jabref.jar

       open the file: yourfile.bib

       select-all and generate!: Ctrl-a then Ctrl-g

       say yes, you want to overwrite the keys

       save! 

       Manually delete the header:
       % This file was created with JabRef 2.10.
       % Encoding: UTF-8

Step 3 merge yourfile.bib into cited.bib

       either by copy-paste or the "cat" command

Step 4 run script genCitedConference.sh to generate both long and compact bib files


The full steps of maintaining up-to-date ccg.bib

Step 1 Download the latest bib file version from the publication page of the group website:
        
       http://cogcomp.org/bib/ccg.bib

       Remove all the header information

Step 2 manually check if the author names is correctly separated by "and"

       manually correct errors 

       or use the java code for assistance (see MainClass.java for details)

Step 3 run script genCitedConference.sh to generate both long and compact bib files
