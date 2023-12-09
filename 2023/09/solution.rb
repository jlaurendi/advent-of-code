class AOCClass
    def parse_input(input)
        lines = []
        input.each_line do |line|
            lines.push(line.split.map { |x| x.to_i })
        end
        return lines
    end
    
    def all_zero(arr)
        arr.each do |x|
            if x != 0
                return false
            end
        end
        return true
    end

    def calc_history(line)
        seqs = [line]

        while !all_zero(seqs[-1])
            seqs << []

            i = 0
            while i < seqs[-2].length - 1
                # puts seqs.inspect
                seqs[-1].push(seqs[-2][i+1] - seqs[-2][i])
                i += 1
            end
            # puts seqs.inspect
        end
        return seqs
    end

    def calc_val(seqs)
        s = 0
        seqs.each do |seq|
            s += seq[-1]
        end
        return s
    end

    def part_one(input)
        lines = parse_input(input)

        vals = []
        lines.each do |line|
            seqs = calc_history(line)
            vals << calc_val(seqs)
        end

        return vals.sum
    end

    def calc_val2(seqs)
        s = 0
        seqs.reverse.each do |seq|
            s = seq[0] - s
        end
        return s
    end


    def part_two(input)
        lines = parse_input(input)

        vals = []
        lines.each do |line|
            seqs = calc_history(line)
            vals << calc_val2(seqs)
        end

        return vals.sum
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
# puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"

# -2 not right