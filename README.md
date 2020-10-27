# ccg-bibfiles
Repository to store CogComp's BibTex files for (1) [All Cogcomp publications](https://cogcomp.seas.upenn.edu/page/publications/). (2) All citations from CogComp papers. 
### Last Updated: Oct. 24, 2020
## Guide for Using bib files during Paper Writing
We recommend using 3 bib files for paper writing. 
1. **ccg.bib**, which has all previous papers from CogComp.
2. **cited.bib**, which includes all cited papers in previous CogComp publications
3. **new.bib**, where you will put all new citations in. 

## Format of CogComp style bib item
If you paper has <= 3 authors, the key for an entry should be the concatenation of:
1. The full last name of the first author (first letter capitalized),
2. The first two characters of the last name of each following author (first letter capitalized),
3. The last two digits of the year of the publication, and
4. [Optional] A letter from "bcdefg..." or other text (e.g. volume number) if necessary to yield unique keys.

Entries with more than 3 authors should replace (1) and (2) with
the first letter of each author's last name, capitalized.

**Example:** For a paper written in `2020`, by `John Doe` and `Nick Fury`, the bib item key would be `DoeFu20`. If there are two more authors on the paper, say `Wonder Woman` and `Bat Man`, the key would be `DFWM20`. 

## Steps for updating `ccg.bib`
`ccg.bib` is generated by a dynamic script from the CCG website backend. The most up to date version is served at https://cogcomp.seas.upenn.edu/bib/ccg.bib. Once every month,  the latest version of ccg.bib will be updated to this repo automatically from the CCG website. If you ever find `ccg.bib` out of sync, please drop Sihao or Jen an email. 

## Steps for merging your `new.bib` to `cited.bib`
After your paper gets published, we need to update `cited.bib` to include all new citations you made in your paper. Here's how to approach this. 

1. Convert your `new.bib` file to the CCG format with the [conversion tool].(https://github.com/CogComp/ccg-bibfiles/tree/master/ccg_bib_converter). Check the sub-folder readme for detailed steps. 

2. Merge `new.bib` into `cited.bib`

       either by copy-paste or the "cat" command

3. Import `cited.bib` to JabRef software (included in the repo). Generate the correct bib entry keys and sort them by year via the software.

4. (Optional) Generate `cited-recent.bib`, `cited-recent-long.bib`, `cited-recent-compact.bib` from the updated `cited.bib`. These are needed in case `cited.bib` contains too many entries, and sometimes leads to problems with the TeX compiler.  

- *To generate cited-recent.bib*: In JabRef, select all entries after year 2004 (2004 included) and make a copy
- Run script genCitedConference.sh to generate both long and compact bib files
