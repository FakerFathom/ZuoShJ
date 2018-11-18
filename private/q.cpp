#include <iostream>
class LivingThing {
public:
    virtual void breathe() {
        printf("I'm breathing as a living thing.\n");
    }
};
class Animal : public LivingThing {
public:
    virtual void breathe();
};
class Reptile : public LivingThing {
public:
    virtual void breathe();
};
class Snake : public Animal, public Reptile {
public:
    virtual void breathe();
};
int main() {
    Snake snake;
    snake.breathe();
    return 0;
}