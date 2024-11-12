# made with help of Aprxl :>

class Solution:
    #3rd attempt: adaption of a dfs on the graph.
    def go(self, current: str, tickets: dict, results: list):
        print("DEBUG! current", current)
        try:
            this = tickets[current]
        except:
            this = []

        while len(this) > 0:
            next = this.pop(0)
            #print("DEBUG! next:", next)
            self.go(next, tickets, results)

        results.append(current)
        return
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        zetta = {}
        results = []
        for i in tickets:
            if i[0] not in zetta:
                zetta[i[0]] = [i[1]]
            else:
                zetta[i[0]].append(i[1])
        for key in zetta:
            zetta[key] = sorted(zetta[key])
        print(zetta)
        self.go("JFK", zetta, results)
        results.reverse()
        return results