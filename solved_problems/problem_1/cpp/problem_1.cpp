/* Problem 1: Multiples of 3 or 5

https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. */


#include <iostream> // use cout for printing to console
#include <list> // use lists

using namespace std; // avoid using std:: before each standard lib component


list<int> numberMultiplesOfThreeOrFive(int below) {
    list<int> MultiplesOfThreeOrFive = {};
    for (int i = 1; i < below; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            MultiplesOfThreeOrFive.push_back(i);
        };
    };
    return MultiplesOfThreeOrFive;
};


int sumMultiplesOfThreeOrFive(int below) {
    list<int> MultiplesOfThreeOrFive = numberMultiplesOfThreeOrFive(below);
    int sum = 0;
    for (int i : MultiplesOfThreeOrFive) {
        sum = sum + i;
    }
    return sum;
}


int main() {
    list<int> belows = {10, 1000};
    
    for (int i: belows) {
        cout << "Sum of multiples of 3 or 5 below " << i << ": " << sumMultiplesOfThreeOrFive(i) << endl;
    } // expect Sum of multiples of 3 or 5 below 10: 23 
    
    return 0; // indicates the program's exit status to the OS
}