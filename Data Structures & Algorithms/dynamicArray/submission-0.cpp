#include <iostream>
using namespace std;

class DynamicArray {
private:
    int* array;
    int capacity;
    int curr_idx;

public:
    // Constructor
    DynamicArray(int cap) {
        capacity = cap;
        curr_idx = 0;
        array = new int[capacity];
    }

    // Destructor
    ~DynamicArray() {
        delete[] array;
    }

    int get(int i) {
        return array[i];
    }

    void set(int i, int n) {
        array[i] = n;
    }

    void pushback(int n) {
        if (curr_idx == capacity) {
            resize();
        }
        array[curr_idx] = n;
        curr_idx++;
    }

    int popback() {
        curr_idx--;
        return array[curr_idx];
    }

    void resize() {
        int new_capacity = capacity * 2;
        int* new_array = new int[new_capacity];

        for (int i = 0; i < curr_idx; i++) {
            new_array[i] = array[i];
        }

        delete[] array;
        array = new_array;
        capacity = new_capacity;
    }

    int getSize() {
        return curr_idx;
    }

    int getCapacity() {
        return capacity;
    }
};