password = str(input())
Special_Allowed = "!@#$%^&_*."
Special_notallowed = '''/\='" '''
pass_len = len(password)
if pass_len >= 8 and pass_len <= 32:
    Len_prop = True
    if Len_prop == True:
        Start_prop = password[0].isalpha()
        if Start_prop == True:
            alpha_pop = password.isalnum()
            if alpha_pop == True or alpha_pop == False:
                counter = 0
                final = True
                while counter < len(Special_notallowed):
                    Status = password.find(Special_notallowed[counter])
                    if Status > 0:
                        print("False")
                        final = False
                        break
                    else:
                        counter += 1
                if final == True :
                  print(final)
        else:
                print("False")               
else :
  print("False")