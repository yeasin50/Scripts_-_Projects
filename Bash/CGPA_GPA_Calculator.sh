
#Testing purp. for each input
# CGPA According CGPA 
# GPA accodoing SSC and JSC BD
cgpa () {
    # gets mark as parameter assign on positonal argument $1
    r="   Avarage CGPA grade:"
    if [ $1 -gt 100 ]; then echo "Invalid Operation.Mark cannt over 100"
    elif [ $1 -gt 79 ]; then echo "$r A+"
    elif [ $1 -gt 74 ]; then echo "$r A"
    elif [ $1 -gt 69 ]; then echo "$r A-"
    elif [ $1 -gt 64 ]; then echo "$r B+"
    elif [ $1 -gt 59 ]; then echo "$r B"
    elif [ $1 -gt 54 ]; then echo "$r B-"
    elif [ $1 -gt 49 ]; then echo "$r C+"
    elif [ $1 -gt 44 ]; then echo "$r C"
    elif [ $1 -gt 39 ]; then echo "$r D"
    else printf "You have failed dude, Keep it up\n Next time you gonna Do Great\n"

fi
}


# get grade
cgpa_Grade () {
    # gets mark as parameter assign on positonal argument $1
    grade=0
    if [ $1 -gt 100 ]; then echo "Invalid Operation.Mark cannt ov"
    elif [ $1 -gt 79 ];then  grade=4.0
    elif [ $1 -gt 74 ]; then  grade=3.75
    elif [ $1 -gt 69 ]; then  grade=3.50
    elif [ $1 -gt 64 ]; then  grade=3.25
    elif [ $1 -gt 59 ]; then  grade=3.00
    elif [ $1 -gt 54 ]; then  grade=2.75
    elif [ $1 -gt 49 ]; then  grade=2.50
    elif [ $1 -gt 44 ]; then  grade=2.25
    elif [ $1 -gt 39 ]; then  grade=2.00
    else echo  "You have failed  according CGPA"

fi
}


# get grade letter
cgpa_Grade_Letter () {
    # gets mark as parameter assign on positonal argument $1
    cgpa_letter="0"

  if (( $(echo "$1 > 4.0" |bc -l) )); then echo "overLoaded : >4.0"
  elif (( $(echo "$1 > 3.75" | bc -l) )); then cgpa_letter="A+"
  elif (( $(echo "$1 > 3.50" | bc -l) )); then cgpa_letter="A"
  elif (( $(echo "$1 > 3.25" | bc -l) )); then cgpa_letter="A-"
  elif (( $(echo "$1 > 3.00" | bc -l) )); then cgpa_letter="B+"
  elif (( $(echo "$1 > 2.75" | bc -l) )); then cgpa_letter="B"
  elif (( $(echo "$1 > 2.50" | bc -l) )); then cgpa_letter="B-"
  elif (( $(echo "$1 > 2.25" | bc -l) )); then cgpa_letter="C+"
  elif (( $(echo "$1 > 2.00" | bc -l) )); then cgpa_letter="C"
  elif (( $(echo "$1 > 2.25" | bc -l) )); then cgpa_letter="D"
  else echo  "You have failed  according CGPA"

fi
}
# return grade
gpa_Grade () {
    # gets mark as parameter assign on positonal argument $1
    Ggrade=0
    if [ $1 -gt 100 ]; then echo "Invalid Operation.Mark cannt ov"
    elif [ $1 -gt 79 ];then  Ggrade=5.0
    elif [ $1 -gt 69 ]; then  Ggrade=4.0
    elif [ $1 -gt 59 ]; then  Ggrade=3.50
    elif [ $1 -gt 49 ]; then  Ggrade=3.0
    elif [ $1 -gt 39 ]; then  Ggrade=2.00
    elif [ $1 -gt 32 ]; then  Ggrade=1.00
    else echo  "You have failed according GPA"

fi
}

#Gpa
gpa () {
    # gets mark as parameter assign on positonal argument $1
    r="    Avarage GPA (Letter):"
    if [ $1 -gt 100 ]; then echo "Invalid Operation.Mark cannt over 100"
    elif [ $1 -gt 79 ]; then echo "$r A+"
    elif [ $1 -gt 69 ]; then echo "$r A"
    elif [ $1 -gt 59 ]; then echo "$r A-"
    elif [ $1 -gt 49 ]; then echo "$r B"
    elif [ $1 -gt 39 ]; then echo "$r C"
    elif [ $1 -gt 54 ]; then echo "$r D-"
    else printf "$r F\n  You have failed dude, Keep it up\n Next time you gonna Do Great\n"

fi
}



#reset 
reset () {
    input=0
    total_marks=0
    counter=0
    avg_mark=0

    avg_cgpa=0.0
    total_cgpa=0.0

    avg_gpa=0.0
    total_gpa=0.0

    clear
    echo "Dataset-> Default"
    echo "help -h , result -r"
    echo ""
}

help () {
  echo ""
  echo " Mark Range should  be 0 to 100"
  echo " Enter h for help"
  echo " Enter q to Quit the script"
  echo " Enter d to reset value/ delete previous values"
  echo " Enter r to see the result"
  echo " "
}

#init values 
reset 

while true
do 
read v
if [[ "$v" == 'q' ]];then
  echo " exit 0"
	break

elif [[ "$v" == 'h' ]]; then help 
elif [[ "$v" == 'd' ]] ; then reset

elif [[ "$v" == 'r' ]]; then
    echo ""
    echo "    Total Mark: $total_marks  Courses: $counter "
    avg_mark=`echo 'scale=2;' $total_marks / $counter | bc -l`
    echo "    Avg mark $avg_mark"

#  CGPA calcu.
    echo ""
    avg_cgpa=`echo 'scale=2;' $total_cgpa / $counter | bc -l`
    cgpa_Grade_Letter $avg_cgpa 
    echo "    Avarage CGPA (Point) : $avg_cgpa "
    echo "    Avarage CGPA (Letter): $cgpa_letter"
    # cgpa $(( total_marks/ counter)) # avg in grade


# GPA calcu:
    echo ""
    avg_gpa=`echo 'scale=2;' $total_gpa / $counter | bc -l`
    echo "    Avarage GPA (Point) : $avg_gpa"
    gpa $(( total_marks/ counter)) # avg in grade


    #reset req
    echo ""
    echo "press d to reset value"
    echo ""
# elif [ "$v" -gt 100 ]; then echo "Out of range num<=100"
# elif [ "$v" -lt 0 ]; then echo "To small, num>=0"

elif [ "$v" -ge 0 -a "$v" -le 100 ];
 then 
 total_marks=$(( $total_marks + $v ))
      ((counter++))
        # echo "$total_marks $counter "
      cgpa_Grade $v
      total_cgpa=`echo 'scale=2;' $total_cgpa + $grade | bc -l`
      
      gpa_Grade $v
      total_gpa=`echo 'scale=2;' $total_gpa + $Ggrade | bc -l`

else echo " invalid Input, enter h for help"

fi
done
