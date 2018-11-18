#ifndef LAPTOP_HPP_
#define LAPTOP_HPP_
#include "Computer.hpp"
class Laptop : public Computer
{
  private:
    int m_SlowDownFacter;

  public:
    int GetSlowDownFacter();
    void SetSlowDownFacter(int SlowDownFacter);
    Laptop(int Flops, int SlowDownFacter);
    int GetFlops(int BatteryMode=1);
};

int Laptop::GetSlowDownFacter()
{
    return m_SlowDownFacter;
}
void Laptop::SetSlowDownFacter(int SlowDownFacter)
{
    m_SlowDownFacter = SlowDownFacter;
}
Laptop ::Laptop(int Flops, int SlowDownFacter)
{
    Computer::SetFlops(Flops);
    SetSlowDownFacter(SlowDownFacter);
}
int Laptop::GetFlops(int BatteryMode)
{
    switch (BatteryMode)
    {
    case 0:
        return Computer::GetFlops();
        break;
    case 1:
        return Computer::GetFlops() / m_SlowDownFacter;
        break;
    default:
        return Computer::GetFlops();
    }
}

#endif