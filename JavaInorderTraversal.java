// User function Template for Java Inorder Traversal

/* A Binary Tree node

class Node {
    int data;
    Node left, right;
   Node(int item)    {
        data = item;
        left = right = null;
    }
} */
class Solution {
    // Function to return a list containing the inorder traversal of the tree.
    ArrayList<Integer> inOrder(Node root) {
        // Code
        ArrayList<Integer> result = new ArrayList<>();
        helper(root, result);
        return result;
    }
    public void helper(Node root, List<Integer> result){
        if(root == null){ return;}
            helper(root.left, result);
            result.add(root.data);       //result.push_back(root.val);
            helper(root.right, result);
        
    }
}
