gpaOne=4
gpaTwo=3
gpaThree=2

creditsOne=6
creditsTwo=5
creditsThree=1

totalCredits = creditsOne+creditsTwo+creditsThree

weightedOne=gpaOne*creditsOne
weightedTwo=gpaTwo*creditsTwo
weightedThree=gpaThree*creditsThree

totalWeighted=weightedOne+weightedTwo+weightedThree

finalGPA=round(totalWeighted/totalCredits,2)
#print(finalGPA)

print ('Your GPA is: ',finalGPA)

# launch IDLE and run this file
# explain comments
# fix the error
# add line numbers
# better print line (concatenate it)
# round the result
# re-organize my code

# a # can help you comment things out if you dont want a line to run but don't want to delete it.

