# Συνάρτηση Κρυπτογράφησης Καίσαρα.
def encrypt_ceasar(plain_text,key):

    cipher_text = ""

    for letter in plain_text:   

        # Μετατροπή του γράμματος σε αριθμό.
        # ( A = 0, B = 1, ... Z = 25 )
        num = ord(letter) - ord("A")

        # Δεξιά μετατόπιση του αριθμού κατά key θέσεις.
        met = ( num + key ) % 26

        # Μετατροπή του τελικού αριθμού σε γράμμα.
        # ( 0 = A, 1 = B, ... 25 = Z )
        ch = chr( met + ord("A"))

        # Το τελικό κείμενο προκύπτει από την προσθήκη των γραμμάτων.
        cipher_text = cipher_text + ch

    # Έξοδος από την συνάρτηση, επιστροφή του κρυπτογραφημένου κειμένου.
    return cipher_text

# Συνάρτηση Αποκρυπτογράφησης Καίσαρα.
def decryrt_ceasar(cipher_text,key):
    
    plain_text = ""
    
    for letter in cipher_text:

        # Μετατροπή του γράμματος σε αριθμό.
        num = ord (letter) - ord("A")

        # Αριστερή μετατόπιση του αριθμού κατά key θέσεις. 
        met = ( num - key ) % 26 

        # Μετατροπή του τελικού αριθμού σε γράμμα.
        ch = chr( met + ord("A"))

        # Το τελικό κείμενο προκύπτει από την προσθήκη των γραμμάτων στην κενή λίστα.
        plain_text  = plain_text + ch

    # Έξοδος από την συνάρτηση, εμφάνιση του αποκρυπτογραφημένου κειμένου.
    return plain_text

# Συνάρτηση Κρυπτογράφησης Βιζενέρ.
def encrypt_vigenere(plain_text,key):

    cipher_text=""

    # Η θέση του γράμματος από την λέξη κλειδί.
    pos = 0

    for letter in plain_text:       

        # Μετατροπή του γράμματος σε αριθμό.
        # ( A = 0, B = 1, ... Z = 25 )
        num = ord(letter) - ord("A")
        
        # Μετατόπιση του αριθμού σύμφωνα με τον πίνακα Vigenere και την λέξη κλειδί.
        met = ord( key [ pos % len( key )] ) - ord("A")
        
        # Μετατροπή του τελικού αριθμού σε γράμμα.
        ch = chr(( num + met ) % 26 + ord("A"))
        
        # Το τελικό κείμενο προκύπτει από την προσθήκη των γραμμάτων στην κενή λίστα.
        cipher_text = cipher_text + ch

        # ...
        pos = pos + 1

    # Έξοδος από την συνάρτηση, εμφάνιση του κρυπτογραφημένου κειμένου στην κενή λίστα.
    return cipher_text

# Συνάρτηση Αποκρυπτογράφησης Βιζενέρ.
def decrypt_vigenere(cipher_text,key):

    new_text = ""

    # Η θέση του γράμματος στην λέξη κλειδί με την οποία θα γίνει η κρυπτογράφηση.   
    pos = 0
        
    for letter in cipher_text:

        # Μετατροπή του γράμματος σε αριθμό.
        # ( A = 0, B = 1, ... Z = 25 )
        num = ord(letter) - ord("A")

        # Μετατόπιση του αριθμού σύμφωνα με τον πίνακα Vigenere και την λέξη κλειδί.
        met = ord( key [ pos % len( key ) ] ) - ord('A')

        # Μετατροπή του τελικού αριθμού σε γράμμα.
        ch = chr( ( num - met ) % 26 + ord("A") )

        # Το τελικό κείμενο προκύπτει από την προσθήκη των γραμμάτων στην κενή λίστα.
        new_text= new_text + ch

        # ...
        pos= pos+1

    # Έξοδος από την συνάρτηση, εμφάνιση του κρυπτογραφημένου κειμένου στην κενή λίστα.
    return new_text

# Ο χρήστης επιλέγει έναν από τους 2 κώδικες (Καίσαρα, Βιζενέρ)

choice_1 = input("Για τον αλγόριθμο του Καίσαρα πλήκτρολογήστε C και για τον αλγόριθμο του Βιζενέρ V:  ")
choice_1 = choice_1.upper()

while choice_1 != "C" and choice_1 != "V" :

    choice_1 = input("Πρέπει να πληκτρολογήσετε ένα από τα 2 γράμματα (C-για Καίσαρα, V-για Βιζενέρ.):  ")
    choice_1 = choice_1.upper()
    
# Εφόσον ο χρήστης επιλέξει τον αλγοριθμο του Καίσαρα έχει την επιλογή κρυπτογράφσης και αποκρυπτογράφησης.
if choice_1 == "C" :

     
    choice_2 = input("Για κρυπτογράφηση πληκτρολογήστε Ε και για αποκρυπτογράφηση D:  ")
    choice_2 = choice_2.upper()

    while choice_2 != "E" and choice_2 != "D" :

        choice_2 = input("Πρέπει να πληκτρολογήσετε ένα από τα 2 γράμματα (E-για κρυπτογράφηση, D-για αποκρυπτογράφηση.):  ")
        choice_2 = choice_2.upper()

        
    if choice_2 == "E" :

        
        text = input("Πληκτρολογήστε το κείμενο που θέλετε να κρυπτογραφήσετε: ")
        text = text.upper()

        while text.isalpha() == False :
            print("Το κείμενο προς κρυπτογράφηση πρέπει να αποτελείται από γράμματα του αγγλικού αλφαβήτου.")
            text = input("Πληκτρολογήστε ξανά σωστά το κείμενο:  ")    
        
        
        key = input("Πληκτρολογήστε έναν αριθμό κλειδί: ")
        
        while not key.isdigit() :

            print("Το κλειδί πρέπει να είναι αριθμός")

            key = input("Πληκτρολογήστε ξανά έναν αριθμό κλειδί:  ")

        key = int(key)
        
        cipher_ceasar = encrypt_ceasar(text,key)

        print("Το κρυπτογραφημένο κείμενο είναι: ",cipher_ceasar)
                  
    
    elif choice_2 == "D" :

        cipher_text = input("Πληκτρολογήστε το κείμενο που θέλετε να αποκρυπτογραφήσετε: ")

        key = input("Πληκτρολογήστε τον αριθμό κλειδί που χρησιμοποιήθηκε: ")

        while not key.isdigit() :

            print("Το κλειδί πρέπει να είναι αριθμός")

            key = input("Πληκτρολογήστε ξανά τον αριθμό κλειδί που χρησιμοποιήθηκε:  ")

        key = int(key)
        

        dcipher_ceasar = decryrt_ceasar(cipher_text,key)

        print("Το αποκρυπτογραφημένο κείμενο είναι: ", dcipher_ceasar)
        

elif choice_1 == "V" :

    choice_2 = input("Για κρυπτπγράφηση πληκτρολογήστε Ε και για αποκρυπτογράφηση D:  ")
    choice_2 = choice_2.upper()


    while choice_2 != "E" and choice_2 != "D" :

            choice_2 = input("Πρέπει να πληκτρολογήσετε ένα από τα 2 γράμματα (E-για κρυπτογράφηση, D-για αποκρυπτογράφηση.):  ")
            choice_2 = choice_2.upper()

    if choice_2 == "E" :
        text = input("Πληκτρολογήστε ένα κείμενο για κρυπτογράφηση:  ")
        text = text.upper()

        while text.isalpha() == False :
            print("Το κείμενο προς κρυπτογράφηση πρέπει να αποτελείται από γράμματα του αγγλικού αλφαβήτου.")
            text = input("Πληκτρολογήστε ξανά σωστά το κείμενο:  ")

        key = input("Πληκτρολογήστε μία λέξη κλειδί για την μετατόπιση:  ")

        while key.isalpha() == False:

            print("Η λέξη κλειδί πρέπει να αποτελείται αποκλειστικά απο χαρακτήρες του λατινικού αλφαβήτου.")

            key = input("Πληκτρολογήστε ξανά την λέξη κλειδί:  ")
        
        key = key.upper()

        cipher_vigenere = encrypt_vigenere(text,key)

        print("Το κρυπτογραφημένο κείμενο είναι: ", cipher_vigenere)

    elif choice_2 == "D" :
        cipher_text = input("Πληκτρολογήστε το κείμενο που θέλετε να αποκρυπτογράφησετε:  ")

        cipher_text = cipher_text.upper()

        key = input("Πληκτρολογήστε την λέξη κλειδί που χρησιμοποιήθηκε για την μετατόπιση:  ")

        while key.isalpha() == False:

            print("Η λέξη κλειδί πρέπει να αποτελείται αποκλειστικά απο χαρακτήρες του λατινικού αλφαβήτου:  ")

            key = input("Πληκτρολογήστε ξανά την λέξη κλειδί:  ")        
        
        key = key.upper()

        decrypt_vigenere = decrypt_vigenere(cipher_text,key)

        print("Το κρυπτογραφημένο κείμενο είναι: ", decrypt_vigenere)

        
    
