class AOCClass
    def priority(x)
        return x.ord - 96 > 0 ? x.ord - 96 : x.ord - 38
    end

    def part_one(input)
        sum = 0
        input.each_line do |line|
            mid = line.length / 2
            left, right = line[0..mid-1], line[mid..line.length-1]

            left_chars = {}
            left.each_char do |c|
                left_chars[c] = 1
            end

            found = nil
            right.each_char do |c|
                if left_chars[c] == 1
                    found = c 
                    break
                end
            end

            sum += priority(found)
        end

        return sum
    end

    def part_two(input)
        lines = input.split("\n")
        sum = 0
        for i in 0..(lines.length / 3 - 1)
            first = lines[3 * i]
            second = lines[3 * i + 1]
            third = lines[3 * i + 2]
            found = nil

            first_chars = {}
            first.each_char do |c|
                first_chars[c] = 1
            end

            union_first_second = {}
            second.each_char do |c|
                if first_chars[c] == 1
                    union_first_second[c] = 1
                end
            end

            third.each_char do |c|
                if union_first_second[c] == 1
                    found = c 
                    break
                end
            end

            sum += priority(found)
        end
        return sum
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"