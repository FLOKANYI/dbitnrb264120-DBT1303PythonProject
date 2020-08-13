# Crime reporting system
# Desc - pseudocode - the crime victim reports a case and the system tracks the crime status
# DBITNRB264120
# Florence Kanyi

# Program start
username = input("kindly Log in using your username:")
verification = input("Enter your Password:")
verification = 'correct'
if verification == 'correct':
    print("Log in Successful")
elif verification != 'correct':
    print("Log in Failed!")
else:
    print("Try to Log in again")

#This response allows the victim to proceed to reporting the case
victim = input("Kindly proceed to report your case here:")
system = print("Am so sorry" +username + " for what has just happened to you.")
victim = input("kindly indicate your location so that the officers on duty may be notified:")
system = print("Officers on duty will be there shortly.")
print("Thank you" + username + "for alerting us.")
print("Your case is being followed.")
#the end
