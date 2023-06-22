class Num:

    def __init__(self,ls=None):

        self.ls=ls
 
    def mean(self, list_data=None):
        lst = list_data if list_data else self.ls
        n = len(lst)
        s = sum(lst)
        mean = s/n
        return mean if n>0 else float('nan')
    def median(self, list_data=None ):
        lst = sorted(list_data) if list_data else sorted(self.ls)
        n = len(lst)
        mid = (n)//2
        return lst[mid] if n%2 else (lst[mid-1] + lst[mid])/2



