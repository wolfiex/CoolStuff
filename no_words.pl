#Adapted from somewhere on the internet
#Userful for seeing what words/combinations appear most in programs 
#and simplifing these. 


print "Type the name of the file: ";
# read from cmd
chomp(my $file = <>);
open (FILE, "$file") or die;


while (<FILE>){
     #add up occurances for split in metacharacter (letters)
     $seen{$line}++ ;
     #add up occurances for split in metacharacter (letters)
     $seen{$_}++ for split /\W+/;
}
     
printf $line, '\n';

my $count = 0;
for (sort {
     #sort by most occured    
    $seen{$b} <=> $seen{$a}
              || #or
       lc($a) cmp lc($b)
              || #or
          $a  cmp  $b
} keys %seen)

{
    next unless /\w/;
    printf "%-20s %5d\n", $_, $seen{$_}; 
    last if ++$count > 10;
}
close (FILE)
