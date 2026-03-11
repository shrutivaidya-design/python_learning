
#return - if you want the result of the function to be reused later in the program use return instead of print
#Assign the return value - Assign function call to the variable to store the result 

def clean_name(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
    return cleaned

cln_name=clean_name("Kumar")

print(cln_name)



def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned,up_cleaned

l_clean,u_clean=clean_name("Arya")
print(l_clean)
print(u_clean)

