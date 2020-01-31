lbs = list(map(int , input().split(' ')))
print("Student weight in lbs",lbs)
# kgs=[]
# for x in lbs:
#     kgs.append(x*0.4);
# print("Students weight in kgs", kgs)


kgs=[i*0.4 for i in lbs]
print("Student weight in Kgs:", kgs)