def main():
    #write your code below this line

    sumOfNumbers = 0

    while True:
      number = int(input("Give a number: "))

      if(number == 0):
        break
      
      if(number != 0):
        sumOfNumbers = sumOfNumbers + number
      
    print("Sum of the number: " + str(sumOfNumbers))

if __name__ == '__main__':
    main()
