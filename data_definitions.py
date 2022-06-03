from typing import NamedTuple, List

##################
# Data Definitions

InequalityInfo = NamedTuple('InequalityInfo', [('country_name', str),
                                               ('fem_lab_particip', float), # in range[0,100]
                                               ('mal_lab_particip', float) # in range[0,100]
                                               ])
                                         
# interp. a country's name, female labour force participation rate and male labour force participation rate for the year 2015. 
                            
HappinessInfo = NamedTuple('HappinessInfo', [('country_name', str),
                                             ('happy_score', float)  # in range[0,10] 
                                            ])
                                         
# interp. a country's name and happiness score for the year 2015. 

CountryInfo = NamedTuple('CountryInfo', [('country_name', str),
                                         ('fem_lab_particip', float), # in range[0,100]
                                         ('mal_lab_particip', float), # in range[0,100]
                                         ('happy_score', float)  # in range[0,10] 
                                        ])
                                         
# interp. a country's complete information, with its name, female labour force participation rate, male labour force participation rate and happiness score for the year 2015. 

II1 = InequalityInfo('Canada', 61.6, 71)
II2 = InequalityInfo('United States', 56.3, 68.9)
II3 = InequalityInfo('Japan', 48.8, 70.4)
II4 = InequalityInfo('Saudi Arabia', 20.2, 78.3)
II5 = InequalityInfo('Cameroon', 63.8, 76.8)

HI1 = HappinessInfo('Canada', 7.427)
HI2 = HappinessInfo('United States', 7.119)
HI3 = HappinessInfo('Japan', 5.987)
HI4 = HappinessInfo('Saudi Arabia', 6.411)
HI5 = HappinessInfo('Cameroon', 4.252)

CI1 = CountryInfo('Canada', 61.6, 71, 7.427)
CI2 = CountryInfo('United States', 56.3, 68.9, 7.119)
CI3 = CountryInfo('Japan', 48.8, 70.4, 5.987)
CI4 = CountryInfo('Saudi Arabia', 20.2, 78.3, 6.411)
CI5 = CountryInfo('Cameroon', 63.8, 76.8, 4.252)

# template based on Compound
def fn_for_inequality_info(ii: InequalityInfo) -> ...:
    return ...(ii.country_name,
               ii.fem_lab_particip,
               ii.mal_lab_particip)

# template based on Compound
def fn_for_happiness_info(hi: HappinessInfo) -> ...:
    return ...(hi.country_name,
               hi.happy_score)

# template based on Compound
def fn_for_country_info(ci: CountryInfo) -> ...:
    return ...(ci.country_name,
               ci.fem_lab_particip,
               ci.mal_lab_particip,
               ci.happy_score)
                                         
# List[InequalityInfo]
# interp. a list of InequalityInfo

LOII0 = []
LOII1 = [II1]
LOII2 = [II1, II2]
LOII3 = [II1, II2, II3, II4, II5]

# List[HappinessInfo]
# interp. a list of HappinessInfo

LOHI0 = []
LOHI1 = [HI1]
LOHI2 = [HI1, HI2]
LOHI3 = [HI1, HI2, HI3, HI4, HI5]     
                         
# List[CountryInfo]
# interp. a list of CountryInfo

LOCI0 = []
LOCI1 = [CI1]
LOCI2 = [CI1, CI2]
LOCI3 = [CI1, CI2, CI3, CI4, CI5]

# template based on arbitrary-sized and reference rule
def fn_for_loii(loii: List[InequalityInfo]) -> ...:
    # description of the acc
    acc = ...       # type: ...
    for ii in loii:
        acc = ...(fn_for_inequality_info(ii), acc)

    return ...(acc)  

# template based on arbitrary-sized and reference rule
def fn_for_lohi(lohi: List[HappinessInfo]) -> ...:
    # description of the acc
    acc = ...       # type: ...
    for hi in lohi:
        acc = ...(fn_for_happiness_info(hi), acc)

    return ...(acc)   

# template based on arbitrary-sized and reference rule
def fn_for_loci(loci: List[CountryInfo]) -> ...:
    # description of the acc
    acc = ...       # type: ...
    for ci in loci:
        acc = ...(fn_for_country_info(ci), acc)

    return ...(acc)
