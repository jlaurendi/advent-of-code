class AOCClass
    def part_one(input)
        return "incomplete"
    end

    def part_two(input)
        return "incomplete"
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"