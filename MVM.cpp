


#include<iostream>
using std::cout; using std::endl;
#include<vector>
using std::vector;
#include<string>
using std::string; using std::to_string;
#include<algorithm>
using std::copy; using std::lower_bound;
using std::find;using std::sort;using std::transform;
#include<iterator>
using std::ostream_iterator;
#include<sstream>
using std::ostringstream;
using std::ostream_iterator; using std::back_inserter;

#include "proj09_class.h"


  Element::Element(string key, initializer_list<string> values){
//Take a string key and an initializer_list values and construct an Element with those values

    key_ = key;
    values_ = values;

  }

 bool Element::operator ==(const Element& m )const{
//  Two Elements are equal if their two keys_ are equal and if their two values_ are equal.
// o return true if the two Elements meet this condition, false otherwise.
// o this is a member function.

    if ( m.key_== key_ &&  m.values_== values_){

        return true;
    }

    else{

        return false;
    }
 }

 ostream& operator<<(ostream& out, Element& e){

     out<< e.key_ <<":";
     int i =0;

     for(auto ele: e.values_){

         out<< ele;
        
         if (i < e.values_.size()-1 ){
             out<<",";
         }

         ++i;
     }

     return out;
 }

 MVM::MVM(initializer_list<Element> ele){
// initialize the data_ member to the initializer_list
// is added in initializer_list order (see note below) 

//copy(ele.begin(), ele.end(), back_inserter(data_) );

 data_ = ele;

 }

 ostream& operator<<(ostream& out, MVM& mvm){

     int i =0;

     for(auto ele : mvm.data_){
         
         out<< ele;

        if (i < mvm.data_.size()-1 ){
             out<<" ";
         }

        ++i;
     }

       
     return out;
 }


    vector<Element>::iterator MVM::find_key(string key){

        
// returns an iterator that points to an Element in data_
// return value cases are:
// points to an Element in data_ which has the key
// point to an Element in data_ which is just bigger than the key (thus the key isn’t there).
// if data_.end(), the key isn’t there and it’s bigger than all existing keys

        auto itr = lower_bound(data_.begin(), data_.end(), key, 
    
        [] (auto c, string key)

        { return c.key_ < key; });
        
        return itr;
    }


size_t MVM::size(){

  return data_.size();
}


bool MVM::remove_key(string key){


    auto a = find_key(key);

    if( a ->key_ == key){

        data_.erase(a);
        
        return true;
    }

    else{
        return false;
    }

    
}

  vector<string> MVM::find_value(string val){
// returns a (possibly empty) vector<string> which is a list of all keys where val is located
       vector<string> test;
    
// range loop is simple version of this
    for(auto i = data_.begin(); i != data_.end(); i++){

        for(auto o = (*i).values_.begin(); o!= (*i).values_.end(); o++){

            if(  *o == val  ){

                test.push_back( (*i).key_);
            }
        }

       
    }

     return test;
  }
    
 bool MVM::add(string key, string value){

// The key exists. Check the value
// value not in values_, push it onto the back of values_ 
//  value is already in values_, do nothing but return false
//  The key isn’t there and it is bigger than all existing keys
//  push a new Element(key, {value}) onto the back of data_
//  The key isn’t there. The find_key iterator can be used to do an insert into data_.
//  The return is always true unless the key and the value (both) already exist.     

    auto a = find_key(key);
    vector<string> b = find_value(value); // vector of strings

//// if The key exists. Check the value
    if( a ->key_ == key){
    
   if ( find( b.begin(),b.end(), key ) == b.end() ){

        a->values_.push_back(value);
   }
   else{

       return false;
       
       }
    
     }
 
// The key isn’t there and it is bigger than all existing keys push a new Element(key, {value}) onto the back of data_

    if (a->key_ != key &&  key > a->key_ ){

        data_.emplace_back( Element ( key, { value } ) );

    }

    if ( a ->key_ != key){

// places the ( key, { value } ) at the iteration position

    data_.emplace(a, Element ( key, { value } ) );

    }

    return true;
 }

  
vector<string> MVM::remove_value(string  val){
//  for every Element in the MVM
// o if the value is in the values_ of the Element, remove it
// o return a vector<string> of all the keys where a value was removed 

vector<string> test;
vector<Element>::iterator itr;
vector <string> keys = find_value(val); // vector with strings that are keys

 for(auto ele : keys){ // ele is each individual key string

     itr = find_key(ele); //iterator

        auto a = find( itr->values_.begin(), itr->values_.end(), val ); 

            test.push_back(ele);
            itr->values_.erase(a);
     }

    return test;
 }




