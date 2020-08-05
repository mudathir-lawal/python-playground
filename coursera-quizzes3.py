def add_divisors_of(number):
    divisor = 1    
    divisor_sumation = 0
    divisor_equals_number = divisor == number
    is_divisor = divisor <= number and number % divisor == 0

    while is_divisor:
        if divisor_equals_number:
        divisor += 1
        break
    sum += divisor
    divisor += 1

    return divisor_sumation  

## Test code:          
print(add_divisors_of(36))

======

def add_divisors_of(number):
    divisor = 1    
    divisor_sumation = 0
    divisor_equals_number = divisor == number
    is_divisor = divisor <= number and number % divisor == 0

    while is_divisor:
        if divisor_equals_number:
            divisor += 1
            break
        divisor_sumation += divisor
        divisor += 1

    return divisor_sumation  

## Test code:          
print(add_divisors_of(36))
===
def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  divisor = 1

  while ( divisor <= n ) and ( ( n % divisor ) == 0 ):
    if divisor == n:
      divisor = divisor + 1
      break
    sum = sum + divisor
    divisor = divisor + 1

  return sum


print(sum_divisors(5))
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
=====



def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  divisor = 1
  
  while divisor < n:
      if n % divisor != 0:
          divisor += 1
          continue
      sum += divisor
      divisor += 1  

  return sum

=====

def add_divisors_of(number):
    divisor = 1    
    divisor_summation = 0
    iteration_flag = divisor <= number
    is_divisor = number % divisor == 0
    not_divisor = number % divisor != 0
    divisor_equals_number = divisor == number    

    while is_divisor or not_divisor and iteration_flag:
        if is_divisor:
            divisor_summation += divisor            
        divisor += 1

    return divisor_summation  

## Test code:          
print(add_divisors_of(36))
# if not_divisor or divisor_equals_number:

=====
def sum_divisors(n):

  sum = 0
  divisor = 1
  # Return the sum of all divisors of n, not including n
 
  while divisor < n:
    if n % divisor == 0:
        sum += divisor
        divisor += 1
    else:
        divisor += 1

  return sum

print(sum_divisors(0))   # 0 => 0
print(sum_divisors(5))   # 1 => 1
print(sum_divisors(3))   # 1 => 1
print(sum_divisors(36))  # 1+2+3+4+6+9+12+18 => 55
print(sum_divisors(102)) # 1+2+3+6+17+34+51  => 114
======



def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

def factorial(n):
    result = 1
    for i in range(1, n):
        result *= n
        n -= 1
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120



def get_same_val_indicies(list1, list2):
	same_val_indicies = []
	for value in 
	list1[n] == 



function getSameValueIndicies( arr1, arr2 ){
	let sameValueIndicies = [];
	for( let m = 0; m < arr1.length; m++ ){
	    for( let n = 0; n < arr2.length; n++ ){
	        if ( arr1[ m ] == arr2[ n ] ){
	            sameValueIndicies.push( n );
	        }
	    }
	}
	return sameValueIndicies;
}

let set1 = [ 'a', 'b', 'c', 'd' ];
    set2 = [ 'c', 'b', 'a', 'd' ];
console.log( getSameValueIndicies( set1, set2 ) );


function getSameValueIndicies( arr1, arr2 ){
	let sameValueIndicies = [];
	for( let n = 0; n < arr1.length; n++ ){
        if ( arr1[ n ] == arr2[ n ] ){
            sameValueIndicies.push( n );
        }
	}
	return sameValueIndicies;
}

let set1 = [ 'a', 'b', 'c', 'd' ];
    set2 = [ 'c', 'b', 'a', 'd' ];
console.log( getSameValueIndicies( set1, set2 ) );


====

def is_valid(usr):
  return len(usr) > 3 or len(usr) == 3

def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users([ "purplecat" ])

=========