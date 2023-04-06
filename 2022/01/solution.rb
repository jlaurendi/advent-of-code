def part_one(input)
    # lines = input.split("\n").map(&:to_i)
    current_elf = 0
    elves = []
    input.each_line do |line|
        line = line.strip
        if line.nil? || line.empty? || line == ""
            elves.push(current_elf)
            current_elf = 0
        else
            current_elf += line.to_i
        end
    end
    return elves.max
end

def part_two(input)
    return "<incomplete>"
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
puts "Part one: #{part_one(input)}"
puts "Part two: #{part_two(input)}"

