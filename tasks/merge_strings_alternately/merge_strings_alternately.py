class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len, word2_len = len(word1), len(word2)
        result = ["" for _ in range(word1_len + word2_len)]
        ptr_res = 0

        for i in range(max(word1_len, word2_len)):
            if i < word1_len:
                result[ptr_res] = word1[i]
                ptr_res += 1

            if i < word2_len:
                result[ptr_res] = word2[i]
                ptr_res += 1

        return "".join(result)

if __name__ == "__main__":
    solution = Solution()
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
