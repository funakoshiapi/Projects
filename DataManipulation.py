

# Opens a data file, and allows the user to observe data about singers and songs.
# The data is diplayed on a table. And the user can also plot the 
# displayed data.




import csv
import string
import pylab
from operator import itemgetter

def open_file(message):
    
    '''
        Asks for input file name, and opens the existing file
        value: processes type string
        Returns: returns a file object
    '''
    
    while True:
        
        try:
            file_obj = open(message, 'r')
            
            return file_obj
          
        
        except FileNotFoundError:
            
            message = input ("File not found.") 
           

def read_stopwords(fp):
    ''' Will read file by line 
        value: file pointer
        Returns: a set '''
    
   
    lst=[]
    
    for line in fp:
        
        l = line.lower()
        line_lst = l.strip()
        lst.append(line_lst)
    
    my_set = set(lst)   
    
    return my_set    
        
        

def validate_word(word, stopwords):
    
    ''' will chek if respect the requested paramenters 
        value: a set and 
        Returns:  a boolean'''
    
    
    if word in stopwords:
        return False
    else: 
        for i in word:
            if i in string.punctuation:
                return False
    if word.isalpha():
        return True
    return False        


def process_lyrics(lyrics, stopwords):
    ''' Will format so that lyrics are outputed lower case and without punctuation
        value: string and set
        Returns: a set'''
    
    word_set = set()
    
    
    lyrics_list = lyrics.split()
    
    # Proccess lyrics function is used to format the lyrics, removing puntuation and 
    
    for word in lyrics_list:
        
        word = word.lower().strip()
        word = word.strip(string.punctuation)
  
        if word and validate_word(word, stopwords) == True:
            
            word_set.add(word)
            
    return word_set


def read_data(fp, stopwords):
    ''' Will read the data, format it and pass to a dictionary
        value: file pointer, and set
        Returns: a dictionary''' 
    
    my_di= {}
    
    fp.readline()
    
    #allows to better format the csv file
    
    my_reader = csv.reader(fp)

    # Reads the file pointer and
    # and separating then by 
    # song, singer, lyrics
    # Proccess lyrics function is used to format the lyrics, removing puntuation and 
    # transforming it to lower case
    # update_dictionary will pass the formated information into the new list
    
    
    for row in my_reader:
        
        song = row[1]
        singer = row[0]
        lyrics = row [2].lower()
        
        my_lyrics = process_lyrics(lyrics, stopwords)
        
        update_dictionary(my_di, singer, song,  my_lyrics )
        
        
    return my_di
    


def update_dictionary(data_dict, singer, song, words):
        ''' Will update the dictionary with the given arguments 
        value: dictionary, set
        Returns: None''' 
            
         
        if singer not in data_dict:
             
             data_dict[singer] = {}
             
        if song not in data_dict[singer]:
             
            data_dict[singer][song] = set()
            
        data_dict[singer][song] = words
      

        
def calculate_average_word_count(data_dict):
    ''' Will  calculate the average word count 
        value: dict
        Returns: dict''' 
    
    my_di = {}
    
    
    for singer in data_dict:
        
        singer_t =0
        songs_t =0
  
        if singer not in my_di:
            
             my_di[singer] = {}
             
        for song in data_dict[singer]:
            
             singer_t +=1
            
             for str in data_dict[singer][song]:
                 
                 songs_t +=1
                 
        average_count = float ( songs_t/ singer_t )
        my_di[singer] = average_count
    
    return my_di
      


def find_singers_vocab(data_dict):
    
    ''' Will provide a set of distinct words 
        value: dict
        Returns: dict''' 
    
    my_di = {}
    
    # checks if elements exist in the 
    # dictionary, and then pass it to the new dictionary
    # adding the lyrics correspondent to its singer
    
    for singer in data_dict:
        
        if singer not in my_di:
            
            my_di[singer] = set()
            
            for song in data_dict[singer]:
                
                for words in data_dict[singer][song]:
                
                    if words not in my_di[singer]:
                 
                        my_di[singer].add(words)
    return my_di           
        

def display_singers(combined_list):
    
    ''' Will provide a table of ifo
        value: list
        Returns: none''' 
    
    
    print("{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs"))
    print('-' * 80)
    
    
    # sorting the from highest to smallest,
    # only outputing the the top 10 oon the list
    
    combined_list = sorted (combined_list, key = itemgetter(1), reverse= True)
    k = combined_list[:10]
    for i in k:
        print( '{:<20s}{:>20.2f}{:>20d}{:>20d}'.format(i[0],i[1],i[2],i[3]))

def vocab_average_plot(num_songs, vocab_counts):
    """
    Plot vocab. size vs number of songs graph
    num_songs: number of songs belong to singers (list)
    vocab_counts: vocabulary size of singers (list)
        
    """       
    pylab.scatter(num_songs, vocab_counts)
    pylab.ylabel('Vocabulary Size')
    pylab.xlabel('Number of Songs')
    pylab.title('Vocabulary Size vs Number of Songs')
    pylab.show()

def search_songs(data_dict, words):
    ''' allows to search songs 
        value: dict, set
        Returns: list'''
    
    lst_song = []
    for singer in data_dict:
        for song , wordset in data_dict[singer].items():
            
            if words  <= wordset:
                my_tup = (singer, song)
                lst_song.append(my_tup)
                lst_song = sorted(lst_song, key = itemgetter(0,1))
                
    return lst_song            
    

def main():
    
    ''' This function is where the other functions are called, and where
    the object file is closed.
    Value: has no argument
    Returns: Does not return anything'''
    
    message = input('Enter a filename for the stopwords: ')
    song_data = open_file(message)

    message = input('Enter a filename for the song data: ')
    
    open_my_file = open_file(message)
    
    reading_data = read_stopwords(song_data)
    
    data_reading = read_data(open_my_file, reading_data )
    
    the_average = calculate_average_word_count(data_reading)
    
    lst_combined= []
    
    vocabulary_m = find_singers_vocab(data_reading)
    
    my_songs_total = []
    
    my_new_v_list = []
    
    
    # this iterartion is important because 
    # it allows to create a list containing 
    # the singer name, count of words, word size and song num to be displayed
    
    for singer in data_reading:
        
        my_count_w = the_average[singer]
        
        words_size_1 = len (vocabulary_m[singer])
        
        my_new_v_list.append(words_size_1)
        
        my_song_num = len(data_reading[singer])
         
        my_songs_total.append(my_song_num)
        
        lst_combined.append((singer,  my_count_w, words_size_1, my_song_num))
        
    display_singers(lst_combined)
    
    my_plot = input('Do you want to plot (yes/no)?: ')   
    print()
    
    if my_plot == 'yes':
        
        vocab_average_plot(my_songs_total,my_new_v_list)
        
        
    print('Search Lyrics by Words')
    print()

    Q = True    
    
    while Q == True:
        
        dis_set = input('Input a set of words (space separated), press enter to exit: ')
        
        if dis_set == '':
            break
    
        dis_set = dis_set.split()
        
        dis_set = set(dis_set)
        
        info_data = search_songs(data_reading, dis_set)
        
        if len(info_data) == 0:
            
            print()*3

         
        print('There are %s songs containing the given words!'% len(info_data)) 
        
        print('{:<20s}{:<20s}'.format('Singer', 'Song'))
    
        info_data = sorted ( info_data, key = itemgetter(0))
        
        if len(info_data)>= 5:  
            
            info_data = info_data[0:5]
            
            for t in info_data:  
                
                print('{:<20s}{:<20s}'.format(t[0], t[1]))

if __name__ == '__main__':
     main()     
        
    #op.close()

    #'Enter a filename for the stopwords: '
    #'Enter a filename for the song data: '
    #'Do you want to plot (yes/no)?: '

#    RULES = """1-) Words should not have any digit or punctuation
#2-) Word list should not include any stop-word"""
                
    #"Search Lyrics by Words"
    #"Input a set of words (space separated), press enter to exit: "
    #'Error in words!'
    #"There are {} songs containing the given words!"
    #"{:<20s} {:<s}"

     
