import csv
import matplotlib.pyplot as plt

from data_definitions import *

def main(filename1: str, filename2: str) -> None:
    """
    Reads the files from given filenames and merges them to form a List of CountryInfo, loci.
    loci is then passed to: (1) make_fem_percentage_list, which creates a list of calculated female labour force participation values;
                            (2) extract_happy_score_list, which creates a list of happiness scores for the countries in LOCI
    
    The returned lists (fp and hs, respectively) are passed to create_scatterplot.
    """
    # return None #stub
    
    # Template from HtDAP, based on function composition 
    
    # loii contains the information contained in the gender_inequality csv file
    loii = read_inequality_csv(filename1) #type: List[InequalityInfo]
    
    # lohi contains the information contained in the world_happiness_ranking csv file
    lohi = read_happiness_csv(filename2) #type: List[HappinessInfo]
    
    #loci is the merged list of info from loii and lohi
    loci = merge_inequality_happiness(loii, lohi) #type: List[CountryInfo]
    
    # fp and hs are the lists of calculated fem_lab_percentage values, and extracted happy_scores respectively
    fp = make_fem_percentage_list(loci) #type: List[float]
    hs = extract_happy_score_list(loci) #type: List[float]
    
    return create_scatterplot(fp, hs) 

def parse_float(s: str):
    """
    converts given string s into a float, or returns None if s cannot be 
    represented by a float
    """
    try: 
        return float(s)
    except:
        return None
    
def read_inequality_csv(filename: str) -> List[InequalityInfo]:
    """    
    Reads information from the specified file and returns a List of InequalityInfo.
    """
    #return []  #stub
    
    # Template from HtDAP
    
    # loii contains the result so far
    loii = [] # type: List[InequalityInfo]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:          
            c = InequalityInfo(row[1], parse_float(row[8]), parse_float(row[9]))
            loii.append(c)
        
    return loii

def read_happiness_csv(filename: str) -> List[HappinessInfo]:
    """    
    Reads information from the specified file and returns a List of HappinessInfo.
    """
    #return []  #stub
    
    # Template from HtDAP
    
    # lohi contains the result so far
    lohi = [] # type: List[HappinessInfo]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:       
            c = HappinessInfo(row[0], parse_float(row[3]))
            lohi.append(c)
    
    return lohi

def merge_inequality_happiness(loii: List[InequalityInfo], lohi: List[HappinessInfo]) -> List[CountryInfo]:
    """    
    Merges the List of InequalityInfo and the List of HappinessInfo to create a List of CountryInfo.
    This will keep only data for countries which appear in both csv files.
    """
    
    # return [] #stub

    # Template from List[InequalityInfo] and List[HappinessInfo]
    
    # loci contains the CountryInfo tuples created combining information contained in InequalityInfo and HappinessInfo
    loci = [] # type: List[CountryInfo]

    for ii in loii: 
        for hi in lohi: 
            if compare_country_names(ii,hi):
                CI = CountryInfo(ii.country_name, ii.fem_lab_particip, ii.mal_lab_particip, hi.happy_score)
                loci.append(CI)
    
    return loci

def compare_country_names(ii: InequalityInfo, hi: HappinessInfo) -> bool:
    """    
    Compares the country names contained in InequalityInfo tuple and HappinessInfo tuple and returns true if they are the same.
    """
    # return True #stub

    # Template from InequalityInfo and HappinessInfo
    return ii.country_name == hi.country_name

def calculate_total_fem_lab_percentage(ci: CountryInfo) -> float:
    """    
    Calculates and returns a country's total female labour force participation as: 
    Labour Force Participation Rate (Female) / ( Labour Force Participation Rate (Female) + Labour Force Participation Rate (Male))
    
    """
    # return 0.0 # stub

    # Template from CountryInfo 
    return ci.fem_lab_particip / (ci.fem_lab_particip + ci.mal_lab_particip)

def extract_happy_score_list(loci: List[CountryInfo]) -> List[float]:
    """    
    Given a List[CountryInfo], extracts and returns a list of happy_scores.
    
    """
    # return [] # stub

    # Template from List[CountryInfo]
    
    # List of happy_score seen so far
    acc_happiness = [] # type: List[float]
    
    for ci in loci:
        acc_happiness.append(ci.happy_score)  
        
    return acc_happiness
                                                                      
def make_fem_percentage_list(loci: List[CountryInfo]) -> List[float]:
    """    
    Given a List[CountryInfo], creates and returns a corresponding list of fem_percentages.
    
    """
    # return [] # stub

    # Template from List[CountryInfo] 
    
    # List of calculate_total_fem_lab_percentage computed so far
    acc_fem_per = [] # type: List[float]

    for ci in loci:
        fem_percentage = calculate_total_fem_lab_percentage(ci)
        acc_fem_per.append(fem_percentage)
    
    return acc_fem_per        
                                                                                                                                           
def create_scatterplot(fp: List[float], hs: List[float]) -> None: 
    """ 
    Creates a scatterplot, plotting FP versus HS.
    Annotates the example countries Canada, United States, Japan, Saudi Arabia and Cameroon on the plot.
    
    """
    # return None #stub
   
    # Template based on visualization
    
    # set the labels for the axes
    plt.xlabel('Female Labour Force Participation')
    plt.ylabel('Country Happiness Score')
    plt.title('Female Labour Force Participation vs. Country Happiness Score')

    # create the scatterplot, with markers that are red (c='r') and star-shaped (marker='*')
    plt.scatter(fp,hs,marker='*', c='r')
                 
    # annotate the example countries Canada, United States, Japan, Saudi Arabia and Cameroon
    plt.annotate('Canada', (calculate_total_fem_lab_percentage(CI1), CI1.happy_score))
    plt.annotate('United States', (calculate_total_fem_lab_percentage(CI2), CI2.happy_score))
    plt.annotate('Japan', (calculate_total_fem_lab_percentage(CI3), CI3.happy_score))
    plt.annotate('Saudi Arabia', (calculate_total_fem_lab_percentage(CI4), CI4.happy_score))
    plt.annotate('Cameroon', (calculate_total_fem_lab_percentage(CI5), CI5.happy_score))

    # show the plot
    plt.show()
    
    return None

main("gender_inequality.csv", "world_happiness_ranking_2015.csv")
                                         
