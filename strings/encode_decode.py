class Encrypt:

    @staticmethod
    def encode(strs: list[str]) -> str:
        ret = ""

        # "#" helps to avoid when len(s) == 0 and list goes out of index
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    @staticmethod
    def decode(s: str) -> list[str]:
        ret = []
        i = 0

        while i < len(s):
            temp = ""

            while s[i] != "#":
                temp += s[i]
                i += 1

            i += 1
            l = int(temp)  # len(word)
            word = ""
            for _ in range(l):
                word += s[i]
                i += 1
            ret.append(word)

        return ret


class EncryptOrd:

    @staticmethod
    def encode(strs: list[str]) -> str:
        if not len(strs):
            return ""

        l = []
        for s in strs:
            w = ""
            for c in s:
                w += str(ord(c) + 6) + " "

            if len(w):
                l.append(w)
            else:
                l.append("e")

        return "b".join(l)

    @staticmethod
    def decode(s: str) -> list[str]:
        if not len(s):
            return []

        l = []
        words = s.split("b")

        for w in words:
            if w == "e":
                l.append("")
            else:
                chars = w.split()
                word = ""

                for c in chars:
                    word += chr(int(c) - 6)
                l.append(word)

        return l
