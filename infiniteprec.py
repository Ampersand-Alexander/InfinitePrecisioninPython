#Alexander Tran 890639255
#Bruce Mckenzie CPSC 462 

class highprecision:
    #will give memory error: digits cannot exceede ~9,223,372,036,854,775,758 digits on a 64 bit system
    #digits tested around 56,854,775,756 digits, very long wait times though.
    #will truncate at limits of Max digits, does not round

    MAX_DIGITS = 100

    def __init__(self, num):
        
        if isinstance(num, str) or isinstance(num, int) or isinstance(num, float):
            #type cast string input int and float
            self.string_num = str(num)
            #permanently increase max digits for negative sign and decimal point
            self.MAX_DIGITS = self.MAX_DIGITS

            self.numberistoobigcheck(num)
            self.initString()

        elif isinstance(num, highprecision):
            #just copy over parameters
            # self.digits = num.digits
            self.string_num = num.string_num
            self.splitted = num.splitted
            self.non_decimal_part = num.non_decimal_part
            self.decimal_part = num.decimal_part
            self.negative = num.negative

    def numberistoobigcheck(self, num):
        if len(str(num))>self.MAX_DIGITS:
            pass
            print("length greater than max digits which is ", self.MAX_DIGITS," digits, results will only be accurate to that")
            # quit() #its not worth truncating, there serves no point as it would not be an accurate calculator

    def initString(self):
        
        #determine if its negative and store
        if self.string_num[0] == '-':
            self.negative = True
            self.string_num = self.string_num[1:]
        else:
            self.negative = False

        #split the string into whole and decimal number
        self.splitted = self.string_num.split('.')
    
        #determine if it is a decimal and store
        if len(self.splitted)>1:
            self.non_decimal_part = str(self.splitted[0])
            self.decimal_part = str(self.splitted[1])
        else:
            self.non_decimal_part = str(self.splitted[0])
            self.decimal_part = "0"

    def __str__(self):
        if self.decimal_part.count("0") == len(self.decimal_part):
            if self.non_decimal_part.count("0")== len(self.non_decimal_part):
                self.decimal_part="0"
                self.non_decimal_part="0"
                s = str(self.non_decimal_part)+"."+str(self.decimal_part)
                #0.0
            else:
                self.decimal_part="0"
                s = str(self.non_decimal_part)+"."+str(self.decimal_part)
                #x.0
        else:
            if self.non_decimal_part.count("0")==len(self.non_decimal_part):
                self.non_decimal_part="0"
                s = str(self.non_decimal_part)+"."+str(self.decimal_part).rstrip("0")
                #0.x
            else:
                s = str(self.non_decimal_part).lstrip("0")+"."+str(self.decimal_part).rstrip("0")
                #x.x

        if self.non_decimal_part == "0" and self.decimal_part == "0":
            self.negative = False
        else:
            if self.negative:
                s = '-' + s
        return s

    def __eq__(self, other):
        return str(self) == str(other)
    
    def __ne__(self, other):
        return str(self) != str(other)
    
    def __gt__(self, other):
        #gt is working
        if len(self.non_decimal_part) > len(other.non_decimal_part):
            return True
        elif len(self.non_decimal_part) < len(other.non_decimal_part):
            return False
        else:
            for i in range(len(self.non_decimal_part)):
                diff = int(self.non_decimal_part[i]) - int(other.non_decimal_part[i])
                if diff==0:
                    continue 
                if diff < 0:
                    return False
                if diff > 0:
                    return True
            if(self.decimal_part != other.decimal_part):
                if(len(self.decimal_part)>len(other.decimal_part)):
                    differenceDecimal = len(self.decimal_part)-len(other.decimal_part)
                    other.decimal_part = other.decimal_part + "0"*(differenceDecimal)

                if(len(self.decimal_part)<len(other.decimal_part)):
                    differenceDecimal = len(other.decimal_part)-len(self.decimal_part)
                    self.decimal_part = self.decimal_part + "0"*(differenceDecimal)
                
            for i in range(len(self.decimal_part)):
                diff = int(self.decimal_part[i]) - int(other.decimal_part[i])
                if diff==0:
                    continue 
                if diff < 0:
                    self.decimal_part =self.decimal_part.rstrip("0")               
                    other.decimal_part = other.decimal_part.rstrip("0")
                    return False
                if diff > 0:
                    self.decimal_part =self.decimal_part.rstrip("0")
                    other.decimal_part = other.decimal_part.rstrip("0")
                    return True
            self.decimal_part =self.decimal_part.rstrip("0")
            other.decimal_part = other.decimal_part.rstrip("0")
            return False

    def __ge__(self, other):
        if len(self.non_decimal_part) > len(other.non_decimal_part):
            return True
        elif len(self.non_decimal_part) < len(other.non_decimal_part):
            return False
        else:
            for i in range(len(self.non_decimal_part)):
                diff = int(self.non_decimal_part[i]) - int(other.non_decimal_part[i])
                if diff==0:
                    continue 
                if diff < 0:
                    return False
                if diff > 0:
                    return True
            if(self.decimal_part != other.decimal_part):
                if(len(self.decimal_part)>len(other.decimal_part)):
                    differenceDecimal = len(self.decimal_part)-len(other.decimal_part)
                    other.decimal_part = other.decimal_part + "0"*(differenceDecimal)

                if(len(self.decimal_part)<len(other.decimal_part)):
                    differenceDecimal = len(other.decimal_part)-len(self.decimal_part)
                    self.decimal_part = self.decimal_part + "0"*(differenceDecimal)
                
            for i in range(len(self.decimal_part)):
                diff = int(self.decimal_part[i]) - int(other.decimal_part[i])
                if diff==0:
                    continue 
                if diff < 0:
                    self.decimal_part =self.decimal_part.rstrip("0")
                    other.decimal_part = other.decimal_part.rstrip("0")
                    return False
                if diff > 0:
                    self.decimal_part =self.decimal_part.rstrip("0")
                    other.decimal_part = other.decimal_part.rstrip("0")
                    return True
            return True

    def __lt__(self, other):
        if other > self:
            return True
        else:
            return False

    def __le__(self, other):
        if other >= self:
            return True
        else:
            return False

    def equalizespaces(self,other):
        #equalize self and other non decimal spaces
        if(self.non_decimal_part != other.non_decimal_part):
            if(len(self.non_decimal_part)>len(other.non_decimal_part)):
                differencenonDecimal = len(self.non_decimal_part)-len(other.non_decimal_part)
                other.non_decimal_part =  "0"*(differencenonDecimal)+other.non_decimal_part

            if(len(self.non_decimal_part)<len(other.non_decimal_part)):
                differencenonDecimal = len(other.non_decimal_part)-len(self.non_decimal_part)
                self.non_decimal_part = "0"*(differencenonDecimal)+self.non_decimal_part 
                
        if(self.decimal_part != other.decimal_part):
            if(len(self.decimal_part)>len(other.decimal_part)):
                differenceDecimal = len(self.decimal_part)-len(other.decimal_part)
                other.decimal_part = other.decimal_part + "0"*(differenceDecimal)

            if(len(self.decimal_part)<len(other.decimal_part)):
                differenceDecimal = len(other.decimal_part)-len(self.decimal_part)
                self.decimal_part = self.decimal_part + "0"*(differenceDecimal)

    def balancestring(string1, string2):
        if len(string1) > len(string2):
            #increase string2
            string2 = "0"*(len(string1)-len(string2)) + string2
        elif len(string1) < len(string2):
            string1 = "0"*(len(string2)-len(string1)) + string1
        return string1, string2

    def __add__(self, other):
        result = highprecision(0)
        result.decimal_part=""
        result.non_decimal_part=""
        # a + b   or -a + -b
        if (self.negative == False and other.negative == False) or (self.negative == True and other.negative == True):
            carry = 0
            self.equalizespaces(other)       

            for i in range(len(self.decimal_part)):
                d = int(self.decimal_part[-i-1]) + int(other.decimal_part[-i-1]) + carry
                result.decimal_part = str(d % 10) + result.decimal_part
                carry = d // 10
            for i in range(len(self.non_decimal_part)):
                d = int(self.non_decimal_part[-i-1]) + int(other.non_decimal_part[-i-1]) + carry
                result.non_decimal_part = str(d % 10) + result.non_decimal_part
                carry = d // 10
            result.non_decimal_part = (str(carry) + result.non_decimal_part).lstrip("0")

            result.negative = self.negative
            result.numberistoobigcheck(result.string_num)
            return result
        # a+-b or 
        if (self.negative == False and other.negative == True):
            other.negative=False
            return self.__sub__(other)
        #-a + b
        if (self.negative == True and other.negative == False):
            self.negative=False
            return other.__sub__(self)

    def __sub__(self, other):
        result = highprecision(0)
        result.decimal_part=""
        result.non_decimal_part=""
        #find the absolute difference
        #a-b or # -a - -b
        if (self.negative == False and other.negative == False) or (self.negative == True and other.negative == True):
            self.equalizespaces(other)
            if self > other:
                borrow = 0
                for i in range(len(self.decimal_part)):
                    d = int(self.decimal_part[-i-1]) - int(other.decimal_part[-i-1]) - borrow
                    if d < 0:
                        d += 10
                        borrow = 1
                    else:
                        borrow = 0
                    result.decimal_part = str(d)+result.decimal_part 
                for i in range(len(self.non_decimal_part)):
                    d = int(self.non_decimal_part[-i-1]) - int(other.non_decimal_part[-i-1]) - borrow
                    if d < 0:
                        d += 10
                        borrow = 1
                    else:
                        borrow = 0
                    result.non_decimal_part = str(d)+ result.non_decimal_part
                try:
                    if self.negflag==1:
                        result.negative = False
                    if self.negflag==2:
                        result.negative = True
                except:
                    result.negative = self.negative
                return result
                
            elif (self == other):
                result.negative = False
                return result
            elif (self<other):
                try:
                    if self.negflag:
                        other.negflag=2
                except:
                    other.negflag = 1
                return other.__sub__(self)
        # a - - b 
        if (self.negative == False and other.negative == True):
            other.negative = False
            return self.__add__(other)
        # - a - b
        if (self.negative == True and other.negative == False):
            self.negative = True
            other.negative = True
            return self.__add__(other)

    def __mul__(self, other):
        
        result = highprecision(0)
        x = self.non_decimal_part + self.decimal_part
        y = other.non_decimal_part + other.decimal_part
        # convert numbers into string
        #find out length of the decimal area
        resultdecimallength = len(self.decimal_part)+len(other.decimal_part)

        resultstr = ""
        # looping over y
        for i in range(len(y)):
            carrym = 0  
            carry=0
            inter_res = ""  
            for j in range(len(x) - 1, -1, -1):
                num = int(y[i]) * int(x[j]) + carrym
                if num > 9 and j > 0:
                    inter_res = str(num % 10) + inter_res
                    carrym = num // 10
                # else the digit is append to intermediate result
                # And assign carry as zero
                else:
                    inter_res = str(num) + inter_res
                    carrym = 0
            # Adding the intermediate results
            resultstr = resultstr+"0"
            #resultstr = resultstr + int(inter_res) #ADD TWO STRINGS and put it into resultstr
            #balace string
            inter_res,resultstr=highprecision.balancestring(inter_res,resultstr)

            resultstr1=""
            for i in range(len(inter_res)-1, -1, -1):
                d = int(resultstr[i]) + int(inter_res[i]) + carry
                resultstr1 = str(d % 10) + resultstr1
                carry = d // 10
            
            if carry>0:
                resultstr1=str(carry)+resultstr1
                
            resultstr=resultstr1

        result.decimal_part = resultstr[-resultdecimallength:]
        result.non_decimal_part= resultstr[:-resultdecimallength]

        return result

    def __floordiv__(self, other):
        quotient = highprecision(0)
        num = self
        div = other
        while div <= num:
            quotient = quotient + highprecision(1)
            num = num - div
        return quotient

    def convertWhole(self, other):
        self.equalizespaces(other)
        self.non_decimal_part = str(self.non_decimal_part) + str(self.decimal_part)
        self.decimal_part = "0"
        other.non_decimal_part = str(other.non_decimal_part) + str(other.decimal_part)
        other.decimal_part = "0"

    def movedecplace(self, decplaces, result):
        result.non_decimal_part = result.non_decimal_part + result.decimal_part[:decplaces]
        result.decimal_part = result.decimal_part[decplaces:]
        return result

    def __truediv__(self, other):
        
        #do some negative logic
        if self.negative and other.negative:
            #ans is positive -a -b
            resultspolarity = False
        elif self.negative and not other.negative:
            #ans is negative a -b
            resultspolarity = True
        elif not self.negative and other.negative:
            #ans is negative -a b
            resultspolarity = True
        elif not self.negative and not other.negative:
            #ans is positive -a -b
            resultspolarity = False
        
        #wipe polarity
        self.negative = False
        other.negative = False

        #count decimal places
        
        #make them ints and 
        self.convertWhole(other)
        decplaces = len(other.decimal_part) -1

        # print("conversion", self, other)
        quotient = self//other
        remainder = self % other
        a= highprecision(10)
        surplus_quotient=highprecision(0)

        if remainder != highprecision(0):
            quotient_str = str(quotient).rstrip("0").replace(".","")
            for loop in range(0, self.MAX_DIGITS):
                if loop == 0:
                    quotient_str = quotient_str + "."

                #add 0 to quotient to get ready to add it to the next number
                #print("remainder going into surp", remainder, "a", a, "other", other)
                surplus_quotient = ((remainder * a) // other)
                i=0
                print("suproi las", surplus_quotient," reamndn", ((remainder * a) // other))

                while(surplus_quotient != ((remainder * a) // other)):
                    # very strange behavior here
                    print("HUH? how can this be?", i)
                    print("got", surplus_quotient, "expected", ((remainder * a) // other))
                    print("replacing")
                    surplus_quotient = ((remainder * a) // other)
                    i= i+1
                    if i>1000:
                        print("something very strange happend in div where surplus quo doesnt want to take the value properly")
                        quit()
                    
                    
                quotient_str = quotient_str + str(surplus_quotient).rstrip("0").replace(".", "")
                b= remainder*a
                remainder = b % other

                if remainder == highprecision(0):
                    print("a rational number")
                    result = self.movedecplace(decplaces, highprecision(quotient_str))
                    result.negative = resultspolarity
                    return result
                
                if loop == self.MAX_DIGITS-1:
                    result = self.movedecplace(decplaces, highprecision(quotient_str))
                    result.negative = resultspolarity
                    return result
        else:
            result = self.movedecplace(decplaces, highprecision(quotient))
            result.negative = resultspolarity
            return result
            
    def __mod__(self,other):
        #self on top
        num1 = self
        #other on bottom
        num2 = other
        while(num1 >= num2):
            num1 = num1-num2
            # if num1 < num2:
            #     pass
            #     print("NEW NUM ", num1, num2)
        return num1

    def state(self):
        print("Internal Strings: ", self.non_decimal_part, self.decimal_part, "Negative State: ", self.negative )

class unittesthighPrec():
    def debug():
        a=highprecision(0)
        b=highprecision(0)
        print(a.decimal_part)
        print(a.non_decimal_part)
        print(b.decimal_part)
        print(b.non_decimal_part)

    def testlargestString():
        i=56854775756#where it gets slow for me at least
        while True:
            string1="."*i
            print(i)
            i=i+1

    def unittestComparators():
        #in limits comparison test
        print("starting")
        spinny = "/-\|"
        for i in range(10000):
            a = highprecision(str(0)+"."+str(i))
            for j in range(5000):
                b = highprecision(str(0)+"."+str(j))
                print("testing",spinny[i%4],"    ", i," ",j,"     ", a, b)
                if float("0."+str(i))>float("0."+str(j)):
                    if a>b:
                        continue
                    else:
                        print("something wrong at >")
                        print(i)
                        quit()
                if float("0."+str(i))<float("0."+str(j)):
                    if a<b:
                        continue
                    else:
                        print("something wrong at <")
                        print(i)
                        quit()
                if float("0."+str(i))==float("0."+str(j)):
                    if a == b:
                        continue
                    else:
                        print("something wrong at eq")
                        print(i)
                        print(j)
                        print("a? ", a)
                        print("b? ", b)
                        print(float("0."+str(i)),float("0."+str(j)))
                        print(a, b)
                        quit()
        print("finished")

        a = highprecision(1234.12341)
        b = highprecision(1234.123400)
        print(a<b)

    def unittestStringoutput():
        #not finished
        spinny = "/-\|"

        for i in range(1000):
            a=highprecision(i)
            if (str(i) == a):
                print("testing", spinny[i%4],"    ", i,"     ", a)
    
    def testaddition():
        a=highprecision(1)
        b=highprecision(1)
        print(a,"+",b)
        print(a+b)
        a=highprecision(1.1)
        b=highprecision(1.9)
        print(a,"+",b)
        print(a+b)
        a=highprecision(1.9)
        b=highprecision(1.1)
        print(a,"+",b)
        print(a+b)
        a=highprecision(98.88)
        b=highprecision(1.12)
        print(a,"+",b)
        print(a+b)
        a=highprecision(983213.88425)
        b=highprecision(12421.12)
        print(a,"+",b)
        print(a+b)

    def testsub():
        # a=highprecision(1)
        # b=highprecision(1)
        # print(a,"-",b)
        # print(a-b)
        # a=highprecision(1.1)
        # b=highprecision(1.9)
        # print(a,"-",b)
        # print(a-b)
        # a=highprecision(1.9)
        # b=highprecision(1.1)
        # print(a,"-",b)
        # print(a-b)
        # a=highprecision(98.88)
        # b=highprecision(1.12)
        # print(a,"-",b)
        # print(a-b)
        # a=highprecision(983213.32142)
        # b=highprecision(12421.721)
        # print(a,"-",b)
        # print(a-b)

        #testing negatives
        #-a - b
        # a=highprecision(-983213.32142)
        # b=highprecision(12421.721)
        # print(a,"-",b)
        # print(a-b)
        # #a - -b
        # a=highprecision(983213.32142)
        # b=highprecision(-12421.721)
        # print(a,"-",b)
        # print(a-b)
        #-a - -b
        a=highprecision(-983213.32142)
        b=highprecision(-12421.721)
        print(a,"-",b)
        print(a-b)

        a=highprecision(-1)
        b=highprecision(-2)
        print(a,"-",b)
        print(a-b)

        #testing larger number
        #-a - b
        b=highprecision(-983213.32142)
        a=highprecision(12421.721)
        print(a,"-",b)
        print(a-b)
        #a - -b
        b=highprecision(983213.32142)
        a=highprecision(-12421.721)
        print(a,"-",b)
        print(a-b)
        #-a - -b
        b=highprecision(-983213.32142)
        a=highprecision(-12421.721)
        print(a,"-",b)
        print(a-b)

    def testmult():
        a=highprecision(1)
        b=highprecision(1)
        print(a,"*",b)
        print(a*b)
        a=highprecision(1.1)
        b=highprecision(1.9)
        print(a,"*",b)
        print(a*b)
        a=highprecision(1.9)
        b=highprecision(1.1)
        print(a,"*",b)
        print(a*b)
        # a=highprecision(98.88)
        b=highprecision(1.12)
        print(a,"*",b)
        print(a*b)
        a=highprecision(983213.32142)
        b=highprecision(12421.721)
        print(a,"*",b)
        print(a*b)

    def testdiv():
        # a=highprecision(1)
        # b=highprecision(1)
        # print(a,"/",b)
        # print(a/b)
        # #neg
        # a=highprecision(1)
        # b=highprecision(-1)
        # print(a,"/",b)
        # print(a/b)
        a=highprecision(1)
        b=highprecision(3)
        print(a,"/",b)
        print(a/b)
        # a=highprecision(11.0)
        # b=highprecision(19.0)
        # print(a,"/",b)
        # print(a/b)
        # a=highprecision(1.1)
        # b=highprecision(1.9)
        # print(a,"/",b)
        # print(a/b)
        # a=highprecision(1.9)
        # b=highprecision(1.1)
        # print(a,"/",b)
        # print(a/b)
        # a=highprecision(98.88)
        # b=highprecision(1.12)
        # print(a,"/",b)
        # print(a/b)
        # a=highprecision(983213.32142)
        # b=highprecision(12421.721)
        # print(a,"/",b)
        # print(a/b)
        # #special div case of doom
        # a=highprecision(1)
        # b=highprecision(3)
        # print(a,"/",b)
        # print(a/b)

    def testfloordiv():
        a=highprecision(1)
        b=highprecision(1)
        print(a,"//",b)
        print(a//b)
        a=highprecision(1.1)
        b=highprecision(1.9)
        print(a,"//",b)
        print(a//b)
        a=highprecision(1.9)
        b=highprecision(1.1)
        print(a,"//",b)
        print(a//b)
        a=highprecision(98.88)
        b=highprecision(1.12)
        print(a,"//",b)
        print(a//b)
        a=highprecision(983213.32142)
        b=highprecision(12421.721)
        print(a,"//",b)
        print(a//b)
    
    def testmod():
        a=highprecision(1)
        b=highprecision(1)
        print(a,"%",b)
        print(a%b)
        a=highprecision(1.1)
        b=highprecision(1.9)
        print(a,"%",b)
        print(a%b)
        a=highprecision(1.9)
        b=highprecision(1.1)
        print(a,"%",b)
        print(a%b)
        a=highprecision(5)
        b=highprecision(2)
        print(a,"%",b)
        print(a%b)
        a=highprecision(983213.32142)
        b=highprecision(12421.721)
        print(a,"%",b)
        print(a%b)

class Calculator():
    def __init__(self):
        print("Hello")
        self.mainmenu()

    def mainmenu(self):
        print("________________Menu__________________")
        
        print("1.___________________________Add______")
        
        print("2.____________________________Sub______")
        
        print("3.____________________________Mul_____")
        
        print("4.___________________Greater_Than_____")
        
        print("5.______________________Less Than_____")
        
        print("6._______________________Equal_to_____")

        print("7._____________Greater_Than_or_EQ_____")

        print("8.________________Less_Than_or_EQ_____")
        
        print("9._______________________FloorDiv_____")

        print("10.___________________________Div_____")

        print("11.____________________________MOD_____")

        print("99.___________________________Exit_____")
        try:
            x= int(input("choose an option (1-11, 99 to exit):     "))
        except:
            print("invalid input")
            self.mainmenu()
        if x==1:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x+y)
            self.mainmenu()
        if x==2:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x-y)
            self.mainmenu()
        if x==3:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x*y)
            self.mainmenu()
        if x==4:
            a=input("give me value dividend   ")
            b=input("give me value divisor   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x/y)
            self.mainmenu()
        if x==5:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x>y)
            self.mainmenu()
        if x==6:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x<y)
            self.mainmenu()
        if x==7:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x>=y)
            self.mainmenu()
        if x==8:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x<=y)
            self.mainmenu()
        if x==9:
            a=input("give me value 1 where value1//value2   ")
            b=input("give me value 2 where value1//value2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x//y)
            self.mainmenu()
        if x==10:
            a=input("give me value 1 where value1/value2   ")
            b=input("give me value 2 where value1/value2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x/y)
            self.mainmenu()
        if x==11:
            a=input("give me value 1   ")
            b=input("give me value 2   ")
            x=highprecision(a)
            y=highprecision(b)
            print(x%y)
            self.mainmenu()
        if x==99:
            print("Bye")
            quit()
        else:
            self.mainmenu()

if __name__ == "__main__":
    #unittesthighPrec.unittestComparators()
    #unittesthighPrec.unittestStringoutput()
    #unittesthighPrec.testsub()
    #unittesthighPrec.testmult()
    #unittesthighPrec.testmod()
    unittesthighPrec.testdiv()
    # a=highprecision(10.0)
    # b=highprecision(19)
    # print(a//b)
    # a=highprecision(0.10)
    # b=highprecision(0.1)
    # print(a, b)
    # Calculator()
