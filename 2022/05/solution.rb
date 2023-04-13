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
        grid_input = input.lines[0..break_point-1].map{ |line| line.gsub("\n", "") }
        instructions_input = input.lines[break_point+1..].map{ |line| line.strip }

        grid = parse_grid(grid_input)
        instructions = parse_instructions(instructions_input)
        return grid, instructions
    end

    def parse_grid(grid_input)
        grid_len = (grid_input[0].length / 4.0).ceil()
        grid = Array.new(grid_len).map { |e| [] }
        for i in 0..grid_input.length-2
            line = grid_input[grid_input.length - 2 - i]
            for j in 0..line.length / 4
                if line[4 * j + 1] != " "
                    grid[j].append(line[4 * j + 1])
                end
            end
        end
        return grid
    end

    def parse_instructions(instructions_input)
        instrs = Array.new()
        instructions_input.each do |line|
            instr = line.match(/move ([0-9]*) from ([0-9]*) to ([0-9]*)/i).captures
            instr = instr.map { |x| x.to_i }
            instrs.push(instr)
        end
        return instrs
    end

    def print_grid(grid)
        grid.each do |row|
            line = ""
            row.each do |char|
                line += char == "" ? " " : char
            end
            puts line
        end
    end

    def process_move(move, grid)
        num, start, stop = move
        start -= 1
        stop -= 1

        for i in 0..num-1
            grid[stop].push(grid[start].pop())
        end
    end

    def process_move_part_two(move, grid)
        num, start, stop = move
        start -= 1
        stop -= 1

        len = grid[start].length
        grid[stop] += grid[start][len-num..]
        grid[start] = grid[start][0..len-num-1]
    end    

    def part_one(input)
        grid, instructions = parse_input(input)

        instructions.each do |move|
            process_move(move, grid)
        end

        # print_grid(grid)

        result = ""
        grid.each do |line|
            result += line.pop()
        end
        return result
    end

    def part_two(input)
        grid, instructions = parse_input(input)

        instructions.each do |move|
            process_move_part_two(move, grid)
        end

        # print_grid(grid)

        result = ""
        grid.each do |line|
            result += line.pop()
        end
        return result
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"