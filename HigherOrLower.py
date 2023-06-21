import random 
import os 

celebrities = [
                "Ariana Grande, American musician and singer.",
                "Selena Gomez, American musician and singer.",
                "Dwayne Johnson, American actor and former pro wrestler.",
                "Taylor Swift, American musician and singer.",
                "Katy Perry, American musician and singer.",
                "Nicki Minaj, American musician and singer.",
                "Rihanna, musician and singer from Barbados.",
                "Cristiano Ronaldo, Portuguese football player.",
                "Lionel Messi, Argentinian football player.",
                "Miley Cyrus, American musician and singer.",
               ] 


number_of_followers = {
    "Ariana Grande, American musician and singer." : 372,
    "Selena Gomez, American musician and singer." : 421,
    "Dwayne Johnson, American actor and former pro wrestler." : 384,
    "Taylor Swift, American musician and singer." : 264,
    "Katy Perry, American musician and singer." : 201,
    "Nicki Minaj, American musician and singer." : 221,
    "Rihanna, musician and singer from Barbados." : 151 ,
    "Cristiano Ronaldo, Portuguese football player." : 591,
    "Lionel Messi, Argentinian football player." : 470,
    "Miley Cyrus, American musician and singer." : 211,
}

artwork = """

 **      ** **   ********  **      ** ******** *******    
/**     /**/**  **//////**/**     /**/**///// /**////**   
/**     /**/** **      // /**     /**/**      /**   /**   
/**********/**/**         /**********/******* /*******    
/**//////**/**/**    *****/**//////**/**////  /**///**    
/**     /**/**//**  ////**/**     /**/**      /**  //**   
/**     /**/** //******** /**     /**/********/**   //**  
//      // //   ////////  //      // //////// //     //   
                                
 **         *******   **       ** ******** *******        
/**        **/////** /**      /**/**///// /**////**       
/**       **     //**/**   *  /**/**      /**   /**       
/**      /**      /**/**  *** /**/******* /*******        
/**      /**      /**/** **/**/**/**////  /**///**        
/**      //**     ** /**** //****/**      /**  //**       
/******** //*******  /**/   ///**/********/**   //**      
////////   ///////   //       // //////// //     //       

""" 

versus_artwork = """

 **      **    ********
/**     /**   **////// 
/**     /**  /**       
//**    **   /*********
 //**  **    ////////**
  //****            /**
   //**       ******** 
    //       ////////  

"""


def pick_celebrity():
    celebrity = random.choice(celebrities)
    celebrities.remove(celebrity)
    return celebrity 


def compare_followers(A, B):

    followers_A = number_of_followers.get(A)
    followers_B = number_of_followers.get(B)

    if followers_A > followers_B:
        return "A"
    else:
        return "B"
    
score = 0

def increment_score():
    global score
    score += 1
    return score

def game():

    print(artwork)
    celebrity_A = pick_celebrity()
    celebrity_B = pick_celebrity()

    print(f"Compare A: {celebrity_A} ")
    print(versus_artwork)
    print(f"Against B: {celebrity_B} ")

    user_guess = input("Who has more followers on Instagram? Type 'A' or 'B' : ").upper()
    if user_guess == compare_followers(celebrity_A, celebrity_B):
        
        print(f"That's correct! Current score: {increment_score()}")
        game()

    else:
        print(f"That's incorrect! Final score: {score}")
        return

game()