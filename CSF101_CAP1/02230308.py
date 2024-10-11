file_path = '02230308.txt'
# opens the file and read its content
with open(file_path) as file:
    Data = file.readlines()

names = []
scores = []

for line in Data:
    
    name,score = line.split(',')# split by comma
    names.append(name)
    scores.append(int(score))# convert score to an integer


# bubble sort function
def bubble_sort(name, score):
    n = len(score)

    for i in range(n):
        for j in range(0, n-i-1):

            if score[j] > score[j+1]:
                score[j], score[j+1] = score[j+1], score[j]
               
                name[j], name[j+1] = name[j+1], name[j]

            
    return name,score

y = bubble_sort(names,scores)
print(y)

combined_list = list(zip(names,scores))
print(combined_list[0][1])
# insertion sort function
def insertion_sort(name, score):
    n = len(score)

    for i in range(1, n):
        key_score = score[i]
        key_name = name[i]
        j = i-1

        while j>=0 and score[j] > key_score:
            score[j+1] = score[j]
            name[j+1] = name[j]
            j-=1

        score[j+1] = key_score
        name[j+1] = key_name

insertion_sort(names, scores)
print("sorted names and scores:")
for name, score in zip(names, scores):
    print(f"{name}: {score}")

def linear_search(scores, target_score):
    for i in range(len(scores)):
        if scores[i] == target_score:
            return names[i]
    return None


def binary_search(scores, target_score):
    low = 0
    high = len(scores) - 1

    while low <= high:
        mid = (low + high) // 2
        if scores[mid] == target_score:
            return names[mid]
        elif scores[mid] < target_score:
            low = mid + 1
        else:
            high = mid - 1

    return None
# user input
target_score_input = input("Enter the score:")

target_score = int(target_score_input)
# perform linear search
found_name_linear = linear_search(scores, target_score)
if found_name_linear:
    print(f"Linear Search: '{found_name_linear}': {target_score}")
else:
    print(f"Linear Search: No student found with score {target_score}.")

# perform binary search
found_name_binary = binary_search(scores, target_score)
if found_name_binary:
    print(f"Binary Search: '{found_name_binary}': {target_score}")
else:
    print(f"Binary Search: No student found with score {target_score}.")

linear_search_result = "Linear Search: Please enter a valid integer score."
binary_search_result = "Binary Search: Please enter a valid integer score."


def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

average_score = calculate_average(scores)
print(f"\nAverage Score: {average_score:.2f}")

lowest_score = min(scores)
highest_score = max(scores)

students_with_lowest_score = [names[i] for i in range(len(scores)) if scores[i] == lowest_score]
students_with_highest_score = [names[i] for i in range(len(scores)) if scores[i] == highest_score]
# write results to Output.txt
with open('Output.txt', 'w') as output_file:
    output_file.write(f"Average Score: {average_score:.2f}\n\n")
    # write sorted names and scores
    output_file.write("Sorted Students and Scores:\n")
    for name, score in zip(names, scores):
        output_file.write(f"{name}: {score}\n")
    # write search results
    output_file.write("\nSearch Results:\n")
    output_file.write(linear_search_result + "\n")
    output_file.write(binary_search_result + "\n")
    # write lowest and highest score results
    output_file.write("\nStudents with lowest score:\n")
    output_file.write(", ".join(students_with_lowest_score) + f" (score: {lowest_score})\n")

    output_file.write("\nStudents with highest score:\n")
    output_file.write(", ".join(students_with_highest_score) + f" (score: {highest_score})\n")

print("\nResults written to Output.txt")


