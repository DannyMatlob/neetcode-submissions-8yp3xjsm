class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<Integer>();
        minStack = new Stack<Integer>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.size() == 0) {
            minStack.push(val);
            return;
        } 

        int topOfMin = minStack.peek();
        if (topOfMin <= val) {
            minStack.push(topOfMin);
        } else {
            minStack.push(val);
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
