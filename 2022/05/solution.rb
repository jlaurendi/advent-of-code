class AOCClass
    def parse_input(input)
        break_point = 0
        i = 0
        input.each_line do |line|
            if line.strip == ""
                break_point = i 
                break
            end
            i += 1 
        end
        grid = input.lines[0..break_point-1].map{ |line| line.gsub("/\n/", "") }
        instructions = input.lines[break_point..].map{ |line| line.strip }
        return grid, instructions
    end

    def part_one(input)
        grid, instructions = parse_input(input)
        puts grid.inspect
        # puts instructions.inspect
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