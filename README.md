# ccg-bibfiles
Repository to store cogcomp's bib and cited bib files

The full steps of generating ccg-style keys AUTOMATICALLY for your own bibfiles

Step 1 Create a new bib file containing *only* your added bib entries: yourfile.bib

Step 2 Merge yourfile.bib into cited.bib

       either by copy-paste or the "cat" command

Step 3 *Sub-rountine - Generate correct bib entry keys and sort them by year via JabRef*

       To generate cited-recent.bib: 

              select all entries after year 2004 (2004 included) and make a copy

Step 4 Run script genCitedConference.sh to generate both long and compact bib files

The full steps of maintaining up-to-date ccg.bib

Step 1 Download the latest bib file version from the group server:
        
       scp hpeng7@legolas.cs.illinois.edu:/srv/data/cogcomp/html/bib/ccg.bib ccg_web.bib

       Remove all the header information

Step 2 Check if the author names is correctly separated by "and"

       manually correct errors 

       or use the java code for assistance (see MainClass.java for details)

Step 3 *Sub-rountine - Generate correct bib entry keys and sort them by year via JabRef*

Step 4 Update the group server version with the fixed ccg_web.bib 

       Add back all the header information

       scp ccg_web.bib legolas.cs.illinois.edu /srv/data/cogcomp/html/bib/ccg.bib

Step 5 Remove all the header information from ccg_web.bib to get ccg.bib

Step 6 Run script genCitedConference.sh to generate both long and compact bib files

*Sub-rountine - Generate correct bib entry keys and sort them by year via JabRef*

       open the program: java -jar jabref.jar

       open file: cited.bib / ccg.bib

       sort all bib entries by year (descending order, i.e. the most recent appears first)

       select-all and generate!: Ctrl-a then Ctrl-g

       say yes, you want to overwrite the keys

       open "Options" - "Preferences" from menu bar, and select "File"

              in "Sort Order" section, make sure you select "Save in current table sort order" 

       save! 

       Manually delete the header:
       % This file was created with JabRef 2.10.
       % Encoding: UTF-8