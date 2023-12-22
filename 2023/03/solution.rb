class AOCClass
    def parse(input)
        @grid = []
        input.each_line do |line|
            @grid.append(line.strip.chars)
        end
    end

    def print_grid
        @grid.each { |row| puts row.join(' ') }
    end

    def check_part_num(x, y)
        for ii in -1..1
            for jj in -1..1
                i = x + ii
                j = y + jj
                # puts "in check_part_num: #{i}, #{j}"
                if i < 0 || i >= @grid.length || j < 0 || j >= @grid[0].length
                    next
                end

                if (@grid[i][j] =~ /[^a-zA-Z\d\.]/) != nil
                    # puts "found it: #{i}, #{j}, #{@grid[i][j]}"
                    return true
                end
            end
        end
        return false
    end

    def find_part_nums
        state = 'searching'
        part_nums = []
        curr_num = 0
        is_part_num = false
        for i in 0...@grid.length
            for j in 0...@grid[0].length
                val = @grid[i][j]
                finish_part_num = false
                if (val =~ /^\d$/) === 0
                    state = 'reading-number'
                    curr_num = curr_num * 10 + val.to_i
                    check = check_part_num(i, j)
                    # puts "#{i}, #{j} - #{check.inspect}"
                    is_part_num = check || is_part_num
                elsif state == 'reading-number' || j == 0
                    finish_part_num = true
                end

                if finish_part_num || j == @grid[0].length - 1
                    if is_part_num
                        part_nums.append(curr_num)
                    end
                    curr_num = 0
                    state = 'searching'
                    is_part_num = false
                end
            end
        end
        part_nums
    end

    def get_part_num_starting_at(x, y)
        searching = true
        while searching
            y -= 1
            if y < 0
                y = 0
                searching = false
                break
            end

            is_digit = (@grid[x][y] =~ /^\d$/) === 0
            if !is_digit
                searching = false
                y += 1
            end
        end

        num = @grid[x][y].to_i
        searching = true
        while searching
            y += 1
            if y >= @grid[0].length
                searching = false
            end

            is_digit = (@grid[x][y] =~ /^\d$/) === 0
            if is_digit
                num = num * 10 + @grid[x][y].to_i
            else
                searching = false
            end
        end
        num
    end

    def get_gear_ratio(x, y)
        ratio = nil
        if @grid[x][y] != '*'
            return ratio
        end

        part_nums = []
        num_part_nums = 0
        for ii in -1..1
            mode = 'searching'
            for jj in -1..1
                i = ii + x
                j = jj + y
                if i < 0 || j < 0 || i >= @grid.length || j > @grid[0].length
                    next
                end

                is_digit = (@grid[i][j] =~ /^\d$/) === 0
                if is_digit
                    mode = 'in-num'
                elsif mode == 'in-num'
                    mode = 'searching'
                    num_part_nums += 1
                    part_nums.append(get_part_num_starting_at(i, j))
                end
            end
            if mode == 'in-num'
                mode = 'searching'
                num_part_nums += 1
                part_nums.append(get_part_num_starting_at(i, j))                
            end    
        end
        if mode == 'in-num'
            num_part_nums += 1
            part_nums.append(get_part_num_starting_at(i, j))
        end

        # puts part_nums.inspect

        if num_part_nums == 2
            ratio = part_nums.reduce(:*)
        end

        ratio
    end

    def find_gear_ratios
        ratios = []
        for i in 0...@grid.length
            for j in 0...@grid[0].length
                if @grid[i][j] == '*'
                    ratio = get_gear_ratio(i, j)
                    if ratio != nil
                        ratios.push(ratio)
                    end               
                end
            end
        end
        ratios
    end

    def part_one(input)
        parse(input)
        print_grid
        part_nums = find_part_nums
        puts part_nums.inspect
        return part_nums.sum
    end

    def part_two(input)
        ratios = find_gear_ratios
        return ratios.sum
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"