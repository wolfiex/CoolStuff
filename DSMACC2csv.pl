#!/usr/bin/perl
#use strict;
use warnings;

## Parses the Spec and rate files from the DSMACC model into csv-style files that can be read into pandas with read_csv. 
# chmod a+x the file, then run with files as arguments  
# can use multiple files:     ./csv_to_DSMACC.pl *.dat
# creates        .ropa       file with inital filename 
####################### Dan Ellis ####################

my $data;
my $len;
my $individual;
for my $arg (@ARGV) {
    my $write = "";
    open(my $fh, "<", $arg) or die "$!";

    @new = split(/\./,$arg);
    open(my $writefile, ">", $new[0].".ropa") or die "$!";


    while( <$fh> ) {

        s/\!/,/g;
        s/\s+//g;
        chop($_); #rm last 

        #print $_;
        if ($. > 1) { 
            
                $_ =~ s/(\d)([+-]\d)/$1E$2/g;     

        }
        $write .="$_\n";
      
    }

    print $writefile $write;
    close $fh or die "Error in closing the file ", __FILE__, " $!\n";
    close $writefile or die "Error in closing the file ", __FILE__, " $!\n";

    print "Made ".$arg.".ropa";
}

