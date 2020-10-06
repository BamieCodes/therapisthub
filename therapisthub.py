def collectEmail():
    email = input("Submit your email address to proceed: ")
    print("A mail has been sent to", email, "Kindly check your inbox!")
    
    
print('Hello, and welcome to Online doctor')

therapists = ['clinical', 'behavioural', 'occupational', 'cognitive', 'addiction', 'divorce', 'child']

print('\nWe have the following types of therapists:')

for therapist in therapists:
    print(therapist)

therapist_chosen = input('Ask for a therapist: ')
appointment_status = True

if appointment_status == True:
    print("A", therapist_chosen,"therapist has been alerted...!")
    collectEmail()



# for therapist in therapists:
#     
# Green_status = available to see you
# Red_status = not available, therefore cannot see you
# 
# 
# if Green_status:
#     print('check in with your doctor now')
# else:
#     print('Doctor unavailable to see you at the moment')
    