Backtracking


https://www.youtube.com/watch?v=I081UkZCLlc&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=72


_____________
Backtracking basic idea:
        
SO backtracking is basically trial and error method and that we explore all possible solution one by one

We start with an empty solution and try to add elements to it one by one. If at any point we realize that the current solution cannot lead to a valid solution, we backtrack and try a different approach.     
        

                                             ________________
                                            |                |
                                            |   decision     |
                                            |    tree        |
                                            |                |
                                            ----------------

                                            
example:            
                 
                 
                 
                        "A"
                    /      \ 
                   /        \ 
                 "AA"       "AB"
               /   \        /   \
              /     \      /     \
            "AAA"   "AAB" "ABA" "ABB"
            ...     