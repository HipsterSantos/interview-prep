from typing import List, Tuple,Dict,Union,Any,Optional

# def great(name:str) -> str:
#     if type(name) is not str:
#         raise TypeError('')
#     return type(name)
#
# # print(great(232))
#
# def contains(name:str)->bool:
#     return name and great(name) and True
#
# print(contains("283"))

# def processData(data:List[Union[str,int]])->Dict[str,int]:
#     dictt = {}
#     for index,elements in enumerate(data):
#         dictt[f"data-{data[index]}"] = data[index]
#     return dictt

# print(processData(["something",221]))

# def processData2(data:List[int])->Tuple[str,int]:
#     return (data[0],data[1])
# print(processData2([1,2,3,4,4]), len((1, 2, 2, 3, 4, 45, 5, 4, 4, 2)),tuple([1,2,2,3]))
if __name__ == "__main__":
    def hugeComputation(tup:Tuple,dict:Dict[str,int],list:List)->List[Union[Tuple,Dict]]:
        #get all tuple having true
        #get dictionary having false
        #get all list item with index event
        tup = (1,2,3,4)
        even = all(i for i in range(len(list)) if i % 2 == 0) # this line righ here check all even numbe and the n retur nfals or true
        return [tup,dict]

print(hugeComputation((1,2,23,3,2),{"soemthing":212},[12,12,33,34,21,34,4,5]))