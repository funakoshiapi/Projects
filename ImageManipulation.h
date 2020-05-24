
//#ifndef PROJ08-STRUCT_H
//#define PROJ08-STRUCT_H


#pragma once

#include<vector>
using std::vector;
#include<string>
using std::string;
#include <math.h>
#include <fstream>
using std::ifstream; using std::ofstream;
#include <vector>
#include <sstream>


struct Image{

public: // could be private, testing easier as public

  
  vector<vector<long>> pixels_; // where the pixels will be stored

  long height_ = 0;
  long width_ = 0;
  long max_val_ = 0;

  Image convolve(vector<vector<long>> mask, long div=1, long whiten=0) const;

public:

  Image()=default;

  Image (string f_name);

  void write_image(string f_name) const;
 
  Image sharpen() const;
  Image edge_detect() const;
  Image blur() const;
  Image emboss() const;
  void embed(const Image &);
  Image extract(long) const;
  //add in h
  long bound(long my_row, long my_width) const;
  vector<vector <long>>neighbor_num(long my_row, long my_width)const;




};



//#endif 