class PArc:
    def __init__(self, iBeg, iEnd, pDestVert, iDestVert):
        self.iBeg = iBeg  # индексы символов метки
        self.iEnd = iEnd  # в исходной строке
        self.pDestVert = pDestVert  # вершина, куда входит дуга
        self.iDestVert = iDestVert  # индекс листа, куда входит дуга


class PNode:
    def __init__(self, ch_arc_idx, pArc):
        self.arcs = {}
        for i in range(256):
            self.arcs[chr(i)] = 0
        self.arcs[ch_arc_idx] = [pArc]

    def add(self, ch_arc_idx, pArc):
        if self.arcs.get(ch_arc_idx) == 0:
            self.arcs[ch_arc_idx] = [pArc]
        else:
            self.arcs[ch_arc_idx].append(pArc)

    def display(self, s):
        for i in range(len(self.arcs)):
            curr = self.arcs.get(chr(i))
            if curr != 0:
                for j in range(len(curr)):
                    print(s[curr[j].iBeg:curr[j].iEnd + 1])


def find_suffixTree_arc(s, substr, m, pTree):
    pArc = None
    idxSubstr, idxArc = 0, 0
    pCurrNode = pTree
    bStopped = 0
    while not bStopped and pCurrNode:
        pNextArc = pCurrNode.arcs.get(ord(substr[idxSubstr]))
        if pNextArc:
            pArc = pNextArc
            idxArc = pArc.iBeg
            while idxSubstr < m and idxArc < pArc.iEnd + 1 and substr[idxSubstr] == s[idxArc]:
                idxSubstr += 1
                idxArc += 1
            if idxArc <= pArc.iEnd:
                bStopped = 1
            else:
                pCurrNode = pArc.pDestVert
        else:
            bStopped = 1
    if idxSubstr == m:
        idxArc += 1
    return pArc, idxArc, idxSubstr


def st_build_naive(s):
    n = len(s)
    pUVArc = PArc(0, n - 1, None, 0)
    pTree = PNode(s[0], pUVArc)
    pWNode = None
    for i in range(1, n):
        # "Поиск" очередного суффикса на дереве
        pUVArc, idxarc, idxsubstr = find_suffixTree_arc(
            s, s[i:], n - i, pTree)
        if not pUVArc:
            pWNode = pTree
        elif idxarc <= pUVArc.iEnd:
            pWNode = pTree
            pWNode.add(s[i], pUVArc)
            p_wv_arc = PArc(idxarc, pUVArc.iEnd,
                            pUVArc.pDestVert, pUVArc.iDestVert)
            pUVArc.pDestVert = pWNode
            pUVArc.iDestVert = -1
        else:
            pWNode = pUVArc.pDestVert
        pArc_new = PArc(i + idxsubstr, n - 1, None, i)
        try:
            pWNode.add(s[i + idxsubstr], pArc_new)
        except IndexError:
            pass
    return pWNode


def st_leaves_traversal(p_start_arc, n_alpha):
    if p_start_arc.iDestVert >= 0:
        print("Найдена позиция", p_start_arc.iDestVert)
    else:
        p_start_node = p_start_arc.pDestVert
        for k in range(n_alpha):
            pArc = p_start_node.arcs[k]
            if pArc:
                st_leaves_traversal(pArc, n_alpha)


if __name__ == '__main__':
    with open("text.txt", "r") as file:
        S = file.readline()
        print("String-> " + S)
        n = len(S)

    tree = st_build_naive(S)
    print('Суффиксное дерево')
    tree.display(S)
    for i in range(len(tree.arcs)):
        curr = tree.arcs.get(chr(i))
        if curr != 0:
            for j in range(len(curr)):
                st_leaves_traversal(curr[j], 256)
