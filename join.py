import sys 
import csv

def column_check(columns_list, column_name):
    """"
    Function column_check returns indices of the column_name.
    Takes two parameters:
    -columns_list - list of columns names
    -column_name - name of column which being searched for
    """
    for i,word in enumerate(columns_list):
        if(word == column_name):
            return(i)

    sys.exit(f'There is no column named: {column_name}!')

def inner_join(file_1,file_2,column_name):
    """"
    Function inner_join make inner join on two given files and takes 3 arguments: 
    -file_1 - path to the file
    -file_1 - path to the file
    -column_name - the name of the column on which join is to be made
    """
    csv_file_1 = csv.reader(file_1, delimiter=',')
    csv_file_2 = csv.reader(file_2, delimiter=',')

    index_1=column_check(next(csv_file_1),column_name)
    index_2=column_check(next(csv_file_2),column_name)

    file_2.seek(0)
    file_1.seek(0)
    
    for row_1 in csv_file_1:
        for row_2 in csv_file_2:
            if(row_1[index_1] == row_2[index_2]):
                row_2.pop(index_2)
                print(f'{",".join(row_1)},{",".join(row_2)}')
        
        file_2.seek(0)



def left_join(file_1,file_2,column_name):
    """"
    Function left_join make left join on two given files and takes 3 arguments: 
    - file_1 - path to the file
    - file_1 - path to the file
    - column_name - the name of the column on which join is to be made
    """
    csv_file_1 = csv.reader(file_1, delimiter=',')
    csv_file_2 = csv.reader(file_2, delimiter=',')

    index_1=column_check(next(csv_file_1),column_name)
    index_2=column_check(next(csv_file_2),column_name)

    file_2.seek(0)
    file_1.seek(0)
    

    for row_1 in csv_file_1:
        matching=False
        for row_2 in csv_file_2:
            if(row_1[index_1] == row_2[index_2]):
                matching=True
                break

        row_2.pop(index_2)

        if(matching):
            print(f'{",".join(row_1)},{",".join(row_2)}')
        else:
            string=len(row_2)*',NULL'
            print(f'{",".join(row_1)}{string}')
        
        file_2.seek(0)




def right_join(file_1,file_2,column_name):
    """"
    Function right_join make right join on two given files and takes 3 arguments: 
    - file_1 - path to the file
    - file_1 - path to the file
    - column_name - the name of the column on which join is to be made
    """
    left_join(file_2,file_1,column_name)
   

def main():

    if(len(sys.argv) < 3 or len(sys.argv) > 5 ):
        sys.exit("Invalid number ofr arguments!\n")
    
    file_path_1 = sys.argv[1]
    file_path_2 = sys.argv[2]
    column_name = sys.argv[3]


    #By default join_type being set on inner_join
    join_type = "inner" if (len(sys.argv) == 4) else sys.argv[4]

    #Choosing the type of the join
    join_type={
        "inner": inner_join,
        "left": left_join,
        "right": right_join
    }[join_type]
    
    try:
        with open(file_path_2, newline='') as file_2, open(file_path_1, newline='') as file_1:
            join_type(file_1,file_2,column_name)
    except FileNotFoundError as exception:
        print(exception)



if __name__ == "__main__":
    main()
