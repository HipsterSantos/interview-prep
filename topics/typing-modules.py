from typing import List, Tuple,Dict,Union,Any

def great(name:str)->str:
    return name

def contains(name:str)->bool:
    return name and great(name) and True
def processData(data:List[str,int])->Dict[str,int]:
    dictt = {}
    for index,elements in range(len(data)):
        dictt[f"data-{data[index]}"] = data[index]
    return dictt
def processData2(data:List[int])->Tuple[str,int]:
    return (data[0],data[1])
def hugeComputation(tup:Tuple,dict:Dict,list:List)->List[Tuple,Dict]:
    #get all tuple having true
    #get dictionary having false
    #get all list item with index event
    even = all(i for i in range(list) if i % 2 == 0) # this line righ here get all even number
    return [even,dict]