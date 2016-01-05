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
    
    open(my $fh, "<", $arg) or die "$!";

    @new = split(/\./,$arg);
    open(my $write, ">", $new[0].".ropa") or die "$!";


    while( <$fh> ) {
        s/\!/,/g;
        s/\s+//g;
        chop($_); #rm last 

        if ($. > 1) { 
             if($_ !~ m/(\d.\d{16}E[+-]\d{3}\,{0,1}){$len}/g){
                for $individual (split(/,/,$_)){ 

                    if ($individual !~ m/\d.\d{16}E[+-]\d{3}\,{0,1}/){
                        
                        if ($individual !~ m/E/ ) { 
                        
                           $individual =~ m/[+-]{0,1}\d+[+-]/;
                          
                           my $pos = $+[0] - 2 ; 
                           $individual =~ s/^(.{$pos})./$1E/; 
                           print $write $individual ;
                           # change the 6th character in string - The reason for the 5 : 6 -1 between {}. The first "^" means the the beginning of the string and the second with the backslash before means the character "^" and not the beginning of the string like the first one.
                        }
                    }             
                 }
             }else{            
                print $write $_ . "\n";
                       
             }
             
        }else{ # if headers
            $data = $_ ;
            @array = split(/,/, $data) ;
            $len=$#array + 1;
            print $write $_ . "\n";
        }     
        
    }
    close $fh or die "Error in closing the file ", __FILE__, " $!\n";
    close $write or die "Error in closing the file ", __FILE__, " $!\n";

print "Made ".$arg.".ropa";
}

