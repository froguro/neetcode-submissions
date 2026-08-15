class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Kahn's Algorithm for cycle detection
        // BFS focused on in degrees of nodes
        // basically
        // add nodes that have no dependencies (in_degree == 0) into a queue
        // as you empty out the queue
        // remove the node from the graph
        // insert node into result array
        // once the length of the result array is equal to the total number of nodes, then you know that you've found a topological sort for the entire graph (desired for this problem)
        // otherwise you just continue until all topological sortings are found!
        vector<vector<int>> prereq(numCourses);
        vector<int> indegrees(numCourses, 0); // if a course has no dependencies, then you can take it.
        for (auto& courses : prerequisites) { // Populate the graph
            prereq[courses[1]].push_back(courses[0]);
            indegrees[courses[0]]++;
        }

        

        queue<int> q;
        int processed = 0;

        for (int i = 0; i < numCourses; i++) {
            if (indegrees[i] == 0) {
                q.push(i);
                processed++;
            }
        }
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            for (int neighbor : prereq[curr]) {
                indegrees[neighbor]--;
                if (indegrees[neighbor] == 0) {
                    processed++;
                    q.push(neighbor);
                } 
            }
        }
        
        return processed == numCourses;


    }
};
