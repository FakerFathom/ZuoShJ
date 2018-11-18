#ifndef COMPUTER_HPP_
#define COMPUTER_HPP_
#include"Screen.cpp"
class Computer{
private:
Screen m_screen;

public:
Computer():m_screen(480,460){}
void SetScreen(Screen myScreen){
    m_screen=myScreen;
}
Screen GetScreen(){
    return m_screen;
}
};

#endif