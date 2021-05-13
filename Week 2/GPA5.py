name1, dob1, name2, dob2 = input(), input(), input(), input()

if (int(dob1[6:10])) > int(dob2[6:10]):
    print(name1)
elif (int(dob1[6:10])) < int(dob2[6:10]):
    print(name2)
else:
    if (int(dob1[3:5])) > int(dob2[3:5]):
        print(name1)
    elif (int(dob1[3:5])) < int(dob2[3:5]):
        print(name2)
    else:
        if (int(dob1[0:2])) > int(dob2[0:2]):
            print(name1)
        elif (int(dob1[0:2])) < int(dob2[0:2]):
            print(name2)
        else:
            if (name1 > name2):
                print(name2)
            else:
                print(name1)
