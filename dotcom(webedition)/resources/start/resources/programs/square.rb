system "clear"

class Square

    def initialize(sideLength)
        @sideLength = sideLength
    end

    def getSideLength
            return @sideLength
    end

    def setSideLength(sideLength)
        @sideLength = sideLength
    end

    def perimeter
        return @Perimeter = @sideLength * 4
    end

    def area
        return @sideLength * @sideLength
    end

    def drawSquare
        puts "*" * @sideLength

        (@sideLength - 2).times do
            puts "*" + (" " * (@sideLength -2)) + "* \n"
        end
        puts "*" * @sideLength
    end

    def to_s
        print "Side length:"
        puts @sideLength
        print "Perimeter: "
        puts @perimeter
        print "area: "
        puts @area
    end

end

square1 = Square.new(3)
square2 = Square.new(50) # The side length will not stay as 50

square2.setSideLength(5) # The side length is no longer 50 but 15

# puts "======================="
# print square1.getSideLength
# puts " is the side length of square one"
# print "The perimeter is "
# puts square1.perimeter
# print "The are is "
# puts square1.area
# puts "======================="
# print square2.getSideLength
# puts " is the side length of square two"
# print "The perimeter is "
# puts square2.perimeter
# print "The are is "
# puts square2.area
# puts "======================="

puts square1.drawSquare

