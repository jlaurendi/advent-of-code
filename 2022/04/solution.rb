class AOCClass
    def parse_input(input)
        lines = input.split("\n")
        new_lines = []
        lines.each do |line|
            left, right = line.split(',')
            lmin, lmax = left.split('-').map{|x| x.to_i}
            rmin, rmax = right.split('-').map{|x| x.to_i}
            new_lines.push([[lmin, lmax], [rmin, rmax]])
        end

        return new_lines
    end

    def contains(a, b)
        return b[0] >= a[0] && b[1] <= a[1]
    end

    def overlaps(a, b)
        return (a[0] <= b[0] && a[1] >= b[0]) || (a[0] <= b[1] && a[1] >= b[1]) || (a[0] >= b[0] && a[1] <= b[1])
    end

    def part_one(input)
        lines = parse_input(input)
        num_contained = 0
        lines.each do |line|
            a, b = line
            if contains(a, b) || contains(b, a)
                num_contained += 1
            end
        end
        return num_contained
    end

    def part_two(input)
        lines = parse_input(input)
        num_overlapping = 0
        lines.each do |line|
            a, b = line
            if overlaps(a, b)
                num_overlapping += 1
            end
        end
        return num_overlapping
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"


# part two
# 715 too low