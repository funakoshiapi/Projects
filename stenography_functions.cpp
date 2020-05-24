


#pragma once

#include <string>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <bitset>
using std::string;

string lower_case(const string &s);
string to_binary(char);
char from_binary(const string &);
bool check_message(const string &, const string &);
string encode(const string &, const string &);
string decode(const string &);
bool punctuation(char c);
bool bit_size_5(const string &n);
void is_alpha_loop(string text_lower, int index);


string lower_case(const string &s)
// convert to lower case
{

    string modified = "";
    for (char c : s)
    {
        modified.push_back(std::tolower(c));
    }
    return modified;
}

string to_binary(char c)
// convert to binary
{

    int output;

    if (isupper(c) || punctuation(c) == true)
    {

        return "";
    }
    else
    {
        output = c - 'a'; //index
    }

    return (std::bitset<5>(output).to_string()); // return 5 bit binary converted to string
}

bool punctuation(char c)

// this function checks if the puctuation is present in the string
{

    string pun = "!;'/?.,-_#*=+|`";

    for (int i = 0; i < pun.size(); i++)
    {
        char t = pun[i];
        if (c == t)
            return true;
    }

    return false;
}

char from_binary(const string &n)
// convert binary to string
{

    long decimal = (std::bitset<5>(n).to_ulong());
    long ascii = 97 + decimal;
    char character = static_cast<char>(ascii);

    // check if ascii is between a and z
    if (ascii > 122 || ascii < 97)
    {

        return '\0';
    }
    // check if is a 5 bit binary
    else if (bit_size_5(n) == true)
    {

        return '\0';
    }

    else
    {

        if (std::isupper(character))
        {

            return '\0';
        }
    }

    return character;
}

bool bit_size_5(const string &n)

// function to chek if bit size is equal to 5
{

    for (int i = 0; i < n.size(); i++)
    {
        if (i > 5)
        {
            return true;
        }
    }
    return false;
}

bool check_message(const string &plain, const string &secret)
// check if parameters apply
{


    long count = 0;
    for (char c : plain)
    {
        //is alphabetic, add to count
        if (isalpha(c))
        {
            count++;
        }
    }
    if (count >= (secret.size() * 5))
    {
        // 5x bigger than original
        return true;
    }

    return false;
}

string encode(const string& original_text, const string& message){
    //encodes the string input

  
    string text_lower = lower_case(original_text);
    string secret_l_case = lower_case(message);
    int index = 0;
  
   
  
    if (check_message(text_lower, secret_l_case)){
        for (char c : secret_l_case){
            //convert the character to binary
            string bi_string = to_binary(c);
            
            for (int i = 0; i < bi_string.size(); i++){
                if (bi_string[i] == '0'){
                  
                    while (true){
                        
                        if ((index < text_lower.size()) && (!isalpha(text_lower[index]))){
                            index++;
                        }
                        else if (isalpha(text_lower[index])){
                            break;
                        }
                        
                    }
                    // convert to lower
                    text_lower[index] = tolower(
                        text_lower[index]);
                    index++;
                }
                else if (bi_string[i] == '1'){

                    //check for alpha characters
                     while (true){
                        
                        if ((index < text_lower.size()) && (!isalpha(text_lower[index]))   ) {
                            index++;
                        }
                        else if (isalpha(text_lower[index])){
                            break;
                        }
                        
                    }
                    //character is found, convert to upper
                    text_lower[index] = toupper(text_lower[index]);
                    index++;
                }
            }
        }
        // encoded
        return text_lower;
    }
    else{
    
        return "Error";
    }
}


string decode(const string& decoding){
    // decode the string input
    
    string d_bi = "";
    string message = "";
    long secret_index= 0;
    
   
     for (int i = 0; i < decoding.size(); i++)
      {
            char c = decoding[i];
            
            if (isalpha(c)){
                if (islower(c)){
                //if low 
                d_bi.push_back('0');
            }
            else{
                //if high
                d_bi.push_back('1');
            }
        }

  
    
        if (d_bi.size() == 5 || d_bi.size() >= 5){
            //takes care of the space

            int ascii = 27; // 27 represent space in the accii table

            if (d_bi == (std::bitset<5>(27).to_string())){
                message.push_back(' ');
            }

            else{
                
                //add letter to message string
                long decimal = (std::bitset<5>(d_bi).to_ulong());
                secret_index=   97 + decimal;
                message.push_back(static_cast<char>(secret_index));
            }
            //reset binary string
            d_bi = "";
        }
    }
    //returns the final secret message
    return message;
}
