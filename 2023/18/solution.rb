class AOCClass
    def parse(input)
        @instructions = []
        input.split("\n").each do |line|
            parts = line.split(" ")
            color = parts[2].gsub("(", "").gsub(")", "")
            @instructions.push([parts[0], parts[1].to_i, color])
        end
    end

    def get_max_dims
        i, j = 0, 0
        max_down, max_left, max_up, max_right = 0, 0, 0, 0
        @instructions.each do |dir, num_steps, color|
            if dir == "U"
                i -= num_steps
                if i < max_up
                    max_up = i
                end
            elsif dir == "D"
                i += num_steps
                if i > max_down
                    max_down = i
                end
            elsif dir == "L"
                j -= num_steps
                if j < max_left
                    max_left = j 
                end
            elsif dir == "R"
                j += num_steps
                if j > max_right
                    max_right = j
                end
            end
        end
        [max_down, max_left, max_up, max_right]
    end

    def get_path
        path = []
        @max_down, @max_left, @max_up, @max_right = get_max_dims
        i, j = @max_up.abs, @max_left.abs
        @grid = Array.new(@max_down+@max_up.abs+2) {Array.new(@max_left.abs+@max_right+2, '.')}
        @instructions.each do |dir, num_steps, color|
            if dir == "U"
                for ii in 0...num_steps
                    i -= 1
                    path.append([i, j])
                    @grid[i][j] = "#"
                end
            elsif dir == "D"
                for ii in 0...num_steps
                    i += 1
                    path.append([i, j])
                    @grid[i][j] = "#"
                end
            elsif dir == "L"
                for ii in 0...num_steps
                    j -= 1
                    path.append([i, j])
                    @grid[i][j] = "#"
                end
            elsif dir == "R"
                for ii in 0...num_steps
                    j += 1
                    path.append([i, j])
                    @grid[i][j] = "#"
                end
            end
        end
        path
    end

    def fill_left(x, y)
        i, j_idx = x, y
        while true
            j_idx -= 1
            if @grid[i][j_idx] == "#"
                break
            end
            @filled_grid[i][j_idx] = "#"
        end

    end

    def fill_right(x, y)
        i, j_idx = x, y
        while true
            j_idx += 1
            if @grid[i][j_idx] == "#"
                break
            end
            @filled_grid[i][j_idx] = "#"
        end
    end

    def is_in_grid(x, y)
        num_y_crosses = 0
        state = "searching"
        enter_shape = nil
        for j in 0..y
            val = @grid[x][j]
            if val == "#"
                if state != "on-edge"
                    state = "on-edge"
                    enter_shape = @grid[x][j+1] == "#" ? nil : "|"
                    enter_shape = enter_shape.nil? ? (@grid[x+1][j] == "#" ? "D" : "U") : enter_shape
                end
            elsif state == "on-edge"
                state = "searching"
                enter = nil
                exit_shape = @grid[x+1][j-1] == "#" ? "D" : "U"
                if enter_shape == "|" || enter_shape != exit_shape
                    num_y_crosses += 1
                end
            end
        end

        num_x_crosses = 0
        state = "searching"
        for i in 0..x
            val = @grid[i][y]
            # puts "i,y: #{i}, #{y}, #{state}, #{val}"
            if val == "#"
                if state != "on-edge"
                    state = "on-edge"
                    enter_shape = @grid[i+1][y] == "#" ? nil : "-"
                    enter_shape = enter_shape.nil? ? (@grid[i][y+1] == "#" ? "L" : "R") : enter_shape
                end
            elsif state == "on-edge"
                state = "searching"
                exit_shape = @grid[i-1][y+1] == "#" ? "L" : "R"
                if enter_shape == "-" || enter_shape != exit_shape
                    num_x_crosses += 1
                end
            end
        end
        return (num_x_crosses % 2) == 1 && (num_y_crosses % 2) == 1
    end

    def fill_grid
        @filled_grid = Marshal.load(Marshal.dump(@grid))
        i, j = @max_up.abs, @max_left.abs

        @instructions.each do |dir, num_steps, color|
            if dir == "L"
                j -= num_steps
            elsif dir == "R"
                j += num_steps
            elsif dir == "D"
                left_in_grid = is_in_grid(i+1, j-1)
                for ii in 0..num_steps
                    if left_in_grid
                        fill_left(i+ii, j)
                    else
                        fill_right(i+ii, j)
                    end
                end

                i += num_steps
            elsif dir == "U"
                left_in_grid = is_in_grid(i-1, j-1)
                for ii in 0..num_steps
                    if left_in_grid
                        fill_left(i-ii, j)
                    else
                        fill_right(i-ii, j)
                    end
                end
                i -= num_steps
            end
        end
    end

    def print_grid
        @grid.each do |line|
            line = line.join("")
            puts line
        end
    end

    def print_filled_grid
        @filled_grid.each do |line|
            line = line.join("")
            puts line
        end
    end

    def count_filled
        @filled_grid.reduce(0) do  |acc, row| 
            acc + row.reduce(0) {|row_sum, elt| row_sum + (elt == "#" ? 1 : 0)}
        end
    end

    def part_one(input)
        parse(input)
        path = get_path
        # print_grid
        fill_grid
        return count_filled()
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