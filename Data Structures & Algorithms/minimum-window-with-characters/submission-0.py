class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t, window = {}, {}
        for c in t:
            hash_t[c] = 1 + hash_t.get(c, 0)

        have, need = 0, len(hash_t)
        res = [-1, -1]
        len_res = float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            # acrescentar caracter no map da janela 
            window[c] = 1 + window.get(c, 0)

            # caracter atual é procurado e bateu em qtd
            if c in hash_t and window[c] == hash_t[c]:
                have += 1

            # loop para diminuir janela do comeco buscando substring menor que corresponda aos criterios
            while have == need:
                if (r - l + 1) < len_res: # substring valida eh menor
                    res = [l, r]
                    len_res = (r - l + 1)

                window[s[l]] -= 1

                # valor cortado do inicio era caracter procurado
                if s[l] in hash_t and window[s[l]] < hash_t[s[l]]:
                    have -= 1
                # caminha janela
                l += 1
        l, r = res
        return s[l:r+1] if len_res < float("inf") else ""
       
        
