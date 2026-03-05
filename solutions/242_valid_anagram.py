# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 9.72 MB

            return false;            return false;
        }        }

        unordered_map<char, int> smap;        unordered_map<char, int> smap;

        unordered_map<char, int> tmap;        unordered_map<char, int> tmap;
        for (int i = 0; i < s.size(); i++) {        for (int i = 0; i < s.size(); i++) {
            smap[s[i]] += 1;                   smap[s[i]] += 1;       
        }        }
            tmap[t[i]] += 1;                   tmap[t[i]] += 1;       

    }    }
        return (smap == tmap);        return (smap == tmap);
};};
