def compute_elves(input)
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
    if current_elf != 0
        elves.push(current_elf)
        current_elf = 0
    end
    return elves
end

def part_one(input)
    elves = compute_elves(input)
    return elves.max
end

def part_two(input)
    elves = compute_elves(input)
    top_three = [0, 0, 0]
    min_idx = 0
    min_val = 0
    elves.each do |elf|
        if elf > min_val
            top_three[min_idx] = elf
            min_val, min_idx = top_three.each_with_index.min
        end
    end
    return top_three.sum
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
puts "Part one: #{part_one(input)}"
puts "Part two: #{part_two(input)}"

