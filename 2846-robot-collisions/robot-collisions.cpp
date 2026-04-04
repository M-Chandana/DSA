class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        
        int n = positions.size();
        
        // Step 1: store (position, health, direction, original index)
        vector<tuple<int,int,char,int>> robots;
        for(int i = 0; i < n; i++){
            robots.push_back({positions[i], healths[i], directions[i], i});
        }
        
        // Step 2: sort by position
        sort(robots.begin(), robots.end());
        
        stack<int> st; // stack stores indices of robots
        
        for(int i = 0; i < n; i++){
            auto &[pos, health, dir, idx] = robots[i];
            
            if(dir == 'R'){
                st.push(i);
            }
            else{ // dir == 'L'
                
                while(!st.empty() && get<2>(robots[st.top()]) == 'R'){
                    
                    int j = st.top();
                    
                    if(get<1>(robots[j]) < health){
                        // R dies
                        get<1>(robots[j]) = 0;  
                        st.pop();
                        health--;
                    }
                    else if(get<1>(robots[j]) > health){
                        // L dies
                        get<1>(robots[j])--;
                        health = 0;
                        break;
                    }
                    else{
                        // both die
                        get<1>(robots[j]) = 0;   // ✅ FIX
                        st.pop();
                        health = 0;
                        break;
                    }
                }
                
                if(health > 0){
                    st.push(i);
                }
            }
        }
        
        // Step 5: collect survivors
        vector<pair<int,int>> survivors; // {original index, health}
        
        for(int i = 0; i < n; i++){
            if(get<1>(robots[i]) > 0){
                survivors.push_back({get<3>(robots[i]), get<1>(robots[i])});
            }
        }
        
        // sort back to original order
        sort(survivors.begin(), survivors.end());
        
        vector<int> ans;
        for(auto &p : survivors){
            ans.push_back(p.second);
        }
        
        return ans;
    }
};