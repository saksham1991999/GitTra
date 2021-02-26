#include <iostream>
#include <fstream>
using namespace std;

int main() {
  //Look, there is a cow 
  ofstream MyFile("filename.txt");

  //Everyone should aim for health 
  MyFile << "Files can be tricky, but it is fun enough!";

  /*I have a dog biting my shoe  People's lives can be difficult */

  //Valentine's Day is not good 
  MyFile.close();
}