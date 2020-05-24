

#include<string>
using std::string;
using std::stol;
#include<sstream>
using std::ostringstream; 
using std::stringstream;
using std::istringstream;
#include<iostream>
using std::cout; using std::endl; using std::ostream; using std::cerr;
#include<fstream>
using std::ifstream; using std::ofstream;
#include <vector>
using std::vector;
using namespace std;

#include "proj08-struct.h"


long Image::bound(long my_row, long my_width) const 
// Look for bound values
{

if (my_row < 0 || my_width < 0){ return 0;}

else if (my_row >= height_ || my_width >= width_) {
  
   return 0;}

else{ 
  
  return pixels_[my_row][my_width];}

}


vector<vector <long> >Image::neighbor_num(long my_row, long my_width)const {
// will look for neighbor values 

  vector<vector<long>> vec;

//to be deleted
  long left;
  long right;
  long up, down, left_corner, right_corner, dlef_corner, drigh_corner;
  long pixel;
//  
  int i=my_row -1;

  while ( i<= my_row+1 ){
  
  
  
    vector<long> temp; 

    // fill temp

    for ( int j = my_width-1 ; j<= my_width+1; ++j){
      // store the bound values in the temporary vector 
      // in orhter to later store it in vector vector long
      temp.push_back(bound(i,j));
    
    }

    vec.push_back(temp);
    ++i ;
  }
  return vec;

}

long use_mask (const vector< vector<long>> &neighbor_num, const vector<vector<long>> &mask){

//apply the mask to the old image, setting the new pixels in the new image
//by passing the mask over all the pixels in the old image (the one the this pointer points to) and
//doing the calculation as described

  long my_sum = 0;
  int i = 0;

  while ( i<3){
    for (int j = 0; j < 3; j++ ){

      my_sum += neighbor_num[i][j] * mask[i][j];

    }

     i++;
  }

  return my_sum;

}



 Image::Image(string f_name) {

  // constructor, reads in the PGM file into the class instance. It:
  // o sets the max_val_, height_ and width_ given in the file
  // o it then reads in every individual pixel value into the vector<vector<long>> v_
  // More on that in the notes section.


   
   // read file

        ifstream input_file(f_name);

        string pixel_string;

        vector<long> temp; // change temp to long
       
        stringstream ss;
	      string line;
    
        // gets the PMG format which for this project it will be P2

         getline(input_file, line);
         //int line_size = line.length();
         //cout << line;

        string format;
        format= line;

        //ignore line with # sign

        while(getline(input_file, line)){

		if( !(line[0] == '#' ) ) 
        
            {break;}

	}

	    ss << line;
        
        
            ss >> width_;

            ss >> height_;

            ss >> max_val_;

            getline(input_file, line);

            //ss << line;

            max_val_ = stol(line); // max valeu of gray shade
        

        //pass the valeu into stringstream so that on
        // next while loop the pixesl_strings can be extracted easily withou empty space


        // convert the pixel values 
        // and append on a vector vector long

        long pixel_value;
        

        while ( getline (input_file, line) ) {

            std::istringstream ss(line);
            std::vector<long> temp;

        while (ss >> pixel_value) {
            
            temp.push_back(pixel_value);
        }
        pixels_.push_back(temp);
    }


}

void Image::write_image(string f_name) const{

//   method, writes out the contents of the class
// instance into the given file as a properly configured PGM file (if you write it, you should be able
// to read it back in and view it using paint.net). 



    ofstream out_file(f_name);

        out_file << "P2" << endl <<
			width_ << " " <<
			height_ << endl <<
			max_val_ << endl;



       for (auto row : pixels_) {
        for (auto elements : row) {
            out_file << elements << ' ';
           // cout << elements << ' ';

        }
        out_file << endl;
        
    }
}



Image Image::convolve(vector<vector<long>> mask, long div, long whiten) const{

 // apply the mask to the old image, setting the new pixels in the new image
 //by passing the mask over all the pixels in the old image

 Image r;

 r.height_  = height_;
 r.width_ = width_;
 r.max_val_ = max_val_;
 r.pixels_ = pixels_;
 int i = 0;
 

while( i < r.height_ ){

  for ( int j = 0 ; j < r.width_ ;  j++  ){

    vector<vector<long>> m = neighbor_num(i, j);

    long value_ = use_mask(mask, m);

    long changed = (value_ / div) + whiten;

    if (changed < 0){

      changed = 0;
    }

    if (changed > max_val_){

      changed = max_val_;
    }

     r.pixels_[i][j] = changed ;

  }

  i++;
 
}

return r;
}
  
  

  Image Image::sharpen() const{

    // method. Applies the 3x3 mask below to create the new image. Calls
    // convolve. When calling convolve, it takes defaults on div and whiten. It returns a
    // new Image.

    vector<vector<long>>v {{0, -1, 0}, {-1, 5, -1}, {0, -1, 0}};

    Image image = convolve(v);
    return image;


  }



  Image Image::edge_detect() const{

    //method. Applies the 3x3 mask below to create the new image.
    // Calls convolve. When calling convolve, it takes defaults on divisor but the image
    // tends to be dark so it provides a whiten to brighten the resulting Image. Use whiten=50.
    // It returns a new Image

    vector<vector<long>>v {{0, 1, 0}, {1, -4, 1}, {0, 1, 0}};

    Image image = convolve(v,1,50);

    
    return image;
  }

Image Image::blur() const{

  //   method. Applies the 3x3 mask below to create the new image. Calls
  // convolve. When calling convolve, it takes defaults on whiten but mask always
  // overshoots the max_val_.

    vector<vector<long>>v {{1, 1, 1}, {1, 1, 1}, {1, 1, 1}};

    Image image = convolve(v,9,0);
   
    return image;
}

  Image Image::emboss() const{

    //method. Applies the 3x3 mask below to create the new image. Calls
    // convolve. When calling convolve, it takes defaults on divisor and whiten. It returns a
    // new Image.

    vector<vector<long>>v {{-2, -1, 0}, {-1, 1, 1}, {0, 1, 2}};

    Image image = convolve(v);
    return image;
  }

  void Image::embed(const Image &secret_){

     //method. Takes the secret image by const&,
      //and embeds it in the plain image (the object on which it is called.) 

    for ( int i = 0 ; i < secret_.height_ ;  i++  ){
  for ( int j = 0 ; j < secret_.width_ ;  j++  ){

    if (secret_.pixels_[i][j]==0){

      if (pixels_[i][j] % 2 == 1){
          
          pixels_[i][j] = pixels_[i][j] -1;

      }
      


    }
    else {

      if ( pixels_[i][j] % 2 == 0 ){

             if ( pixels_[i][j] == max_val_){

               pixels_[i][j] = pixels_[i][j] -1;
             }

             else{
                pixels_[i][j] = pixels_[i][j] +1;

             }

             
      }
    }
      

  }
  }
  }
  
  Image Image::extract(long m) const{

  // This function returns an image which is
  // extracted from the pixels in the calling object (referred to by the this pointer). The max_val
  // of this image is set to max_val, and the dimensions are the same as the called image object.
  // Values of pixels in the resulting image are either 0 or max_val

    Image image;

    image.pixels_ = pixels_;
    image.width_ = width_;
    image.height_ = height_;
    image.max_val_= m;

    for ( int i = 0 ; i < image.height_ ;  i++  ){
  for ( int j = 0 ; j < image.width_ ;  j++  ){

    if (image.pixels_[i][j] %2 ==1){

        image.pixels_[i][j]= image.max_val_;
    }
    else {

        image.pixels_[i][j]= 0;

    }


  }
    }
 
    
    return image;
  }

  

 
