def lastStoneWeight(self, stones) -> int:

    while len(stones) > 1:
        heaviest = max(stones)
        stones.remove(max(stones))
        sec_heaviest = max(stones)

        if heaviest != sec_heaviest:
            stones.remove(sec_heaviest)
            stones.append(heaviest - sec_heaviest)
        else:
            stones.remove(sec_heaviest)

    return stones[0] if stones else 0

