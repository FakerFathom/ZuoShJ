#include <iostream>
class LivingThing {
public:
    void breathe() {
        printf("I'm breathing as a living thing.\n");
    }
};
class Animal : public LivingThing {};
class Reptile : public LivingThing {};
class Snake : public Animal, public Reptile {};
int main() {
    Snake snake;
    snake.breathe();
    return 0;
}