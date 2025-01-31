// C++ random code
//  https://leetcode.com/problems/redundant-connection/description/?envType=daily-question&envId=2025-01-29

class Solution {
private:
    bool isConnected(int src, int target, vector<bool>& visited,
        vector<int> adjList[]) {
        visited[src] = true;
        if (src == target) {
            return true;
        }
        int isFound = false;
        for (int adj : adjList[src]) {
            if (!visited[adj]) {
                isFound = isFound || isConnected(adj, target, visited, adjList);
            }
        }
        return isFound;
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int N = edges.size();
        vector<int> adjList[N];
        for (auto edge : edges) {
            vector<bool> visited(N, false);

            // If DFS returns true, we will return the edge.
            if (isConnected(edge[0] - 1, edge[1] - 1, visited, adjList)) {
                return edge;
            }
            adjList[edge[0] - 1].push_back(edge[1] - 1);
            adjList[edge[1] - 1].push_back(edge[0] - 1);
        }
        return {};
    }
};

/*
The provided solution uses Depth-First Search (DFS) to determine if adding an edge creates a cycle in an undirected graph. 

**Time Complexity:**
The time complexity of the solution can be analyzed as follows:
1. For each edge in the input list, the algorithm performs a DFS to check if the two vertices of the edge are already connected. In the worst case, the DFS may visit all vertices and edges in the graph.
2. The DFS takes O(V + E) time, where V is the number of vertices and E is the number of edges.
3. Since we check each edge in the input list, the overall time complexity becomes O(E * (V + E)). However, since the number of edges E is at most V (for a connected graph), we can simplify this to O(E^2) in the worst case.

**Space Complexity:**
The space complexity is determined by:
1. The adjacency list representation of the graph, which requires O(E) space.
2. The visited array used in the DFS, which requires O(V) space.
3. The recursion stack for DFS can go as deep as O(V) in the worst case.

Thus, the overall space complexity is O(V + E), which simplifies to O(E) since E can be at most V in a connected graph.

In summary:
- Time Complexity: O(E^2)
- Space Complexity: O(E)
*/