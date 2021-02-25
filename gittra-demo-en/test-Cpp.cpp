#include <iostream>
#include <fstream>
using namespace std;

int main() {
  // 看，有一头牛
  ofstream MyFile("filename.txt");

  // 每个人都应该以健康为目标
  MyFile << "Files can be tricky, but it is fun enough!";

  /*
  我有一只狗咬我的鞋子
  人们的生活可能会很艰难
  */

  // 情人节不好
  MyFile.close();
}