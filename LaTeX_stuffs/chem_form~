#!/usr/bin/perl
use strict;
use warnings;

#############################################
# A program to replace common matches of words in the list and replaces them with their counterparts
# It also corrects any chemical formulae into the corresponding capitalised and subscripted froms
# Dan Ellis 2016
#############################################

#note case insensetive.
my @find_list   = ( 'co'  , 'no'  , 'oh'  , 'mcm',   'nox'   ,    );
my @replace_l   = ( '$CO$', '$NO$', '$OH$', 'MCM', '$NO_{\times}$',  );

my @ignore_list = ( 'YO10', '5DD',  );





local $^I   = '.bak';              # emulate  -i.orig  # makes a backup
local @ARGV = glob("*.tex");       # read all tex files

sub parse_chem { 
    # parsing function
    s/(\w+)/\$\U${1}\$/;   
    s/([A-Z])(\d+)/${1}_\{${2}\}/ig;
    return;};



# loop through each file
foreach(@ARGV){
    #get file content
    my $content; {local $/=undef;  open FILE, $_ or die "Couldn't open file: $!"; $content = <FILE>;  close FILE;};
    #backup copy
    open my $backup, '>', ($_.'.backup') or die '$!'; print $backup $content; close $backup;
    
    $content =~ s/\h*\n\h*/ \n /gi;
    $content =~ s/,/ , /gi;
    #split into math and non math mode sections
    my @body = split(/\$/,$content); 
     
    #for non-math mode sections 
    my $index = 0;  foreach(@body){
        $index++; if ($index % 2 == 1){  
     
            #split into words  
            my @words = split(/\h+/,$_);    
            foreach(@words){

                if (m/http.*/ || m/www/ && !/.*\url.*/ ) {  
                    #hyperlink formatting
                    s/\b(.*)\h*\b/\{\\scriptsize\\textit\{\(\\url\{${1}\}\)\}\} /g;
                
                # is alphanumeric with no punctuation and measurement units
                }elsif ( /\d+/ && /\w+/ && !/.*[[:punct:]].*/ && !/\w*[mc]m/i && !/.*in/i  ) {  # if has digit, capitalise and enter mathmode
                    #print "\n+++",$_ , '---';
                    &parse_chem();
                };
          
            };
        
            $_ = join(' ',@words);        
            
        } 
     } 

      
    $content = join('$',@body) ;
    

    foreach (@ignore_list){ 
        my $retained = $_;
        &parse_chem();
        s/([\\\/\^\.\$\|\(\)\[\]\{\}\_\-])/\\${1}/g;
        $content =~ s/$_/$retained/ig ;
    }

    
    for(my $i = 0; $i<$#find_list +1 ; $i++){
        
        my $find = $find_list[$i];
        my $replace = $replace_l[$i];
        
        #post-process specific words
        $content =~ s/(\s)$find(\s)/${1}$replace${2}/ig ;
        
    }

    #print $content;
    $content =~ s/\h+,\h+/, /gi;    #fix commas
    print 'overwriting',$_,"\n";

    open my $file, '>', $_ or die '$!'; print $file $content; close $file;
      
    }




    


#while (<>) {} continue {close ARGV if eof} 
