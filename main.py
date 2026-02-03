import numpy as np

marks=np.array([
               [78,85,96],
               [95,88,92],
               [89,91,90],
               [100,95,98],
               [76,80,85]
               ])
print("Marks of the Students:",marks)
print()

# Calculate the average marks for each student
average_marks=np.mean(marks,axis=1)
print("Average marks of each student is :\n",average_marks[0],average_marks[1],average_marks[2],average_marks[3],average_marks[4])
print()

# Calculate the average marks for each subject
average_mrk_subject=np.mean(marks,axis=0)
print("Average marks of each subject is :\n",average_mrk_subject[0],average_mrk_subject[1],average_mrk_subject[2])
print()

# highest and lowest marks in each subject
highest_marks=np.max(marks,axis=0)
lowest_marks =np.min(marks,axis=0)
print("Highest marks in each subject:",highest_marks)
print("Lowest marks in each subject:",lowest_marks)
print()

#Total marks obtained by a student
total=np.sum(marks,axis=1)
print("Total marks obtained by each student is:\n",total[0],total[1],total[2],total[3],total[4])
print()

# Highest scorer and Lowest scorer
highest=np.argmax(total)
lowest=np.argmin(total)
print("Highest scorer:\n",highest+1,"with total marks:",total[highest])
print("Lowest scorer:\n",lowest+1,"with total marks:",total[lowest])
print()

