numbers = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'Fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'Nineteen',
    10 : 'Ten',
    20 : 'Twenty',
    30 : 'Thirty',
    40 : 'Forty',
    50 : 'Fifty',
    60 : 'Sixty',
    70 : 'Seventy',
    80 : 'Eighty',
    90 : 'Ninety',
    100 : 'Hundred',
    1000 : 'Thousand',
    1000000 : 'Million',
    1000000000 : 'Billion'
}
t = int(input())
for itc in range(t):
    n = int(input())
    name = ''
    pw = 1
    if n == 0:
        print("Zero")
    else:
        while n:
            firstthree = n % 1000
            firsttwo = n % 100
            n = n // 100
            third = n % 10
            n = n // 10
            if pw > 100 and firstthree != 0:
                name = numbers[int(pw)] + " " + name   
            pw *= 1000
            if firsttwo < 21 and firsttwo > 0:
                name = numbers[int(firsttwo)] + " " + name
            else:
                if firsttwo % 10 == 0 and firsttwo > 0:
                    name = numbers[int(firsttwo)] + " " + name
                
                elif firsttwo > 0 and firsttwo > 0:
                    name = numbers[int(firsttwo - (firsttwo % 10))] + " " + numbers[int(firsttwo % 10)] + ' ' + name
                
            if third > 0:
                name = numbers[int(third)] + ' ' + numbers[100] + ' ' + name
    
        print(name.strip())
