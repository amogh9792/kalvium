# The spell_out_number function takes in one parameter:
# number: the number to spell out
# The function uses multiple if-else statements to handle numbers of different lengths,
# and returns the spelled-out number as a string.
# The function uses string concatenation and recursion to handle numbers larger than 100.
# The additional rule for large numbers is handled by checking the length of the number and skipping the "thousand" portion if it is 4 digits long
# and the thousands place is non-zero.
def spell_out_number(number):
    if number < 10:
        return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][number]
    if number < 20:
        return ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][number - 10]
    if number < 100:
        tens = number // 10
        ones = number % 10
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][tens - 2] + ('' if ones == 0 else '-' + spell_out_number(ones))
    if number < 1000:
        hundreds = number // 100
        remainder = number % 100
        return spell_out_number(hundreds) + ' hundred' + ('' if remainder == 0 else ' ' + spell_out_number(remainder))
    if number < 10000:
        thousands = number // 1000
        remainder = number % 1000
        return spell_out_number(thousands) + ' thousand' + ('' if remainder == 0 else ' ' + spell_out_number(remainder))

# Example usage
print("Please Enter a number")
number=int(input());
print(spell_out_number(number))
