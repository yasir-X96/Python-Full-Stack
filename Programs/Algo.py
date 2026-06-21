# find a number in a list

def linear_search(scores,target):
    for index in range(len(scores)):
        if scores[index]==target:
            return index
    return -1

scores=[25,30,50,69,55]

target=69

search_result=linear_search(scores,target)

if( search_result!=-1):
    print(f"Score found: {search_result}")
else:
    print("score not found")

# for num in scores:
#     if num==target:
#         print("target found:",num)
#         break

# Binary Search

 # 5,10,15,20, 25, 30, 35
# search 25
# 1st step---Middle 20  25>20---search right half

def binary_search(numbers,target):
    left=0
    right=len(numbers)-1
    while left<=right:
        mid=(left+right)//2

        if numbers[mid]==target:
            return mid
        elif numbers[mid]< target:
            left=mid+1
        else:
            right=mid-1
    return -1


numbers=[5,10,15,20,25,30,35,45]
target=45
result=binary_search(numbers,target)
if (result != -1):
    print(f"Score found: {result}")
else:
    print("score not found")


#Greedy Approach
#Given list of meetings with start and End Time ,single meeting room is available , 
# schedule as many(max) meetings as possible with non-overlapping meetings in a room
def schedule_meetings(meetings):
    # sort the meetings by endTime
    meetings.sort(key=lambda m:m[2])

    selected=[]
    # always select first meeting
    selected.append(meetings[0])

    last_endTime=meetings[0][2]

    for meeting in meetings[1:]:
        start_time=meeting[1]

        if start_time>=last_endTime:
            selected.append(meeting)
            last_endTime=meeting[2]

    return selected



meetings=[
    ("M1",1,5),
    ("M2", 2, 3),
    ("M3", 3, 6),
    ("M4", 0,7),
    ("M5", 5, 8),
    ("M6", 8, 9),
]

schedule_result=schedule_meetings(meetings)

for meeting in schedule_result:
    print(meeting)

print ("Total meetings:",len(schedule_result))