def sort_affirmations():
    """Sort affirmations into lists by beginnings: "I am, I'm", "Today", "My life", "I set", "I feel", "I accept"""

    f = open('data/affirmations.txt', encoding='UTF8')
    I_am = [] 
    I_m = []
    I_set = [] 
    I_feel = [] 
    I_accept = [] 
    Today = []
    My_life = [] 
    Other_affirmations = []
    for line in f:
        if line.startswith('I am'):
            I_am.append([line])
        elif line.startswith('I\m'):
            I_m.append([line])
        elif line.startswith('I set'):
            I_set.append([line])
        elif line.startswith('I feel'):
            I_feel.append([line])
        elif line.startswith('I accept'):
            I_accept.append([line])
        elif line.startswith('Today'):
            Today.append([line])
        elif line.startswith('My life'):
            My_life.append([line])
        else: 
            Other_affirmations.append([line])


    # fread = f.read()
    # print(fread)   
    print(I_am, I_m, I_set, I_feel, I_accept, Today, My_life)

sort_affirmations()
