struct Node {
    int val;
    Node* next;

    Node(int val, Node* next): val(val), next{next}{}
};


class LinkedList {
private:
    Node* head;
    Node* tail;
public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    int get(int index) {
        Node* temp = head;
        for (int i = 0; i < index; i++){
            if (temp == nullptr){
                return -1;
            }
            temp = temp->next;
        }
        if (temp == nullptr){
            return -1;
        }
        return temp->val;
    }

    void insertHead(int val) {
        head = new Node(val, head);
        if (head->next == nullptr){ // edge case, first element
            tail = head;
        }
    }
    
    void insertTail(int val) {
        if (head == nullptr) {
            insertHead(val);
            return;
        }
        tail->next = new Node(val, nullptr);
        tail = tail->next;
    }

    bool remove(int index) {
        if (head == nullptr) return false;
        if (index == 0) {
            Node* temp = head;
            head = head->next;
            if (head == nullptr) tail = nullptr;
            delete temp;
            return true;
        }
        Node* prev = nullptr;
        Node* temp = head;
        for (int i = 0; i < index; i++){
            if (temp == nullptr){
                return false;
            }
            prev = temp;
            temp = temp->next;
        }
        if (temp == nullptr){
            return false;
        }
        prev->next = temp->next;
        if (temp == tail) tail = prev;
        delete temp;
        return true;
    }

    vector<int> getValues() {
        vector<int> vals{};
        Node* curr = head;
        while (curr != nullptr){
            vals.push_back(curr->val);
            curr = curr->next;
        }
        return vals;
    }
};