def compute_1x2x(N):
    
    return(1 if N == 1 else N * compute_1x2x(N - 1));

print(f"1x2x...xN = {compute_1x2x(int(input("Input: ")))}");
