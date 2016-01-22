############################################################################################################################
#Program to easily remove jobs from the queing system, as on earths case, qdel -u <user> does not work
# chmod a+x filename and run normally (./file) or use 'perl filename'
#Author:  D.Ellis   Date:  #Jan 2016
############################################################################################################################

use 5.6.0;
use strict;
use Term::ANSIColor;


#########################
## Enter username here ##
my $line=`qstat -u dp626`;
#########################

my @output = split("\n",$line) ;
my $randm;
#entry write to screen
print color("red"), "To delete task: enter number, or 'A' for all. \n", color("reset");

#read all current jobs and parse
for my $i (0 .. $#output){
    if ($i > 4) { #skip detail lines
      print "# " . color("green"), sprintf("%02d",$i-4) , color("reset"), "    $output[$i] \n" ;
    } else { 
        print color("red"), $output[$i]."\n", color("reset");
    }
}

print color("red"), "\n Enter input here: \n", color("reset");

## on Tomas' suggestion: Worms references.         
my $input = <>;

if ($input eq "A\n") { 
        my @message = ( "Kamikaze!", 
                        "Exterminate",
                        "Prepare to die, tasklings! ",  
                        "Aren't we such a superior race?",
                        "Y'wee buzzar!  ",  
                        "Court is adjorned!"   );
                    
        $randm = $message[ rand @message ]; #random message
        print $randm."\n";
        
        #do for all jobs. 
        for my $j (4 .. $#output){
            $output[$j] =~ s/(\d*).*/$1/  ;
            system("qdel $output[$j]") ; 
               
        }   


}elsif ( ($input) > 0 and ($input) < ($#output)-3 ) { #check if within allowed range
       
       $input = $input+4; #correct array 
        
       my @message = ( "What the heck Grenades, because life is full of surprises!",
                       "Just what the doctor ordered! ",
                       "Fire Punch, made from real Dragon Scales! For a smokin' punch.",
                       "Victory! The winner's choice! ",
                       "Quitter Time patches, for quitters who win in the end",
                       "Get that hammer.",
                       "Target eliminated"  );
                            
       $randm = $message[ rand @message ];
      
       print $randm."\n";
        
       $output[$input] =~ s/(\d*).*/$1/  ;
       system("qdel $output[$input]") ;


}else{ #picks up pieces for incorrect entries
     my @message = ( "Incorrect Input! Panic! Run Away!",
        "This wasn't in the battle plan",
        "This won't help with the destruction of the planet.",
        "You want this planet or not?",
        "Stop looking at the ultra-violet rays, and get on with the job!",
        "Yawwnn"     );
        
        $randm = $message[ rand @message ];
        
        die "$randm \n"; #kills program
}
        
        
        
        
