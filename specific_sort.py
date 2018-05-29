
total_count=0
my_own_order = ['A', 'B', 'G', 'D', 'H', 'V', 'Z', 'J', 'T', 'Y', 'K', 'L', 'M', 'N', 'S', 'I', 'P', 'X', 'Q', 'R',
                    'W', 'U', 'C', 'E', 'F', 'O']
order = {key: i for i, key in enumerate(my_own_order)}
def size_str(str1,str2):
    if len(str1) < len(str2):
        return len(str1),1
    else:
        return len(str2),2

def cmp(str1,str2):
    [little_str,num]=size_str(str1,str2)
    if str1 == str2:
        return 0
    i=0
    while i < little_str-1:

       if order[str1[i].upper()] < order[str2[i].upper()]:
           return 1
       elif order[str1[i].upper()] > order[str2[i].upper()]:
           return -1
       elif order[str1[i].upper()] == order[str2[i].upper()]:
           i=i+1
           if i==little_str-1:
              if num==1:
                 return 1
              if num==2:
                 return -1


def Sort_fun(sort_lst):
    n = len(sort_lst)
    i=0
    for i in range(n):
        for j in range(i, n):
            par_cmp = cmp(sort_lst[i],sort_lst[j])
            if par_cmp==-1:
                sort_lst[j],sort_lst[i]=sort_lst[i],sort_lst[j]
    return sort_lst

def main():
    a = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
    lst = a.split(' ')
    sorted_list=sorted(lst, key=lambda d: order[d[0].upper()])
    result=Sort_fun(sorted_list)
    str_result = " ".join(str(e) for e in result)
    str_result=str_result.replace(',','')
    print str_result

if __name__ == "__main__":
    main()