def tv_remote(words):
    #define starting conditions
    keyboard1 = ('abcde123',
                 'fghij456',
                 'klmno789',
                 'pqrst.@0',
                 'uvwxyz_/',
                 ('|', ' ', None, None, None, None, None, None))
    keyboard3 = ('^~?!\'"()',
                 '-:;+&%*=',
                 '<>€£$¥¤\\',
                 '[]{},.@§',
                 ('#', '¿', '¡', None, None, None, '_', '/'),
                 ('|', ' ', None, None, None, None, None, None))
    previous_x, previous_y = 0, 0
    previous_keyboard = 1
    words = list(words)
    char_no = 0
    presses = 0
    
    while char_no < len(words):
        char = words[char_no]
        
        #if shift is needed, add its symbol to list and skip to next iteration
        if char.isalpha() and char.islower() and previous_keyboard != 1:
            for i in range(4 - previous_keyboard):
                words.insert(char_no, '|')
            previous_keyboard = 1
            continue
            
        if char.isalpha() and char.isupper() and previous_keyboard != 2:
            if previous_keyboard == 1:
                previous_keyboard += 3
            for i in range(5 - previous_keyboard):
                words.insert(char_no, '|')
            previous_keyboard = 2
            continue
            
        if char.isdigit() and previous_keyboard == 3:
            words.insert(char_no, '|')
            previous_keyboard = 1
            continue
        
        if not char.isalnum() and char != '.' and char != '@' and char != '_' and char != '/' \
                              and char != '|' and char != ' ' and previous_keyboard != 3:
            for i in range(3 - previous_keyboard):
                words.insert(char_no, '|')
            previous_keyboard = 3
            continue
    
        #find the coordinates of the current character
        if previous_keyboard == 1 or previous_keyboard == 2:
            for row in range(len(keyboard1)):
                if char.lower() in keyboard1[row]:
                    y = row
                    x = keyboard1[row].index(char.lower())
                    break
        else:
            for row in range(len(keyboard3)):
                if char in keyboard3[row]:
                    y = row
                    x = keyboard3[row].index(char)
                    break
        
        presses += min(abs(x - previous_x), (8 - abs(x - previous_x))) + \
                   min(abs(y - previous_y), (6 - abs(y - previous_y))) + 1
        previous_x, previous_y = x, y
        char_no += 1
    
    return presses
