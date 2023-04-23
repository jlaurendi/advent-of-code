class AOCClass
    def part_one(input)
        for i in 0..input.length-4
            chars = {}
            s = input[i..i+3]
            s.each_char do |c|
                chars[c] = 1
            end
            if chars.count == 4
                break 
            end
        end
        return i+4
    end

    def part_two(input)
        for i in 0..input.length-14
            chars = {}
            s = input[i..i+13]
            s.each_char do |c|
                chars[c] = 1
            end
            if chars.count == 14
                break 
            end
        end
        return i+14
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"


# part one
# 1286 too low