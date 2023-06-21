class AOCClass
    attr_reader :curr_cycle

    def initialize
        @curr_cycle = 1
        @cycles_to_sum = [20, 60, 100, 140, 180, 220]
        @registerX = 1
        @answer = 0
        @grid = [[], [], [], [], [], [], [], [], [], []]
    end

    def parse_input(input)
        instructions = []
        input.each_line do |line|
            args = line.split(" ")
            if args[0] == "noop"
                instructions.append([args[0]])
            elsif args[0] == "addx"
                instructions.append([args[0], args[1].to_i])
            end
        end
        instructions
    end

    def process_one_step(instruction)
        step = instruction[0] == "noop" ? 1 : 2
        start_cycle = @curr_cycle
        end_cycle = @curr_cycle + step
        # puts instruction.inspect, start_cycle, end_cycle, @registerX
        @cycles_to_sum.each do |x|
            if x >= start_cycle and x < end_cycle
                # puts "#{x} #{@registerX}"
                @answer += @registerX * x
                break
            end
        end

        if instruction[0] == "addx"
            @registerX += instruction[1]
        end
        @curr_cycle = end_cycle
    end

    def process_one_step_pt2(instruction)
        step = instruction[0] == "noop" ? 1 : 2
        start_cycle = @curr_cycle
        end_cycle = @curr_cycle + step

        (start_cycle...end_cycle).step(1) do |n|
            puts "Processing cycle #{n} #{instruction[0]} #{instruction[1]}"
            row = (n - 1) / 40
            col = (n - 1) % 40 + 1
            if (col - 1 - @registerX).abs() <= 1
                next_char = '#'
            else
                next_char = '.'
            end
            puts "row: #{row} col: #{col} x: #{@registerX} next_char: #{next_char}"
            @grid[row].append(next_char)

            @curr_cycle += 1
        end

        if instruction[0] == "addx"
            @registerX += instruction[1]
        end
    end

    def print_grid()
        @grid.each do |row|
            puts row.join('')
        end
    end

    def part_one(input)
        @curr_cycle = 1
        instructions = parse_input(input)
        instructions.each do |instr|
            process_one_step(instr)
        end
        return @answer
    end

    def part_two(input)
        @curr_cycle = 1
        @registerX = 1
        instructions = parse_input(input)
        instructions.each do |instr|
            process_one_step_pt2(instr)
        end
        print_grid
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"