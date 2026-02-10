class Solution {
public:
    int maxArea(vector<int>& height) {

        int n = height.size();

        int maxArea = 0;
        
        for(int i = 0; i<n; i++){
            for(int j= i+1; j<n; j++){
                int w = j-i;
                int current_height = min(height[i], height[j]);
                int area = w*current_height;

                maxArea = max(maxArea, area);
            }

        }
        return maxArea;

    }
};
