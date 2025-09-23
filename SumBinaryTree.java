//  https://www.geeksforgeeks.org/problems/sum-of-binary-tree/1?page=1&company=Microsoft,Flipkart,Adobe,Samsung,MakeMyTrip,Zoho,Paytm,OYO%20Rooms,FactSet,Wipro,Infosys&difficulty=Basic&status=unsolved&sortBy=submissions

//  https://www.geeksforgeeks.org/problems/sum-of-binary-tree/1?page=1

// GFG sum of binary tree

// code in java

/*
// A Binary Tree node
class Node
{
    int data;
    Node left, right;

    Node(int item)
    {
        data = item;
        left = right = null;
    }
}
*/
class Solution {
    // Function to return sum of all nodes of a binary tree
    static int sumBT(Node root) {
        // Your code here
        if(root == null) return 0;
        int ok = root.data;
        int hi = sumBT(root.left);
        int hey = sumBT(root.right);
        return ok+hi+hey;
    }
}

// TC = O(n)
// SC = O(h) = O(log n)
// h -- height of the tree