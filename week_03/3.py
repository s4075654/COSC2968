def prompt_user_to_enter_a_positive_number():
    N = int(input("Enter a positive number, called N: "));
    
    return(N);

def prompt_the_user_to_enter_n_numbers(N):
    n_numbers = [float(input("Enter number: ")) for number in range(0,  N)];
    
    return(n_numbers);

def the_maximum_of_the_N_numbers_entered(n_numbers):
    
    return(max(n_numbers));

print(f"The maximum of the N numbers entered: {the_maximum_of_the_N_numbers_entered(prompt_the_user_to_enter_n_numbers(prompt_user_to_enter_a_positive_number()))}");
