#This program reads the test scores from a CSV file and
#calculate each student's test average.

def main():
    #Open the file.
    csv_file = open('/Users/leslyesirena/Desktop/Python/m7 Class exercise #7a Strings_#4_test_scores.csv', 'r')

    #Read the file's lines into a list.
    lines = csv_file.readlines()

    #close the file.
    csv_file.close()

    #process the lines.
    for line in lines:
        #get the test scores as tokens.
        tokens = line.split(',')

        #calculate the total of the test scores.
        total = 0.0
        for token in tokens:
            total += float(token)

        #calculate the average of the test scores.
        average = total / len(tokens)
        print(f'Average: {average}')

#execute the main function.
if __name__ == '__main__':
    main()