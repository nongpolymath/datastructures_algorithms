#include <stdexcept>

template <class T>
class Stack {
private:
    struct StackNode {
        T data;
        StackNode* next;
    };
    StackNode* top;

public:
    Stack() : top(nullptr) {}

    ~Stack() {
        while (!isEmpty()) pop();
    }

    void push(const T& item) {
        StackNode* node = new StackNode();
        node->data = item;
        node->next = top;
        top = node;
    }

    T pop() {
        if (top == nullptr) throw std::out_of_range("pop from an empty stack");
        T item = top->data;
        StackNode* temp = top;
        top = top->next;
        delete temp;
        return item;
    }

    T peek() const {
        if (top == nullptr) throw std::out_of_range("peek from an empty stack");
        return top->data;
    }

    bool isEmpty() const {
        return top == nullptr;
    }
};