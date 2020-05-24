
"""
    This programm allows the user to create and interact with a pet.
    The interaction with the pet is based on the following commands 
    'drink','shower','sleep','status', 'play' and 'feed'. If status is 
    selected, a table is displayed for the user.
"""



from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]
hunger_lst=[]
drink_lst=[]





class Pet(object):
    '''
    This class is responsable for the activities ('drink','shower','sleep','feed')
    the pet can do. It is also responsable for the pets response, and status
    
    '''
    
  
    
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
        '''
        This method is responsible for the creation of the object from the class pet
        that at its default is a dog called fluffy, of male gender and has white fur
        In this method the the specificatios for the values of hunger
        thirst, smell , loneliness, energy and initial response 'newborn' are set.
        '''
        # modify the following code
        
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = hunger_lst   
        self._drinkable_items = drink_lst 

        self._hunger = randint(0,5)
        self._thirst =randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy = randint(5,10)

        self._reply_to_master('newborn')

    def _time_pass_by(self, t=1):
        
        # this function is complete
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    def get_hunger_level(self):
        '''
        This method will return the valeu of the created object,
        it refers to the instance  
        Value: instance whose method was called
        Returns: valeu of the instance
        '''
	
        return self._hunger


    def get_thirst_level(self):
        '''
        This method will return the valeu of the created object,
        it refers to the instance  
        Value: instance whose method was called
        Returns: valeu of the instance
        '''
        return self._thirst

    def get_energy_level(self):
        
        '''
        This method will return the valeu of the created object,
        it refers to the instance  
        Value: instance whose method was called
        Returns: valeu of the instance
        '''
	
        return self._energy
    
    
    
    def drink(self, liquid):
        
        '''
            This method makes use of the created object,
            instance to set up the the pet behaviour related to drinking.
            In this method the valeu that discribe when the pet is thirst and
            the max valeu for thirst is defined.
            The method keep track the amount of liquid to reduce the thrist amount.
            It calls the reply_to_master method to send the pet message related to
            drink. And calls update status for a message related to its current status.
        '''
    
    
        if isinstance(liquid, tuple(self._drinkable_items)):
            
            self._time_pass_by()
                
            my_liq = int(liquid.get_quantity())

            
                
            if self._thirst >= 2:
                
                self._thirst = self._thirst - my_liq
                
                if self._thirst < 0 : 
                    self._thirst = 0
                    
                    
                self._reply_to_master(event = 'drink')
                    
                    
            else:
                
                print('Your pet is satisfied, no desire for sustenance now.')

        else:
            
            print("Not drinkable")
                    
        self._update_status()
        
        

    def feed(self, food):
        
        '''
            This method makes use of the created object,
            instance to set up the the pet behaviour related to hunger
            In this method the valeu that discribe when the pet is hungry and
            the max valeu for thist is defined.
            The method keep track the amount of food to reduce the hunger amount.
            It calls the reply_to_master method to send the pet message related to
            feed. And calls update status for a message related to its current status.
        '''
        
        if isinstance(food, tuple(self._edible_items)):
            
            self._time_pass_by()
                
            my_liq = int(food.get_quantity())

            
                
            if self._hunger >= 2:
                
                self._hunger  = self._hunger  - my_liq
                
                if self._hunger  < 0 : 
                   self._hunger = 0
                    
                    
                self._reply_to_master(event = 'feed')
                    
                    
            else:
                
                print('Your pet is satisfied, no desire for sustenance now.')

        else:
            
            print("Not edible")
                    
        self._update_status()


    def shower(self):
        
         '''
            This method makes use of the created object,
            instance to set up the the pet behaviour related to shower
            In this method the valeu that discribes when the pet smell is set to zero.
            But the loneliness levels drops depending on the time. This method sets
            The valeu of loneliness to never go less then zero.
            It calls the reply_to_master method to send the pet message related to
            shower. And calls update status for a message related to its current status.
         '''
         
         t = 4
         self._time_pass_by(t)
         self._smell = 0
         

         # prevent that loneliness is never lower then 0
         
         if self._loneliness - t < 0 :
             
             self._loneliness = 0
             
         else:
             self._loneliness = self._loneliness - t
             
         self._reply_to_master(event = 'shower')
         
         self._update_status()
         
            


    def sleep(self):
	
        '''
            This method makes use of the created object,
            instance to set up the the pet behaviour related to sleep
            In this method the valeu that discribe when the pet is sleepy and
            the max valeu for energy is defined.
            It calls the reply_to_master method to send the pet message related to
            sleep. And calls update status for a message related to its current status.
            
        '''
    
    
        
        t = 7
         
        self._time_pass_by(t)
      
        # prevent the energy to never be greater then 10
        
        if self._energy + t > MAX :
             
             self._energy = MAX
        else:
            self._energy = self._energy + t 
             
             
        self._reply_to_master(event = 'sleep')
             
        self._update_status()
         


    def play_with(self):
        
        
        '''
            In this method the behaviours on how the loneliness, smell, and energy, change 
            over time when the pet plays are set.
            It calls the reply_to_master method to send the pet message related to
            playing, and calls update status for a message related to its current status.
            
        '''
    
        t = 4
        
        # intances are affected by the defined time
        
        self._time_pass_by(t)
        self._energy = self._energy - t
        self._loneliness = self._loneliness - t
        self._smell = self._smell + t
        
            
        if self._loneliness < 0 :
            
            self._loneliness = 0
         
            
            
        if self._smell > MAX:
            self._smell = MAX
           
            
            
        if self._energy < 0:
            self._energy = 0
          
            
        self._reply_to_master(event = 'play')    
        self._update_status()
         
    
    def _reply_to_master(self, event='newborn'):
        
        
        '''
            Reply_to_master method prints the pet message related to a specifed event
        '''
        
        # this function is complete #
        
        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event]
        print(s)

    def show_status(self):
        
        '''
            This method makes use of the created object,
            instance to create a table displaying the levels of 
            energy, hunger, loneliness, smell and thirst
            
        '''
        
        
        
        s0 = "{:<12s}: [{:<20s}]".format('Energy', '#'*(2*int(round(self._energy)))) + "{:5.2f}/{:2d}".format(self._energy, MAX)  
        s1 = "{:<12s}: [{:<20s}]".format('Hunger', '#'*(2*int(round(self._hunger)))) + "{:5.2f}/{:2d}".format(self._hunger, MAX)  
        s2 = "{:<12s}: [{:<20s}]".format('Loneliness', '#'*(2*int(round(self._loneliness)))) + "{:5.2f}/{:2d}".format(self._loneliness, MAX)
        s3 = "{:<12s}: [{:<20s}]".format('Smell', '#'*(2*int(round(self._smell))))+ "{:5.2f}/{:2d}".format(self._smell, MAX)      
        s4 = "{:<12s}: [{:<20s}]".format('Thirst', '#'*(2*int(round(self._thirst))))+ "{:5.2f}/{:2d}".format(self._thirst, MAX)   
              
  
              

        print(s0)
        print(s1)
        print(s2)
        print(s3)
        print(s4)
    
        
    def _update_status(self):
        
        '''
            Update status method prints the pet status at a instance
        '''
        # this function is complete #
        
        faces = {}
        talks = {}
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"
        faces['smell'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

class Cat(Pet):
    
     '''
        This class creates a template of what is defined as cat.
        It makes use of objects and __init__ method created in the Pet class.
        The method makes use of the existing instances to set them equal to the 
        cat edible items list and cat drinkable items list. 
     '''
    
     def __init__(self, name='fluffy', gender='male',color='white'):
         
         Pet.__init__(self, name, 'Cat', gender ,color)
                  
         self._edible_items = [CatFood]
     
         self._drinkable_items = [Water]

        
class Dog(Pet):
	
    '''
    This class creates a template of what is defined as dog.
    It makes use of objects and __init__ method created in the Pet class.
    The method makes use of the existing instances to set them equal to the 
    dog edible items list and dog drinkable items list. 
    '''
   
    
    def __init__(self, name='fluffy', gender='male',color='white'):
         
         Pet.__init__(self, name, 'Dog', gender ,color)
                  
         self._edible_items = [DogFood]
     
         self._drinkable_items = [Water]


# Added function that is the source code from main
         
def pet_control(prompt,my_pet,specie,comands):
    
    '''
    
        This function handle the control of the pet that is 
        prompted by the user. It makes verification cheks to what is prompeted
        so that it correspondes to what is allowed as input.
        
        This function checks the specie to of the created pet to know if it 
        is a cat or dog and make the use of the write class dedicated to the 
        specified specie.
    
        Value: string, object (dog or cat Class), list
        Returns: returns nothing 
        
    '''
    
    if prompt == 'drink':
            
            # The following loop prevents that
            # the amount of liquid is never greater that 10 or less then 1,
            # and is allways a digit
             while True:
                
                 my_liq = input('How much drink ? 1 - 10 scale: ')
                
                 if my_liq.isdigit()==True:
                   
                    if int(my_liq) < 1 or int(my_liq) > MAX :
                        
                        print('Invalid input.')
                        
                    else:
                        break
                        
                 elif my_liq.isdigit()==False:
                     print('Invalid input.')

                 else:
                     break
        
             liquid = Water(my_liq)
            
             my_pet.drink(liquid)
        
            
    if prompt == 'status':
           
           my_pet.show_status()
           
           
    if prompt == 'feed':
        
        
        # The following loop prevents that
        # the amount of liquid is never greater that 10 or less then 1,
        # and is allways a digit
        
        while True:
            
             my_food = input('How much food ? 1 - 10 scale: ') 
              
             if my_food.isdigit()==True:
               
            
                if int(my_food) < 1 or int(my_food) > MAX :
                    
                    print('Invalid input.')

                else:
                    break
                    
             elif my_food.isdigit()==False:
                 print('Invalid input.')

             else:
                 break
             
        if specie == 'dog':
            
            food = DogFood(my_food)
            
        elif specie == 'cat':
            
            food = CatFood(my_food)
        
        my_pet.feed(food)       
       
        
    if prompt == 'play':
            
        my_pet.play_with()
            
            
    if prompt == 'shower':
        my_pet.shower()
            
    if prompt == 'sleep':
        my_pet.sleep()
            
    if prompt.lower() not in comands:
               
        print('Invalid command.')
    
    
    	

def main():
    
    '''
    
    User inputs data for the creation of the pet, data prompeted is verified.
    And if passed the verification. The user gets prompetd to interact with the pet
    by calling the pet_control function
    
    Returns: Does not return anything
    
    '''
    
    
    
    print("Welcome to this virtual pet game!")
    prompt = input("Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): ")
    
    
    
    comands=['drink','shower','sleep','status','q', 'play', 'feed']
    defaut = 'dog fluffy male white'
    
    # error checking for user input
    
    while True:
        
        lst=[]
        
        if prompt == '':
            
            for values in defaut.split():
                
                lst.append(values)
                
            break
            
        else: 
            
            for values in prompt.lower().split():
                
                lst.append(values)
                
            if 'dog' == lst[0] or 'cat' == lst[0]:
                 
                 if 'female' == lst[2] or 'male' == lst[2]:
                    
                    break
                
                
            else:
                prompt = input("Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): ")
                
    # pet specifications
        
    specie = lst[0]
    name = lst[1]
    gender = lst[2]
    color = lst [3]
    
    
    # create a pet object
    
    if specie == 'dog':
        
        my_pet = Dog( name, gender,color)
        
    if specie == 'cat':
        
        my_pet = Cat( name, gender,color)
    
    
    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    
    print(intro)
    
    while prompt != 'q':
    
        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
        
        
        # This function contains the source code 
        # responsible for the control of the pet in
        # responce to the user prompted input
        
        pet_control(prompt,my_pet,specie,comands)
        

    print("Bye ~")
    
if __name__ == "__main__":
    main()