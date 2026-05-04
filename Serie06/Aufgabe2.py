x = 2

def outer():
    x = 3

    def inner():
        def innermost():
            global x # vergiss alle x und nimm das globale
            return x 

        print(x) # outer's x (Enclosing)
        print(innermost()) # globales x, via global Keyword
        print(x)
        
    inner()
outer()

