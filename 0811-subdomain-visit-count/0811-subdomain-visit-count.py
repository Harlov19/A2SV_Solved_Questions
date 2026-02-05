class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        for pair in cpdomains:
            pair = pair.split(" ")
            visit = int(pair[0])
            domain =  pair[1]
            counts[domain]+=visit
            while True:
                if(domain.find('.')==-1):
                    break
                domain = domain[domain.find('.')+1:]
                counts[domain]+=visit
            
        return [f"{value} {key}" for key,value in  counts.items()]
            
