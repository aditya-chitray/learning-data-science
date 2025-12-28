# for outputing stats bar
full_dot = '●'
empty_dot = '○'

# function for showing character stats
def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str): # str input check
        return 'The character name should be a string'
    if not name: # empty string check
        return 'The character should have a name' 
    if len(name)>10: # name not longer than 10 charc check
        return 'The character name is too long'
    if ' ' in name: # name should not have empty spaces
        return 'The character name should not contain spaces'

    if not (isinstance(strength,int) and isinstance(intelligence,int) and isinstance(charisma,int)):
        return 'All stats should be integers' #stats integer check

    if strength <1 or intelligence <1 or charisma <1:
        return 'All stats should be no less than 1' #no stat less than 1 check
    
    if strength >4 or intelligence >4 or charisma >4:
        return 'All stats should be no more than 4' # no stat GT than 4 check
    
    if strength+intelligence+charisma !=7:
        return 'The character should start with 7 points' #total sum of stats should be 4 at the start
    
    str_bar = full_dot * strength + empty_dot * (10 - strength)
    int_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_bar = full_dot * charisma + empty_dot * (10 - charisma)

    # generating output format
    result = name + "\n"
    result += "STR " + str_bar + "\n"
    result += "INT " + int_bar + "\n"
    result += "CHA " + cha_bar 


    return result

#function call
create_character('ren', 4, 2, 1)