#ifndef SCREEN_CPP_
#define SCREEN_CPP_

#include <stdlib.h>

class Screen
{
  private:
    int m_width;
    int m_height;

  public:
    void SetWidth(int width);
    void SetHeight(int height);
    int GetWidth();
    int GetHeight();
    int GetNumberPixels();
    Screen(int w = 1, int h = 1);
};
#endif