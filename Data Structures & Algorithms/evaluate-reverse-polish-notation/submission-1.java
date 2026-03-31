class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> args = new Stack<Integer>();
        for (String c : tokens) {
            if (c.equals("+")) {
                args.push(args.pop() + args.pop());
            } else if (c.equals("*")) {
                args.push(args.pop() * args.pop());
            } else if (c.equals("-")) {
                int a = args.pop();
                int b = args.pop();
                args.push(b-a);
            } else if (c.equals("/")) {
                int a = args.pop();
                int b = args.pop();
                args.push(b/a);
            } else {
                args.push(Integer.parseInt(c));
            }
        }
        return args.pop();
    }
}
