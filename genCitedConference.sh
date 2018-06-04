#Only apply incremental changes and de-duplicate using the jar
cat full_head.bib cited.bib > cited-long.bib
rm cited-compact.bib
nice perl shorten.pl cited.bib > cited-compact.bib.tmp
cat compact_head.bib cited-compact.bib.tmp > cited-compact.bib
rm cited-compact.bib.tmp

cat full_head.bib cited-recent.bib > cited-recent-long.bib
rm cited-recent-compact.bib
nice perl shorten.pl cited-recent.bib > cited-recent-compact.bib.tmp
cat compact_head.bib cited-recent-compact.bib.tmp > cited-recent-compact.bib
rm cited-recent-compact.bib.tmp

cat full_head.bib ccg.bib > ccg-long.bib
rm ccg-compact.bib
nice perl shorten.pl ccg.bib > ccg-compact.bib.tmp
cat compact_head.bib ccg-compact.bib.tmp > ccg-compact.bib
rm ccg-compact.bib.tmp
