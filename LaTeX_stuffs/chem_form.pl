#!/usr/local/bin/perl
use strict;
use warnings;


#############################################
# A program to replace common matches of words in the list and replaces them with their counterparts
# It also corrects any chemical formulae into the corresponding capitalised and subscripted froms
# Dan Ellis 2016
#############################################

#note case insensetive.
my @find_list   = ( 'co'  , 'no'  , 'oh'  , 'mcm', 'nox'   ,   );
my @replace_l   = ( '$CO$', '$NO$', '$OH$', 'MCM', 'NO_{x}',   );





local $^I   = '.bak';              # emulate  -i.orig  # makes a backup
local @ARGV = glob("*.tex");       # read all tex files


foreach(@ARGV){
    #get file content
    my $content; {local $/=undef;  open FILE, $_ or die "Couldn't open file: $!"; $content = <FILE>;  close FILE;};
    #split into math and non math mode sections
    my @body = split(/\$/,$content); 
     
    #for non-math mode sections 
    my $index = 0;  foreach(@body){
        $index++; if ($index % 2 == 1){  
     
            #split into words  
            my @words = split(/\h+/,$_);    
            foreach(@words){
                
                if (m/\d/ ) {  # if has digit, capitalise and enter mathmode
                
                s/([0-9a-zA-Z]+)/\$\U${1}\$ /g;    
                s/(.*)(\$\s+)(.*)/${1}\$${3}/g;
                s/([A-Z])(\d+)/${1}_\{${2}\}/g;
                
                };
          
            };
        
            $_ = join(' ',@words);        
            
        } 
     } 

      
    $content = join('$',@body) 
    
    
    
    for(my$i = 0; $i<=$#find_list; $i++){
    
    my $find = $find_list[$i];
    my $replace = $replace_l[$i];
    
    #post-process specific words
    $content =~ s/\b$find\b/$replace/gi 
    
    }
    
    print 'overwriting',$_,'\n';

    open my $file, '>', $_ or die '$!'; print $file $content; close $file;
      
      
    }



#while (<>) {} continue {close ARGV if eof} 

    
