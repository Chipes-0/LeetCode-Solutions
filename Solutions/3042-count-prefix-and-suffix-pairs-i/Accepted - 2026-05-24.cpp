class Solution {
public:
    struct TrieNode {
        bool isEndOfWord;
        unordered_map<char, TrieNode*> children;
    };
    TrieNode* createNode() {
        TrieNode* node = new TrieNode;
        return node;
    }

    void insert(TrieNode* root, const string& word) {
        TrieNode* current = root;
        for (char c : word) {
            if (current->children.find(c) == current->children.end()) {
                current->children[c] = createNode();
            }
            current = current->children[c];
        }
    }

    bool search(TrieNode* root, string& word) {
        TrieNode* current = root;
        for (char c : word) {
            if (current->children.find(c) == current->children.end()) {
                return false;
            }
            current = current->children[c];
        }
        return true;
    }

    int countPrefixSuffixPairs(vector<string>& words) {
        int N = words.size();
        string word, prefix, sufix;
        int out = 0;
        for(int i = 0; i < N; i++){
            TrieNode* prefixTrie = createNode();
            TrieNode* sufixTrie = createNode();
            word = words[i];
            insert(prefixTrie, word);
            reverse(word.begin(), word.end());
            insert(sufixTrie, word);
            for(int j = 0; j < i; j++){
                prefix = words[j];
                sufix = words[j];
                reverse(sufix.begin(), sufix.end());
                if(search(prefixTrie, prefix) && search(sufixTrie, sufix)) {
                    out++;
                }
            }
        }
        return out;
    }
};

