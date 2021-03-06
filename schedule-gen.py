

'''
Utilize recursive algorithm to generate all schedules from sections list. 

sections - List of sections

Subproblem - comparing two classes

Compare each 


'''
'''
P - sections
R - schedule
X - used

algorithm BronKerbosch1(R, P, X) is
    if P and X are both empty then
        report R as a maximal clique
    for each section s in sections do
        BronKerbosch1(R ⋃ {s}, P ⋂ N(s), X ⋂ N(s))
        P := P \ {s}
        X := X ⋃ {s}
'''
        

sections_map = {}
def build_map(sections):
    
    for sec1 in sections:
        
        # Filter out same class for comparisons
        tmp = [x for x in sections if x.crn != sec1.crn]
        
        for sec2 in tmp:
            
            # Comparison has already been made
            if sec2 in sections_map.keys():
                
                # They are compatible
                if sec1 in sections_map[sec2]:
                    
                    # Add sec2 as a neighbor of sec1
                    sections_map[sec1].append(sec2)
                
                # They have been compared and are not compatible  
                else:
                    
                    # Skip
                    continue
            
            # They have not been compared  
            else:
                
                if are_compatible(sec1, sec2):
                    
                    # Add as neighbors as each other
                    sections_map[sec2].append(sec1)
                    sections_map[sec1].append(sec2)
                
                
               
                

