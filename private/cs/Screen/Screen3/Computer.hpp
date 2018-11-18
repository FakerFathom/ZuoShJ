#ifndef COMPUTER_HPP_
#define COMPUTER_HPP_
#include "Screen.cpp"
class Computer
{
  private:
    Screen m_screen;
    int m_Flops;

  public:
    void SetScreen(Screen myScreen);
    Screen GetScreen();
    void SetFlops(int Flops);
    int GetFlops();
    Computer(int Flops = 1);
};
//Computer implement
void Computer::SetScreen(Screen myScreen)
{
    m_screen = myScreen;
}
Screen Computer::GetScreen()
{
    return m_screen;
}
void Computer::SetFlops(int Flops)
{
    m_Flops = Flops;
}
int Computer::GetFlops()
{
    return m_Flops;
}
Computer::Computer(int Flops)
{
    SetFlops(Flops);
}
#endif
