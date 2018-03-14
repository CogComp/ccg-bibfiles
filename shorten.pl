#!/bin/perl

die("Need a bib file") if($#ARGV + 1 != 1);

$file = $ARGV[0];

@fields = ('volume', 'pages', 'number', 'address', 'url', 'location',
'publisher', 'month', 'isbn', 'doi');

@capfields = ();
for $field(@fields)
{
    push @capfields, uc $field;
    push @capfields, ucfirst $field;
}


open FILE, $file or die ($!);

for $line(<FILE>)
{
    for $field(@fields)
    {
	$line =~s/^[ \t]*$field[ \t]*=/$field-omit =/g;
    }
    for $field(@capfields)
    {
	$line =~s/^[ \t]*$field[ \t]*=/$field-omit =/g;
    }
    # $line=~s/volume[ \t]*=/volume-omit =/g;
    # $line=~s/pages [ \t]*=/pages-omit =/g;
    # $line=~s/number [ \t]*=/number-omit =/g;
    # $line=~s/address[ \t]*=/address-omit =/g;
    # $line=~s/url [ \t]*=/url-omit =/g;
    # $line=~s/url [ \t]*=/url-omit =/g;
    # $line=~s/location [ \t]*=/location-omit =/g;
    # $line=~s/publisher [ \t]*=/publisher-omit =/g;
    # $line=~s/month [ \t]*=/month-omit =/g;
    # $line=~s/isbn [ \t]*=/isbn-omit =/g;
    # $line=~s/doi [ \t]*=/doi-omit =/g;
    print $line;
}

close FILE;
