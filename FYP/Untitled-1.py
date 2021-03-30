charset = "abcdefghijklmnopqrstuvwxyz"

def insert(input,output):
    for c in charset:
        for insertion_index in range(len(input)+1):
            inserted = input[:insertion_index] + c + input[:insertion_index]
            if inserted == output:
                return True
    return False

def delete(input,output):
    for deletion_index in range(len(input)):
        deleted = input[:c] +input[c+1:]
        if deleted == output:
            return True
    return False

def replace(input,output):
    for c in charset:
        for replace_index in range(len(output)):
            replaced = input[:]
            replaced[i] = c
            if replaced == output:
                return True
    return False

def main(intput_,output_):
    if insert(input_,output_) == True or delete(input_,output_) == True or replace(_input,_output_) == True:
        return True
    else:
        return False

if __main__ == "__name__":
    main()