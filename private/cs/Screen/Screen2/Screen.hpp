#include"Screen.cpp"


void Screen::SetWidth(int width){
    m_width=width;
}
void Screen::SetHeight(int height){
    m_height=height;
}
int Screen::GetWidth(){
    return m_width;
}
int Screen::GetHeight(){
    return m_height;
}
int Screen::GetNumberPixels(){
    return m_height*m_width;
}
Screen::Screen(int w,int h){
    SetWidth(w);
    SetHeight(h);
}