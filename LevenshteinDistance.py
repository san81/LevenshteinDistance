class LvnDistance:
    """Class for calculating the Levenshtein Distance"""
    dictionary = ["Bombay","Mumbai","Calcutta","Pune","Madras","Hyderabad","Delhi","Goa"]


    def minValue(instance, a,  b,  c):
        temp = None
        if a<b:
            temp=a
        else:
            temp=b
        if temp<c:
            return temp
        else:
            return c
    
    def printMatrix(instance, matrix):
        mprint = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mprint+=(str(matrix[i][j])+" ")
            mprint+="\n"    
        print(mprint)

    def levenshteinEditDistance(instance, inputChar, wordChar):
        inputCharLengh=(len(inputChar)+1)
        wordLengh=(len(wordChar)+1)
        matrix = [ [ 0 for y in range( wordLengh ) ] for x in range( inputCharLengh ) ]
        #Add the first row and column to the matrix
        for i in range(0,len(matrix[0])):
            matrix[0][i] = i

        for i in range(0, len(matrix)):
            matrix[i][0] = i
       
        for i in range(1,inputCharLengh):
            for j in range(1,wordLengh):
                if inputChar[i-1] == wordChar[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = instance.minValue(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
        instance.printMatrix(matrix)    
        return matrix[len(inputChar)][len(wordChar)]

    def autoCorrectByDistance(instance,word):
        distances = [ None for x in range(len(instance.dictionary))]
        inputChar = list(word)
        minValue = 10000
        minIndex = 0
        for i in range(0, len(instance.dictionary)):
            dictChar = list(instance.dictionary[i])
            print("Sending=>D: "+str(inputChar)+" W:"+str(dictChar))
            distance = instance.levenshteinEditDistance(inputChar, dictChar)
            print("D: "+str(distance)+" W:"+word)
            distances[i] = distance
            if distance < minValue:
                minValue = distance
                minIndex = i
            
        return instance.dictionary[minIndex]

lvnDistanceObj = LvnDistance()
autoCorrected=lvnDistanceObj.autoCorrectByDistance('Mad')
print(autoCorrected)
